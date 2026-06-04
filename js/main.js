/* ============================================================
   Zoneblox – Main JavaScript (FR)
   ============================================================ */

const ROBLOX_THUMBS = {
  'blox-fruits': 'https://tr.rbxcdn.com/180DAY-e1ce51abae5188805c3fee78ec7f4d08/768/432/Image/Webp/noFilter',
  'pet-simulator-x': 'https://tr.rbxcdn.com/180DAY-a7bb14d2b3dbf586e67ba2ac7a0c3dc7/500/280/Image/Jpeg/noFilter',
  'adopt-me': 'https://tr.rbxcdn.com/180DAY-ef30533fcd5e71af2468030ffa6c176a/500/280/Image/Jpeg/noFilter',
  'murder-mystery-2': 'https://tr.rbxcdn.com/180DAY-5ba706807447783862364dfef7a465ff/500/280/Image/Jpeg/noFilter',
  'royale-high': 'https://tr.rbxcdn.com/180DAY-1c63d3971f06391b08a95400cdf2bb78/500/280/Image/Jpeg/noFilter',
  'brookhaven': 'https://tr.rbxcdn.com/180DAY-5e77d217cbda7ba5941840cfa3ab8c36/768/432/Image/Webp/noFilter',
  'tower-of-hell': 'https://tr.rbxcdn.com/180DAY-20a372111085c33de1e64004e4dca1d8/768/432/Image/Webp/noFilter',
  'work-at-a-pizza-place': 'https://tr.rbxcdn.com/180DAY-3504f0abedb16721aec2f8fcc0da4e2e/768/432/Image/Webp/noFilter',
  'shindo-life': 'https://t3.rbxcdn.com/180DAY-3b2ec062707376a89a223ea44c20d408',
  'king-legacy': 'https://t3.rbxcdn.com/180DAY-e559fde711d62cc11604158b5f39187c',
  'anime-adventures': 'https://t3.rbxcdn.com/180DAY-58d59bfe7584647d43085d18c3e9d679',
  'fruit-battlegrounds': 'https://tr.rbxcdn.com/180DAY-6688078543e2f947bf998f31c4601037/768/432/Image/Png/noFilter',
  'rivals': 'https://tr.rbxcdn.com/180DAY-27507ba164fae9b46c68047d34d0078b/768/432/Image/Png/noFilter',
  'encounters': 'https://tr.rbxcdn.com/180DAY-024bcafc4df055789126ae841598d15d/768/432/Image/Png/noFilter',
};

/* ---- Copy code ---- */
function copyCode(btn, code) {
  navigator.clipboard.writeText(code).then(() => {
    const orig = btn.textContent;
    btn.textContent = 'Copié !';
    btn.classList.add('copied');
    setTimeout(() => { btn.textContent = orig; btn.classList.remove('copied'); }, 2000);
  });
}

/* ---- Mobile nav ---- */
function initMobileNav() {
  const toggle = document.querySelector('.nav-toggle');
  const links  = document.querySelector('.nav-links');
  if (!toggle || !links) return;
  toggle.addEventListener('click', () => links.classList.toggle('mobile-open'));
  document.addEventListener('click', e => {
    if (!toggle.contains(e.target) && !links.contains(e.target))
      links.classList.remove('mobile-open');
  });
}

/* ---- Search index ---- */
const GAMES_INDEX = [
  { name: 'Blox Fruits',         slug: 'blox-fruits',          emoji: '🍎', codes: 5 },
  { name: 'Pet Simulator X',     slug: 'pet-simulator-x',      emoji: '🐾', codes: 8 },
  { name: 'Adopt Me',            slug: 'adopt-me',             emoji: '🐣', codes: 3 },
  { name: 'Anime Adventures',    slug: 'anime-adventures',     emoji: '⚔️', codes: 6 },
  { name: 'Brookhaven',          slug: 'brookhaven',           emoji: '🏙️', codes: 2 },
  { name: 'Tower of Hell',       slug: 'tower-of-hell',        emoji: '🗼', codes: 0 },
  { name: 'Murder Mystery 2',    slug: 'murder-mystery-2',     emoji: '🔪', codes: 4 },
  { name: 'Shindo Life',         slug: 'shindo-life',          emoji: '🌀', codes: 12 },
  { name: 'Royale High',         slug: 'royale-high',          emoji: '👑', codes: 1 },
  { name: 'Fruit Battlegrounds', slug: 'fruit-battlegrounds',  emoji: '💥', codes: 7 },
  { name: 'King Legacy',         slug: 'king-legacy',          emoji: '⚡', codes: 9 },
  { name: 'Encounters',          slug: 'encounters',           emoji: '👾', codes: 4 },
  { name: 'Rivals',              slug: 'rivals',               emoji: '🎯', codes: 5 },
];

