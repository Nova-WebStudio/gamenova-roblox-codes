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
  'grow-a-garden': 'https://tr.rbxcdn.com/180DAY-028e7742f4ef789f654bf0dd91502b41/768/432/Image/Png/noFilter',
  'blade-ball': 'https://tr.rbxcdn.com/180DAY-aa0679c96e6ce33f961087cebcc07ce6/768/432/Image/Png/noFilter',
  'anime-defenders': 'https://tr.rbxcdn.com/180DAY-c5a2289b4baf7194add46247482074d7/768/432/Image/Png/noFilter',
  'toilet-tower-defense': 'https://tr.rbxcdn.com/180DAY-5a9d6ca7af3e521497366c956bbbea05/768/432/Image/Png/noFilter',
  'pet-simulator-99': 'https://tr.rbxcdn.com/180DAY-b7b8ad3ad6f4103c91efc25da7bc1118/768/432/Image/Png/noFilter',
  'bee-swarm-simulator': 'https://tr.rbxcdn.com/180DAY-315e29556054777604420711cb64f0b6/768/432/Image/Png/noFilter',
  'anime-vanguards': 'https://tr.rbxcdn.com/180DAY-cb38398e8a1315ca4046f168c7504d6b/768/432/Image/Png/noFilter',
  'arsenal': 'https://tr.rbxcdn.com/180DAY-fd5d29ef7df403915891862d02ae09bb/768/432/Image/Png/noFilter',
  'jailbreak': 'https://tr.rbxcdn.com/180DAY-fef285ce1b8ac805b17da2a4f998ccec/768/432/Image/Png/noFilter',
  'bedwars': 'https://tr.rbxcdn.com/180DAY-9e34b6ee9e93b7840f82d1381d14c641/768/432/Image/Png/noFilter',
  'fisch': 'https://tr.rbxcdn.com/180DAY-0b48b36aaaebb05f29da4beb58790100/768/432/Image/Png/noFilter',
  'dress-to-impress': 'https://tr.rbxcdn.com/180DAY-62de69073c3ab87818fa79cd9d34006b/768/432/Image/Png/noFilter',
  'da-hood': 'https://tr.rbxcdn.com/180DAY-655a8b7fc990b48f595db9bcfd7ea70b/768/432/Image/Png/noFilter',
  'bubble-gum-simulator-infinity': 'https://tr.rbxcdn.com/180DAY-7c76a88ace2e799826837aee08875eec/768/432/Image/Png/noFilter',
  'blue-lock-rivals': 'https://tr.rbxcdn.com/180DAY-6c3d95dac7c3d279e20cfa9ef1b27ba5/768/432/Image/Png/noFilter',
  'volleyball-legends': 'https://tr.rbxcdn.com/180DAY-572cf4e9e5cec5dd45074a98fa143ca0/768/432/Image/Png/noFilter',
  'steal-a-brainrot': 'https://tr.rbxcdn.com/180DAY-30a62664e838df470ec079b7fc171637/768/432/Image/Png/noFilter',
  'build-a-boat-for-treasure': 'https://tr.rbxcdn.com/180DAY-1ca8115eb50594d19be488f3d22ac54e/768/432/Image/Png/noFilter',
  'anime-last-stand': 'https://tr.rbxcdn.com/180DAY-b3d29df4d10633c51bd9d2a5b6585bde/768/432/Image/Png/noFilter',
  '99-nights-in-the-forest': 'https://tr.rbxcdn.com/180DAY-c5215eabc21f46723f0084f99bb7622c/768/432/Image/Png/noFilter',
  'plants-vs-brainrots': 'https://tr.rbxcdn.com/180DAY-2ac6fe0e69b8567ab69bc3ca5a2482a0/768/432/Image/Png/noFilter',
  'dead-rails': 'https://tr.rbxcdn.com/180DAY-da525289338642275e4838a07d685e93/768/432/Image/Png/noFilter',
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
  { name: 'Blox Fruits',          slug: 'blox-fruits',          emoji: '🍎', codes: 5 },
  { name: 'Pet Simulator X',      slug: 'pet-simulator-x',      emoji: '🐾', codes: 8 },
  { name: 'Adopt Me',             slug: 'adopt-me',             emoji: '🐣', codes: 0 },
  { name: 'Anime Adventures',     slug: 'anime-adventures',     emoji: '⚔️', codes: 6 },
  { name: 'Brookhaven',           slug: 'brookhaven',           emoji: '🏙️', codes: 0 },
  { name: 'Tower of Hell',        slug: 'tower-of-hell',        emoji: '🗼', codes: 0 },
  { name: 'Murder Mystery 2',     slug: 'murder-mystery-2',     emoji: '🔪', codes: 4 },
  { name: 'Shindo Life',          slug: 'shindo-life',          emoji: '🌀', codes: 12 },
  { name: 'Royale High',          slug: 'royale-high',          emoji: '👑', codes: 1 },
  { name: 'Fruit Battlegrounds',  slug: 'fruit-battlegrounds',  emoji: '💥', codes: 7 },
  { name: 'King Legacy',          slug: 'king-legacy',          emoji: '⚡', codes: 9 },
  { name: 'Encounters',           slug: 'encounters',           emoji: '👾', codes: 1 },
  { name: 'Rivals',               slug: 'rivals',               emoji: '🎯', codes: 5 },
  { name: 'Work at a Pizza Place',slug: 'work-at-a-pizza-place',emoji: '🍕', codes: 0 },
  { name: 'Grow a Garden',        slug: 'grow-a-garden',        emoji: '🌱', codes: 2 },
  { name: 'Blade Ball',           slug: 'blade-ball',           emoji: '⚔️', codes: 8 },
  { name: 'Anime Defenders',      slug: 'anime-defenders',      emoji: '🗡️', codes: 0 },
  { name: 'Toilet Tower Defense', slug: 'toilet-tower-defense', emoji: '🚽', codes: 0 },
  { name: 'Pet Simulator 99',     slug: 'pet-simulator-99',     emoji: '🐹', codes: 0 },
  { name: 'Bee Swarm Simulator', slug: 'bee-swarm-simulator',  emoji: '🐝', codes: 8 },
  { name: 'Anime Vanguards',     slug: 'anime-vanguards',      emoji: '⚔️', codes: 4 },
  { name: 'Arsenal',             slug: 'arsenal',              emoji: '🔫', codes: 5 },
  { name: 'Jailbreak',           slug: 'jailbreak',            emoji: '🚔', codes: 4 },
  { name: 'BedWars',             slug: 'bedwars',              emoji: '🛏️', codes: 0 },
  { name: 'Fisch', slug: 'fisch', emoji: '🐟', codes: 10 },
  { name: 'Dress to Impress', slug: 'dress-to-impress', emoji: '👗', codes: 8 },
  { name: 'Da Hood', slug: 'da-hood', emoji: '🔫', codes: 6 },
  { name: 'Bubble Gum Simulator Infinity', slug: 'bubble-gum-simulator-infinity', emoji: '🫧', codes: 5 },
  { name: 'Blue Lock Rivals', slug: 'blue-lock-rivals', emoji: '⚽', codes: 8 },
  { name: 'Volleyball Legends', slug: 'volleyball-legends', emoji: '🏐', codes: 3 },
  { name: 'Steal a Brainrot', slug: 'steal-a-brainrot', emoji: '🧠', codes: 0 },
  { name: 'Build a Boat for Treasure', slug: 'build-a-boat-for-treasure', emoji: '🚤', codes: 7 },
  { name: 'Anime Last Stand', slug: 'anime-last-stand', emoji: '🗡️', codes: 5 },
  { name: '99 Nights in the Forest', slug: '99-nights-in-the-forest', emoji: '🔦', codes: 2 },
  { name: 'Plants Vs Brainrots', slug: 'plants-vs-brainrots', emoji: '🌻', codes: 5 },
  { name: 'Dead Rails', slug: 'dead-rails', emoji: '🚂', codes: 0 },
];

