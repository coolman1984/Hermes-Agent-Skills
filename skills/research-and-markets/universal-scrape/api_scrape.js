#!/usr/bin/env node
/**
 * api_scrape.js — Public API toolkit for OpenClaw
 * Direct JSON APIs for major platforms — no scraping needed
 * 
 * Works on Android ARM64 / Termux / PRoot with NO browser.
 * All via Node.js built-in fetch + JSDOM for HTML parsing.
 */
import { JSDOM } from 'jsdom';

// ============================================================================
// HACKER NEWS — 2 APIs
// ============================================================================
async function hnTop(limit = 10) {
  // Firebase API (fastest, official)
  const res = await fetch('https://hacker-news.firebaseio.com/v0/topstories.json');
  const ids = await res.json();
  const stories = await Promise.all(ids.slice(0, limit).map(async id => {
    const r = await fetch(`https://hacker-news.firebaseio.com/v0/item/${id}.json`);
    return r.json();
  }));
  return stories.map((s, i) => ({
    rank: i + 1,
    title: s.title,
    score: s.score,
    comments: s.descendants || 0,
    author: s.by,
    url: s.url || `https://news.ycombinator.com/item?id=${s.id}`,
    id: s.id,
  }));
}

async function hnSearch(query, limit = 5) {
  // Algolia API (search + top stories)
  const res = await fetch(
    `https://hn.algolia.com/api/v1/search?query=${encodeURIComponent(query)}&hitsPerPage=${limit}&tags=story`
  );
  const data = await res.json();
  return data.hits.map((h, i) => ({
    rank: i + 1,
    title: h.title || h.story_title || 'N/A',
    url: h.url || h.story_url || `https://news.ycombinator.com/item?id=${h.objectID}`,
    author: h.author,
    points: h.points,
    comments: h.num_comments,
  }));
}

// ============================================================================
// GITHUB
// ============================================================================
async function githubRepo(owner, repo) {
  const res = await fetch(`https://api.github.com/repos/${owner}/${repo}`, {
    headers: { 'User-Agent': 'Mozilla/5.0' }
  });
  if (!res.ok) return { error: `GitHub API returned ${res.status}` };
  const d = await res.json();
  return {
    name: d.full_name,
    description: d.description,
    stars: d.stargazers_count,
    forks: d.forks_count,
    language: d.language,
    url: d.html_url,
    created: d.created_at,
  };
}

async function githubSearch(query, limit = 5) {
  const res = await fetch(
    `https://api.github.com/search/repositories?q=${encodeURIComponent(query)}&per_page=${limit}&sort=stars`,
    { headers: { 'User-Agent': 'Mozilla/5.0' } }
  );
  const d = await res.json();
  return (d.items || []).map(r => ({
    name: r.full_name,
    description: r.description,
    stars: r.stargazers_count,
    language: r.language,
    url: r.html_url,
  }));
}

// ============================================================================
// YOUTUBE — Innertube API
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
// CRYPTOCURRENCY
// ============================================================================
async function cryptoPrice(coins = ['bitcoin', 'ethereum', 'solana']) {
  const res = await fetch(
    `https://api.coingecko.com/api/v3/simple/price?ids=${coins.join(',')}&vs_currencies=usd&include_24hr_change=true`
  );
  const data = await res.json();
  return Object.entries(data).map(([coin, info]) => ({
    coin: coin.charAt(0).toUpperCase() + coin.slice(1),
    price: `$${info.usd?.toLocaleString() || '?'}`,
    change24h: `${info.usd_24h_change?.toFixed(2) || '?'}%`,
  }));
}

// ============================================================================
// WIKIPEDIA
// ============================================================================
async function wikipedia(page) {
  const res = await fetch(
    `https://en.wikipedia.org/api/rest_v1/page/summary/${encodeURIComponent(page)}`
  );
  const d = await res.json();
  return {
    title: d.title,
    extract: d.extract,
    url: d.content_urls?.desktop?.page || '',
    image: d.thumbnail?.source || '',
  };
}

async function wikipediaSearch(query, limit = 5) {
  const res = await fetch(
    `https://en.wikipedia.org/w/api.php?action=opensearch&search=${encodeURIComponent(query)}&limit=${limit}&format=json`
  );
  const [query_, titles, descs, urls] = await res.json();
  return titles.map((t, i) => ({
    title: t,
    description: descs[i] || '',
    url: urls[i] || '',
  }));
}