function gameResultHTML(g) {
  return `
    <a class="search-result-item" href="/codes/${g.slug}.html">
      <img src="${ROBLOX_THUMBS[g.slug]||('/images/games/'+g.slug+'.svg')}" alt="${g.name}" style="width:38px;height:38px;border-radius:7px;object-fit:cover;flex-shrink:0" onerror="this.onerror=null;this.src='/images/games/'+g.slug+'.svg'">
      <div>
        <div style="font-size:.88rem;font-weight:600;color:var(--text-primary)">${g.name}</div>
        <div style="font-size:.75rem;color:var(--text-muted)">${g.codes} code${g.codes !== 1 ? 's' : ''} actif${g.codes !== 1 ? 's' : ''}</div>
      </div>
    </a>`;
}

function initSearch() {
  const input   = document.getElementById('searchInput');
  const results = document.getElementById('searchResults');
  if (!input || !results) return;

  input.addEventListener('input', () => {
    const q = input.value.trim().toLowerCase();
    if (q.length < 2) { results.classList.remove('open'); return; }

    const matches = GAMES_INDEX.filter(g => g.name.toLowerCase().includes(q)).slice(0, 6);
    if (!matches.length) { results.classList.remove('open'); return; }

    results.innerHTML = matches.map(gameResultHTML).join('');
    results.classList.add('open');
  });

  document.addEventListener('click', e => {
    if (!input.contains(e.target) && !results.contains(e.target))
      results.classList.remove('open');
  });
}

/* ---- Hero search (page d'accueil) ---- */
function initHeroSearch() {
  const heroInput   = document.getElementById('heroSearch');
  const heroResults = document.getElementById('heroSearchResults');
  if (!heroInput || !heroResults) return;

  heroInput.addEventListener('input', () => {
    const q = heroInput.value.trim().toLowerCase();
    if (q.length < 2) { heroResults.classList.remove('open'); return; }
    const matches = GAMES_INDEX.filter(g => g.name.toLowerCase().includes(q)).slice(0, 6);
    if (!matches.length) { heroResults.classList.remove('open'); return; }
    heroResults.innerHTML = matches.map(gameResultHTML).join('');
    heroResults.classList.add('open');
  });

  document.addEventListener('click', e => {
    if (!heroInput.contains(e.target) && !heroResults.contains(e.target))
      heroResults.classList.remove('open');
  });
}

/* ---- Newsletter ---- */
function initNewsletter() {
  document.querySelectorAll('.newsletter-form').forEach(form => {
    form.addEventListener('submit', e => {
      e.preventDefault();
      const inp = form.querySelector('input[type="email"]');
      const btn = form.querySelector('button');
      if (!inp.value) return;
      const orig = btn.textContent;
      btn.textContent = '✓ Inscrit !';
      btn.disabled = true;
      inp.value = '';
      setTimeout(() => { btn.textContent = orig; btn.disabled = false; }, 3000);
    });
  });
}

/* ---- Active nav link ---- */
function highlightNav() {
  const path = location.pathname;
  document.querySelectorAll('.nav-links a').forEach(a => {
    a.classList.toggle('active', a.getAttribute('href') === path ||
      (path.includes('/codes/') && a.getAttribute('href') === '/codes/'));
  });
}

/* ---- Roblox Official Thumbnails Loader ---- */
const ROBLOX_UNIVERSE_IDS = {
  'blox-fruits':           2753915549,
  'pet-simulator-x':       6284583030,
  'adopt-me':              920587237,
  'shindo-life':           6017744795,
  'king-legacy':           6096648965,
  'murder-mystery-2':      142823291,
  'fruit-battlegrounds':   3457700596,
  'anime-adventures':      7974552544,
  'rivals':                6035872082,
  'brookhaven':            4924922222,
  'royale-high':           735030788,
  'encounters':            2918970982,
  'tower-of-hell':         1962086868,
  'work-at-a-pizza-place': 192800,
};