function gameResultHTML(g) {
  return `
    <a class="search-result-item" href="/codes/${g.slug}.html">
      <img src="${ROBLOX_THUMBS[g.slug] || ('/images/games/' + g.slug + '.svg')}" alt="${g.name}" style="width:38px;height:38px;border-radius:7px;object-fit:cover;flex-shrink:0" onerror="this.onerror=null;this.src='/images/games/'+'${g.slug}'+'.svg'">
      <div>
        <div style="font-size:.88rem;font-weight:600;color:var(--text-primary)">${g.name}</div>
        <div style="font-size:.75rem;color:var(--text-muted)">${g.codes} code${g.codes !== 1 ? 's' : ''} actif${g.codes !== 1 ? 's' : ''}</div>
      </div>
    </a>`;
}

function attachSearch(inputId, resultsId) {
  const input   = document.getElementById(inputId);
  const results = document.getElementById(resultsId);
  if (!input || !results) return;

  input.addEventListener('input', () => {
    const q = input.value.trim().toLowerCase();
    if (q.length < 1) { results.classList.remove('open'); return; }
    const matches = GAMES_INDEX.filter(g => g.name.toLowerCase().includes(q)).slice(0, 6);
    if (!matches.length) {
      results.innerHTML = '<div style="padding:12px 14px;font-size:.85rem;color:var(--text-muted)">Aucun jeu trouvé</div>';
      results.classList.add('open');
      return;
    }
    results.innerHTML = matches.map(gameResultHTML).join('');
    results.classList.add('open');
  });

  document.addEventListener('click', e => {
    if (!input.contains(e.target) && !results.contains(e.target))
      results.classList.remove('open');
  });
}