// ============================================================================
// STACKOVERFLOW
// ============================================================================
async function stackoverflow(tag, limit = 5) {
  const res = await fetch(
    `https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&tagged=${encodeURIComponent(tag)}&site=stackoverflow&pagesize=${limit}`
  );
  const d = await res.json();
  return d.items.map(q => ({
    title: q.title,
    tags: q.tags,
    score: q.score,
    answers: q.answer_count,
    url: q.link,
    asked: new Date(q.creation_date * 1000).toLocaleDateString(),
  }));
}

// ============================================================================
// COUNTRIES
// ============================================================================
async function country(name) {
  const res = await fetch(
    `https://restcountries.com/v3.1/name/${encodeURIComponent(name)}?fullText=true`
  );
  const data = await res.json();
  return data.map(c => ({
    name: c.name.common,
    capital: c.capital?.[0] || 'N/A',
    population: c.population?.toLocaleString() || '?',
    region: c.region,
    currencies: Object.values(c.currencies || {}).map(c => c.name).join(', ') || 'N/A',
    languages: Object.values(c.languages || {}).join(', ') || 'N/A',
    flag: c.flags?.svg || c.flags?.png || '',
  }));
}

// ============================================================================
// JSDOM HTML SCRAPING
// ============================================================================
async function scrape(url, selectors = {}) {
  const res = await fetch(url, {
    headers: { 'User-Agent': 'Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36' }
  });
  const html = await res.text();
  const dom = new JSDOM(html);
  const doc = dom.window.document;
  
  const result = {
    url,
    status: res.status,
    title: doc.title,
    text: doc.body?.textContent?.replace(/\s+/g, ' ').trim() || '',
    links: [],
  };
  
  if (selectors.title) result.title = doc.querySelector(selectors.title)?.textContent?.trim() || result.title;
  if (selectors.text) result.text = doc.querySelector(selectors.text)?.textContent?.replace(/\s+/g, ' ').trim() || result.text;
  
  // Extract links
  doc.querySelectorAll('a[href]').forEach(a => {
    const href = a.href;
    if (href.startsWith('http') && !href.includes(url.split('/')[2])) {
      result.links.push({ text: a.textContent.trim().slice(0, 60), url: href });
    }
  });
  
  return result;
}

// ============================================================================
// CLI
// ============================================================================
const args = process.argv.slice(2);
const cmd = args[0];

