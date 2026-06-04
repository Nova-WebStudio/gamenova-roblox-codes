/* ============================================================
   Zoneblox – Main JavaScript (FR)
   ============================================================ */

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
      <span style="font-size:1.4rem">${g.emoji}</span>
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
  'fruit-battlegrounds':   10449761463,
  'anime-adventures':      7974552544,
  'rivals':                17017769292,
  'brookhaven':            4924922222,
  'royale-high':           735030788,
  'encounters':            16768148699,
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

/* ---- Init ---- */
document.addEventListener('DOMContentLoaded', () => {
  initMobileNav();
  initSearch();
  initHeroSearch();
  initNewsletter();
  highlightNav();
  loadRobloxThumbnails();
});