function initSearch() {
  attachSearch('searchInput', 'searchResults');
  attachSearch('heroSearch', 'heroSearchResults');
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

/* ---- Miniatures Roblox officielles (chargées via proxy /api/thumbnails si dispo) ---- */
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
  'grow-a-garden':         7436755782,
  'blade-ball':            4777817887,
  'anime-defenders':       5836869368,
  'toilet-tower-defense':  4778845442,
  'pet-simulator-99':      3317771874,
  'bee-swarm-simulator':   601130232,
  'anime-vanguards':       5578556129,
  'arsenal':               111958650,
  'jailbreak':             245662005,
  'bedwars':               2619619496,
  'fisch': 5750914919,
  'dress-to-impress': 5203828273,
  'da-hood': 1008451066,
  'bubble-gum-simulator-infinity': 6504986360,
  'blue-lock-rivals': 6325068386,
  'volleyball-legends': 6931042565,
  'steal-a-brainrot': 7709344486,
  'build-a-boat-for-treasure': 210851291,
  'anime-last-stand': 4509896324,
  '99-nights-in-the-forest': 7326934954,
  'plants-vs-brainrots': 8316902627,
  'dead-rails': 7018190066,
};

const _thumbCache = {};

function applyRobloxThumbs() {
  Object.entries(_thumbCache).forEach(([slug, url]) => {
    document.querySelectorAll(`img[data-game="${slug}"]`).forEach(img => {
      if (img.getAttribute('src') !== url) {
        img.style.opacity = '0';
        img.src = url;
        img.onload = () => { img.style.transition = 'opacity .35s'; img.style.opacity = '1'; };
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
  } catch (e) {
    console.log('API miniatures Roblox indisponible — miniatures en dur en place.');
  }
}

/* ---- Vidéos YouTube (3 plus populaires par jeu) ---- */
// Colle ta clé API YouTube Data v3 ici (gratuite, restreinte au domaine zoneblox.com) :
const YOUTUBE_API_KEY = 'AIzaSyCvalvjmUJryGAP_Xg_NEjhrwk_7GAbD3A';

function renderYouTube(grid, items) {
  grid.innerHTML = items.map(v => `
    <div class="video-card">
      <div class="video-embed">
        <iframe src="https://www.youtube.com/embed/${v.id}" title="${(v.title || '').replace(/"/g, '&quot;')}" allowfullscreen loading="lazy"></iframe>
      </div>
      <div class="video-label">🎬 ${v.title || ''}</div>
    </div>`).join('');
}

function initYouTubeVideos() {
  const grid = document.querySelector('#tab-videos .videos-grid');
  if (!grid) return;
  if (!YOUTUBE_API_KEY) return;

  const m = location.pathname.match(/\/codes\/([a-z0-9-]+)\.html/i);
  if (!m) return;
  const slug = m[1];
  const game = (GAMES_INDEX.find(g => g.slug === slug) || {}).name || slug.replace(/-/g, ' ');
  const query = game + ' Roblox';
  const cacheKey = 'yt_' + slug;

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
      if (!items.length) return;
      try { localStorage.setItem(cacheKey, JSON.stringify({ t: Date.now(), items })); } catch (e) {}
      renderYouTube(grid, items);
    })
    .catch(() => {});
}

/* ---- Init ---- */
document.addEventListener('DOMContentLoaded', () => {
  initMobileNav();
  initSearch();
  initNewsletter();
  highlightNav();
  loadRobloxThumbnails();
  initYouTubeVideos();
});
