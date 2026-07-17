#!/usr/bin/env node
/**
 * universal_scrape.js — Universal scraping toolkit for OpenClaw
 * Works on Android ARM64 with NO browser, NO binary, NO system packages.
 *
 * Layer 1: Jina Reader — server-side JS rendering (any URL → clean Markdown)
 * Layer 2: Curl fallback — SSL workaround + Cheerio for static HTML
 * Layer 3: YouTube Innertube API — video search without browser
 */
import { load } from 'cheerio';
import { execSync } from 'child_process';

// ============================================================================
// LAYER 1 — JINA READER
// Best for: JavaScript-heavy SPAs, complex sites, any URL
// ============================================================================
async function jinaRead(url) {
  const res = await fetch(`https://r.jina.ai/${encodeURIComponent(url)}`, {
    headers: {
      'Accept': 'text/markdown',
      'X-Return-Format': 'markdown',
      'User-Agent': 'Mozilla/5.0',
    }
  });
  if (!res.ok) {
    return { error: `Jina returned ${res.status}`, url };
  }
  const text = await res.text();
  return { url, text, chars: text.length };
}

// ============================================================================
// LAYER 2 — CURL + CHEERIO (Static HTML parsing)
// Best for: Simple sites, well-structured HTML
// ============================================================================
async function scrape(url, options = {}) {
  const { selectors = {} } = options;
  let html;
  
  // Use curl with -k to bypass SSL cert verification (PRoot environment issue)
  try {
    html = execSync(`curl -skL "${url}"`, { timeout: 15000 }).toString();
  } catch (e) {
    return { url, error: `Failed to fetch: ${e.message}`, status: 0 };
  }
  
  const $ = load(html);
  $('script, style, nav, header, footer, aside, noscript, meta, link, svg').remove();
  
  const result = {
    url,
    title: $('title').first().text().trim(),
    meta: {
      description: $('meta[name="description"]').attr('content') || '',
      author: $('meta[name="author"]').attr('content') || '',
    },
    text: $('body').text().replace(/\s+/g, ' ').trim(),
    links: [],
  };

  if (selectors.items) {
    result.items = $(selectors.items).map((i, el) => ({
      text: $(el).text().trim().slice(0, 200),
      href: $(el).attr('href') || '',
    })).get();
  }

  $('a[href]').filter((i, el) => $(el).attr('href').startsWith('http')).slice(0, 30)
    .each((i, el) => result.links.push({
      text: $(el).text().trim().slice(0, 80),
      url: $(el).attr('href'),
    }));

  return result;
}

// ============================================================================
// LAYER 3 — YOUTUBE INNERTUBE API
// Best for: YouTube search, video details, no browser needed
// ============================================================================
async function youtubeSearch(query, limit = 10) {
  const res = await fetch('https://www.youtube.com/youtubei/v1/search?prettyPrint=false', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      context: { client: { clientName: 'WEB', clientVersion: '2.20200720.00.00' } },
      query: query
    })
  });
  const data = await res.json();
  const items = data.contents?.twoColumnSearchResultsRenderer?.primaryContents?.sectionListRenderer?.contents?.[0]?.itemSectionRenderer?.contents || [];
  return items.filter(i => i.videoRenderer).slice(0, limit).map(v => ({
    id: v.videoRenderer.videoId,
    title: v.videoRenderer.title?.runs?.[0]?.text,
    channel: v.videoRenderer.ownerText?.runs?.[0]?.text,
    duration: v.videoRenderer.lengthText?.simpleText,
    views: v.videoRenderer.viewCountText?.simpleText,
    url: 'https://youtube.com/watch?v=' + v.videoRenderer.videoId,
  }));
}

async function youtubeVideo(videoId) {
  const res = await fetch('https://www.youtube.com/youtubei/v1/player?prettyPrint=false', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      context: { client: { clientName: 'WEB', clientVersion: '2.20200720.00.00' } },
      videoId
    })
  });
  const data = await res.json();
  const d = data.videoDetails;
  return {
    id: d?.videoId,
    title: d?.title,
    author: d?.author,
    description: d?.shortDescription,
    viewCount: d?.viewCount,
    lengthSeconds: d?.lengthSeconds,
    url: 'https://youtube.com/watch?v=' + videoId,
  };
}

// ============================================================================
// CLI
// ============================================================================
const args = process.argv.slice(2);
const cmd = args[0];

if (cmd === 'jina') {
  const url = args[1];
  const result = await jinaRead(url);
  if (result.error) { console.error('Error:', result.error); process.exit(1); }
  console.log(result.text);

} else if (cmd === 'scrape') {
  const url = args[1];
  const result = await scrape(url);
  console.log(`Title: ${result.title}`);
  console.log(`Links: ${result.links.length} | Words: ${result.text.split(' ').length}`);
  console.log(`\nText preview:\n${result.text.slice(0, 600)}`);

} else if (cmd === 'yt-search') {
  const query = args.slice(1).join(' ');
  const results = await youtubeSearch(query);
  console.log(`\nYouTube: "${query}"\n`);
  results.forEach((v, i) => {
    console.log(`${i+1}. [${v.id}] ${v.title}`);
    console.log(`   ${v.channel} | ${v.duration || 'LIVE'} | ${v.views || '?'}\n`);
  });

} else if (cmd === 'yt-video') {
  const id = args[1];
  const v = await youtubeVideo(id);
  console.log(`\n${v.title}\nBy: ${v.author} | ${v.viewCount} views | ${v.lengthSeconds}s\n${v.url}\n`);
  console.log(`Description:\n${(v.description || '').slice(0, 500)}`);

} else {
  console.log(`
Universal Scrape — No Browser Required
======================================

  node universal_scrape.js jina <url>       Jina Reader (JS sites + any URL)
  node universal_scrape.js scrape <url>      Curl + Cheerio (static HTML)
  node universal_scrape.js yt-search <q>    YouTube search (API)
  node universal_scrape.js yt-video <id>     YouTube video details

Examples:
  node universal_scrape.js jina "https://news.ycombinator.com"
  node universal_scrape.js jina "https://twitter.com/user/status/123"
  node universal_scrape.js scrape "https://example.com"
  node universal_scrape.js yt-search "AI agents 2026"
  node universal_scrape.js yt-video dQw4w9WgXcQ
`);
}
