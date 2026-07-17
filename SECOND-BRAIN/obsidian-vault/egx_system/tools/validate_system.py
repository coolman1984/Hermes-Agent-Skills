#!/usr/bin/env python3
import csv
import json
import re
import shutil
from collections import Counter
from pathlib import Path

ROOT = Path('/root/Documents/Obsidian Vault')
EGX = ROOT / 'egx_system'
MANIFEST = EGX / 'ai_manifest.json'
AI_START = EGX / 'AI-START-HERE.md'
AI_PROMPT = EGX / 'AI-HANDOFF-PROMPT.md'
RUNBOOK = EGX / 'EGX-SESSION-RUNBOOK.md'
POSITIONS = EGX / 'portfolio' / 'positions.csv'
WATCHLIST = EGX / 'portfolio' / 'watchlist.txt'
MARKET_CONFIG = Path('/root/.hermes/profiles/market/config.yaml')
MARKETLAB_CONFIG = Path('/root/.hermes/profiles/marketlab/config.yaml')
MARKET_JOBS = Path('/root/.hermes/profiles/market/cron/jobs.json')
MARKET_WEEKLY_SKILL = Path('/root/.hermes/profiles/market/skills/note-taking/egx-weekly-review/SKILL.md')

EXPECTED_STATUSES = {'hold', 'review', 'reduce', 'exit'}
EXPECTED_WEEKLY_JOB_ID = '3885f822a7b0'


def read_text(path):
    return path.read_text(encoding='utf-8')


def check_path(path_str):
    p = Path(path_str)
    return {
        'path': str(p),
        'exists': p.exists(),
        'type': 'file' if p.is_file() else 'dir' if p.is_dir() else 'missing'
    }


def extract_backtick_paths(text):
    return re.findall(r'`(/root[^`]+)`', text)


def parse_positions():
    rows = list(csv.DictReader(POSITIONS.open(encoding='utf-8')))
    statuses = Counter(r['status'].strip() for r in rows)
    roles = [r['role'].strip() for r in rows]
    return rows, statuses, roles


def parse_watchlist():
    return [line.strip() for line in WATCHLIST.read_text(encoding='utf-8').splitlines() if line.strip()]


def latest_daily_json():
    daily_dir = EGX / 'reports' / 'daily'
    candidates = sorted(daily_dir.glob('daily-local-review-*.json'))
    return candidates[-1] if candidates else None


def read_timezone(config_path):
    text = read_text(config_path)
    m = re.search(r'^timezone:\s*(.*)$', text, re.M)
    if not m:
        return None
    val = m.group(1).strip().strip("'").strip('"')
    return val or None


def load_jobs():
    if not MARKET_JOBS.exists():
        return []
    return json.loads(read_text(MARKET_JOBS)).get('jobs', [])