async function main() {
  if (cmd === 'hn-top') {
    const stories = await hnTop(parseInt(args[1]) || 10);
    console.log('\n🔴 Hacker News Top Stories\n');
    stories.forEach(s => {
      console.log(`${s.rank}. ${s.title}`);
      console.log(`   ⬆ ${s.score} | 💬 ${s.comments} | by ${s.author}`);
      console.log(`   ${s.url}\n`);
    });

  } else if (cmd === 'hn-search') {
    const results = await hnSearch(args.slice(1).join(' ') || 'AI', parseInt(args[1]) || 5);
    console.log(`\n🔴 HN Search: "${args.slice(1).join(' ')}"\n`);
    results.forEach(s => {
      console.log(`${s.rank}. ${s.title}`);
      console.log(`   ⬆ ${s.points} | 💬 ${s.comments} | ${s.url}\n`);
    });

  } else if (cmd === 'yt-search') {
    const results = await youtubeSearch(args.slice(1).join(' '));
    console.log(`\n📺 YouTube: "${args.slice(1).join(' ')}"\n`);
    results.forEach((v, i) => {
      console.log(`${i+1}. [${v.id}] ${v.title}`);
      console.log(`   ${v.channel} | ${v.duration || 'LIVE'} | ${v.views}\n`);
    });

  } else if (cmd === 'yt-video') {
    const v = await youtubeVideo(args[1]);
    console.log(`\n🎬 ${v.title}\nBy: ${v.author} | ${Number(v.viewCount).toLocaleString()} views | ${Math.floor(v.lengthSeconds/60)}:${String(v.lengthSeconds%60).padStart(2,'0')}\n${v.url}\n`);
    console.log(`Description:\n${(v.description||'').slice(0,300)}`);

  } else if (cmd === 'gh-repo') {
    const [owner, repo] = args[1].split('/');
    const r = await githubRepo(owner, repo);
    if (r.error) { console.log('Error:', r.error); return; }
    console.log(`\n🐙 ${r.name}\n⭐ ${r.stars?.toLocaleString()} | 🍴 ${r.forks?.toLocaleString()} | ${r.language}\n${r.description}\n${r.url}`);

  } else if (cmd === 'gh-search') {
    const results = await githubSearch(args.slice(1).join(' '));
    console.log(`\n🐙 GitHub: "${args.slice(1).join(' ')}"\n`);
    results.forEach(r => {
      console.log(`⭐ ${r.stars?.toLocaleString()} | ${r.language || 'N/A'} | ${r.name}`);
      console.log(`   ${r.description || ''}\n`);
    });

  } else if (cmd === 'crypto') {
    const prices = await cryptoPrice(['bitcoin', 'ethereum', 'solana', 'cardano', 'ripple']);
    console.log('\n💰 Crypto Prices\n');
    prices.forEach(c => console.log(`${c.coin.padEnd(10)} ${c.price.padEnd(12)} ${c.change24h}`));

  } else if (cmd === 'wiki') {
    const w = await wikipedia(args.slice(1).join(' ') || 'Artificial_intelligence');
    console.log(`\n📚 ${w.title}\n${w.extract}\n${w.url}`);

  } else if (cmd === 'wiki-search') {
    const results = await wikipediaSearch(args.slice(1).join(' '));
    console.log(`\n📚 Wikipedia: "${args.slice(1).join(' ')}"\n`);
    results.forEach(r => console.log(`• ${r.title}\n  ${r.description}\n  ${r.url}\n`));

  } else if (cmd === 'so') {
    const questions = await stackoverflow(args[1] || 'python', parseInt(args[2]) || 5);
    console.log(`\n💻 StackOverflow: [${args[1] || 'python'}]\n`);
    questions.forEach(q => {
      console.log(`${q.title}`);
      console.log(`   🏷️ ${q.tags.join(', ')} | ⬆ ${q.score} | 💬 ${q.answers} | ${q.asked}`);
      console.log(`   ${q.url}\n`);
    });

  } else if (cmd === 'country') {
    const countries = await country(args.slice(1).join(' ') || 'Egypt');
    countries.forEach(c => {
      console.log(`\n🌍 ${c.name}`);
      console.log(`Capital: ${c.capital} | Population: ${c.population} | Region: ${c.region}`);
      console.log(`Currency: ${c.currencies} | Languages: ${c.languages}`);
    });

  } else if (cmd === 'scrape') {
    const result = await scrape(args[1]);
    console.log(`\n🌐 ${result.title}\n`);
    console.log(result.text.slice(0, 500));
    console.log(`\n[Links: ${result.links.length}]`);

  } else {
    console.log(`
API Scrape — No Browser Required
================================

  node api_scrape.js hn-top [n]         Hacker News top stories (default: 10)
  node api_scrape.js hn-search <q> [n]   HN search (Algolia API)
  node api_scrape.js yt-search <q>       YouTube search
  node api_scrape.js yt-video <id>       YouTube video details
  node api_scrape.js gh-repo <owner/repo> GitHub repo info
  node api_scrape.js gh-search <q>       GitHub repo search
  node api_scrape.js crypto              Crypto prices (BTC,ETH,SOL,ADA,XRP)
  node api_scrape.js wiki <page>        Wikipedia summary
  node api_scrape.js wiki-search <q>    Wikipedia search
  node api_scrape.js so <tag> [n]       StackOverflow questions
  node api_scrape.js country <name>     Country info
  node api_scrape.js scrape <url>       Scrape any HTML page with JSDOM

Examples:
  node api_scrape.js hn-top 5
  node api_scrape.js hn-search AI 5
  node api_scrape.js yt-search "AI agents 2026"
  node api_scrape.js gh-repo torvalds/linux
  node api_scrape.js gh-search "machine learning framework"
  node api_scrape.js crypto
  node api_scrape.js wiki "Machine learning"
  node api_scrape.js so javascript 3
  node api_scrape.js country Egypt
`);
  }
}

main().catch(e => { console.error('Error:', e.message); process.exit(1); });