const _thumbCache = {};

function applyRobloxThumbs() {
  Object.entries(_thumbCache).forEach(([slug, url]) => {
    document.querySelectorAll(`img[data-game="${slug}"]`).forEach(img => {
      if (img.getAttribute('src') !== url) {
        img.style.opacity = '0';
        img.src = url;
        img.onload = () => {
          img.style.transition = 'opacity .35s';
          img.style.opacity = '1';
        };
      }
    });
  });
}
window.applyRobloxThumbs = applyRobloxThumbs;

async function loadRobloxThumbnails() {
  if (Object.keys(_thumbCache).length > 0) { applyRobloxThumbs(); return; }
  try {
    const res = await fetch('/api/thumbnails', { headers: { 'Accept': 'application/json' } });
    if (!res.ok) return;
    const json = await res.json();
    Object.entries(json).forEach(([slug, url]) => { if (url) _thumbCache[slug] = url; });
    applyRobloxThumbs();
  } catch(e) {
    console.log('API miniatures Roblox indisponible — utilisation des SVG de secours.');
  }
}

/* ---- Vidéos YouTube (3 plus récentes & populaires par jeu) ---- */
// Colle ta clé API YouTube Data v3 ici (gratuite, à restreindre au domaine zoneblox.com) :
const YOUTUBE_API_KEY = 'AIzaSyCvalvjmUJryGAP_Xg_NEjhrwk_7GAbD3A';

function renderYouTube(grid, items) {
  grid.innerHTML = items.map(v => `
    <div class="video-card">
      <div class="video-embed">
        <iframe src="https://www.youtube.com/embed/${v.id}" title="${(v.title||'').replace(/"/g,'&quot;')}" allowfullscreen loading="lazy"></iframe>
      </div>
      <div class="video-label">🎬 ${v.title||''}</div>
    </div>`).join('');
}

function initYouTubeVideos() {
  const grid = document.querySelector('#tab-videos .videos-grid');
  if (!grid) return;
  if (!YOUTUBE_API_KEY) return; // pas de clé → on garde le bouton de secours

  const m = location.pathname.match(/\/codes\/([a-z0-9-]+)\.html/i);
  if (!m) return;
  const slug = m[1];
  const game = (GAMES_INDEX.find(g => g.slug === slug) || {}).name || slug.replace(/-/g, ' ');
  const query = game + ' Roblox'; // vidéos populaires du jeu (pas les tutos de codes concurrents)
  const cacheKey = 'yt_' + slug;

  // Cache navigateur 12h pour limiter la consommation de quota
  try {
    const c = JSON.parse(localStorage.getItem(cacheKey) || 'null');
    if (c && (Date.now() - c.t < 43200000) && c.items && c.items.length) {
      renderYouTube(grid, c.items); return;
    }
  } catch (e) {}

  const since = new Date(Date.now() - 180 * 86400000).toISOString();
  const url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&maxResults=3'
            + '&order=viewCount&relevanceLanguage=fr'
            + '&publishedAfter=' + encodeURIComponent(since)
            + '&q=' + encodeURIComponent(query)
            + '&key=' + YOUTUBE_API_KEY;

  fetch(url)
    .then(r => r.json())
    .then(j => {
      const items = (j.items || [])
        .map(it => ({ id: it.id && it.id.videoId, title: it.snippet && it.snippet.title }))
        .filter(x => x.id);
      if (!items.length) return; // on garde le bouton de secours
      try { localStorage.setItem(cacheKey, JSON.stringify({ t: Date.now(), items })); } catch (e) {}
      renderYouTube(grid, items);
    })
    .catch(() => { /* en cas d'erreur, le bouton de secours reste affiché */ });
}

/* ---- Init ---- */
document.addEventListener('DOMContentLoaded', () => {
  initMobileNav();
  initSearch();
  initHeroSearch();
  initNewsletter();
  highlightNav();
  loadRobloxThumbnails();
  initYouTubeVideos();
});