def main():
    result = {
        'paths': {},
        'coherence': {},
        'portfolio': {},
        'reports': {},
        'cron': {},
        'commands': {},
        'warnings': [],
        'errors': []
    }

    if not MANIFEST.exists():
        result['errors'].append('Manifest missing.')
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1

    manifest = json.loads(read_text(MANIFEST))
    result['paths']['entrypoint'] = check_path(manifest['entrypoint'])
    result['paths']['mandatory_read_order'] = [check_path(p) for p in manifest.get('mandatory_read_order', [])]
    result['paths']['authoritative_files_priority'] = [check_path(p) for p in manifest.get('authoritative_files_priority', [])]

    ai_start_paths = extract_backtick_paths(read_text(AI_START))
    manifest_paths = manifest.get('mandatory_read_order', [])
    result['coherence']['ai_start_missing_manifest_paths'] = [p for p in manifest_paths if p not in ai_start_paths]
    result['coherence']['ai_start_extra_paths'] = [p for p in ai_start_paths if p not in manifest_paths]
    if result['coherence']['ai_start_missing_manifest_paths']:
        result['errors'].append('AI-START-HERE read order does not fully match manifest.')

    prompt_text = read_text(AI_PROMPT)
    result['coherence']['prompt_mentions_ai_start'] = 'AI-START-HERE' in prompt_text
    result['coherence']['prompt_mentions_runbook'] = 'EGX-SESSION-RUNBOOK' in prompt_text
    if not result['coherence']['prompt_mentions_ai_start']:
        result['errors'].append('AI-HANDOFF-PROMPT does not mention AI-START-HERE.')
    if not result['coherence']['prompt_mentions_runbook']:
        result['errors'].append('AI-HANDOFF-PROMPT does not mention EGX-SESSION-RUNBOOK.')

    rows, statuses, roles = parse_positions()
    watchlist = parse_watchlist()
    symbols = [r['symbol'].strip() for r in rows]
    result['portfolio']['positions_count'] = len(rows)
    result['portfolio']['status_counts'] = dict(statuses)
    result['portfolio']['unknown_statuses'] = sorted(set(statuses) - EXPECTED_STATUSES)
    result['portfolio']['watchlist_count'] = len(watchlist)
    result['portfolio']['watchlist_not_in_positions'] = [w for w in watchlist if w not in symbols]
    result['portfolio']['duplicate_symbols'] = sorted([s for s, c in Counter(symbols).items() if c > 1])
    result['portfolio']['core_count'] = sum(1 for r in roles if r.startswith('core_'))
    result['portfolio']['acceleration_count'] = sum(1 for r in roles if r.startswith('acceleration_'))
    if result['portfolio']['unknown_statuses']:
        result['errors'].append('Unknown statuses found in positions.csv.')
    if result['portfolio']['watchlist_not_in_positions']:
        result['errors'].append('Watchlist contains symbols absent from positions.csv.')
    if result['portfolio']['duplicate_symbols']:
        result['errors'].append('Duplicate symbols found in positions.csv.')

    latest_json = latest_daily_json()
    result['reports']['latest_daily_json'] = str(latest_json) if latest_json else None
    result['reports']['latest_daily_exists'] = latest_json is not None
    if latest_json:
        data = json.loads(read_text(latest_json))
        latest_status_counts = data.get('status_counts', {})
        result['reports']['latest_daily_status_counts'] = latest_status_counts
        result['reports']['latest_daily_matches_current_positions'] = latest_status_counts == dict(statuses)
        if not result['reports']['latest_daily_matches_current_positions']:
            result['warnings'].append('Latest daily JSON is stale relative to current positions.csv status counts.')
    else:
        result['warnings'].append('No daily JSON report found.')

    result['paths']['runbook'] = check_path(str(RUNBOOK))
    if not result['paths']['runbook']['exists']:
        result['errors'].append('Session runbook missing.')

    result['reports']['weekly_reports_exist'] = any((EGX / 'reports' / 'weekly').glob('*.md'))
    result['reports']['monthly_reports_exist'] = any((EGX / 'reports' / 'monthly').glob('*.md'))
    if not result['reports']['weekly_reports_exist']:
        result['warnings'].append('No weekly report exists yet.')

    market_tz = read_timezone(MARKET_CONFIG)
    marketlab_tz = read_timezone(MARKETLAB_CONFIG)
    result['cron']['market_timezone'] = market_tz
    result['cron']['marketlab_timezone'] = marketlab_tz
    if market_tz != 'Africa/Cairo':
        result['warnings'].append('market profile timezone is not explicitly Africa/Cairo.')
    if marketlab_tz != 'Africa/Cairo':
        result['warnings'].append('marketlab profile timezone is not explicitly Africa/Cairo.')

    jobs = load_jobs()
    result['cron']['job_count'] = len(jobs)
    weekly_job = next((j for j in jobs if j.get('id') == EXPECTED_WEEKLY_JOB_ID), None)
    result['cron']['weekly_job_present'] = weekly_job is not None
    result['cron']['weekly_skill_exists'] = MARKET_WEEKLY_SKILL.exists()
    if weekly_job:
        result['cron']['weekly_job_skills'] = weekly_job.get('skills', [])
        result['cron']['weekly_job_schedule'] = weekly_job.get('schedule_display')
        if 'egx-weekly-review' not in weekly_job.get('skills', []):
            result['warnings'].append('Weekly cron job is not attached to egx-weekly-review skill.')
    else:
        result['errors'].append('Weekly cron job missing.')
    if not MARKET_WEEKLY_SKILL.exists():
        result['warnings'].append('egx-weekly-review skill is missing from market profile.')

    verified = []
    for cmd in manifest.get('verified_commands', []):
        binary = cmd.split()[0]
        verified.append({'command': cmd, 'binary_found': shutil.which(binary) is not None})
    result['commands']['verified'] = verified
    if not all(v['binary_found'] for v in verified):
        result['errors'].append('One or more verified command binaries are missing.')

    result['summary'] = {
        'all_mandatory_paths_exist': all(x['exists'] for x in result['paths']['mandatory_read_order']),
        'all_authoritative_paths_exist': all(x['exists'] for x in result['paths']['authoritative_files_priority']),
        'error_count': len(result['errors']),
        'warning_count': len(result['warnings'])
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not result['errors'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
