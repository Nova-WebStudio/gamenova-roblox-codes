/* ============================================================
   GameNova – Main JavaScript
   ============================================================ */

/* ---- Language system ---- */
const TRANSLATIONS = {
  en: {
    'nav.home': 'Home', 'nav.codes': 'All Codes', 'nav.tips': 'Tips',
    'nav.about': 'About', 'search.placeholder': 'Search a game…',
    'hero.badge': 'Updated Daily', 'hero.subtitle': 'The #1 source for Roblox codes, tips & videos — updated every day.',
    'section.featured': '🔥 Featured Games', 'section.recent': '⭐ Recently Updated',
    'section.allgames': '🎮 All Games', 'viewall': 'View all →',
    'code.active': 'Active Codes', 'code.expired': 'Expired Codes',
    'code.updated': 'Updated', 'copy': 'Copy', 'copied': 'Copied!',
    'redeem.title': 'How to Redeem Codes',
    'tips.title': '💡 Tips & Tricks', 'videos.title': '🎬 Videos',
    'newsletter.title': '📧 Get Notified', 'newsletter.desc': 'New codes straight to your inbox.',
    'newsletter.placeholder': 'your@email.com', 'newsletter.btn': 'Subscribe',
    'affiliate.title': 'Buy Robux & Gift Cards', 'affiliate.desc': 'Support the site — buy official Robux or Roblox gift cards.',
    'affiliate.btn': 'Shop Now →', 'footer.desc': 'Your #1 daily source for Roblox codes, tips, and game guides.',
    'stat.games': 'Games Covered', 'stat.codes': 'Active Codes', 'stat.updated': 'Daily Updates',
  },
  fr: {
    'nav.home': 'Accueil', 'nav.codes': 'Tous les Codes', 'nav.tips': 'Astuces',
    'nav.about': 'À Propos', 'search.placeholder': 'Rechercher un jeu…',
    'hero.badge': 'Mis à jour chaque jour', 'hero.subtitle': 'La référence #1 des codes Roblox, astuces & vidéos — mise à jour quotidienne.',
    'section.featured': '🔥 Jeux Populaires', 'section.recent': '⭐ Récemment Mis à Jour',
    'section.allgames': '🎮 Tous les Jeux', 'viewall': 'Voir tout →',
    'code.active': 'Codes Actifs', 'code.expired': 'Codes Expirés',
    'code.updated': 'Mis à jour', 'copy': 'Copier', 'copied': 'Copié !',
    'redeem.title': 'Comment utiliser les codes',
    'tips.title': '💡 Astuces & Conseils', 'videos.title': '🎬 Vidéos',
    'newsletter.title': '📧 Être notifié', 'newsletter.desc': 'Nouveaux codes directement dans votre boîte mail.',
    'newsletter.placeholder': 'votre@email.com', 'newsletter.btn': 'S\'abonner',
    'affiliate.title': 'Acheter des Robux & Gift Cards', 'affiliate.desc': 'Soutenez le site — achetez des Robux officiels ou des cartes cadeaux Roblox.',
    'affiliate.btn': 'Acheter →', 'footer.desc': 'Votre source #1 quotidienne de codes Roblox, astuces et guides de jeux.',
    'stat.games': 'Jeux Couverts', 'stat.codes': 'Codes Actifs', 'stat.updated': 'Mises à Jour / Jour',
  }
};

let currentLang = localStorage.getItem('lang') || 'en';

function t(key) { return TRANSLATIONS[currentLang][key] || key; }

function applyLang() {
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (el.tagName === 'INPUT') { el.placeholder = t(key); }
    else { el.textContent = t(key); }
  });
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.lang === currentLang);
  });
  document.documentElement.lang = currentLang;
}

function switchLang(lang) {
  currentLang = lang;
  localStorage.setItem('lang', lang);
  applyLang();
}

/* ---- Copy code ---- */
function copyCode(btn, code) {
  navigator.clipboard.writeText(code).then(() => {
    const orig = btn.textContent;
    btn.textContent = t('copied');
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

/* ---- Search ---- */
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
  { name: 'Blox Fruits 2',       slug: 'blox-fruits-2',        emoji: '🍊', codes: 3 },
  { name: 'King Legacy',         slug: 'king-legacy',          emoji: '⚡', codes: 9 },
  { name: 'Encounters',          slug: 'encounters',           emoji: '👾', codes: 4 },
  { name: 'Rivals',              slug: 'rivals',               emoji: '🎯', codes: 5 },
];

function initSearch() {
  const input   = document.getElementById('searchInput');
  const results = document.getElementById('searchResults');
  if (!input || !results) return;

  input.addEventListener('input', () => {
    const q = input.value.trim().toLowerCase();
    if (q.length < 2) { results.classList.remove('open'); return; }

    const matches = GAMES_INDEX.filter(g => g.name.toLowerCase().includes(q)).slice(0, 6);
    if (!matches.length) { results.classList.remove('open'); return; }

    results.innerHTML = matches.map(g => `
      <a class="search-result-item" href="/codes/${g.slug}.html">
        <span style="font-size:1.4rem">${g.emoji}</span>
        <div>
          <div style="font-size:.88rem;font-weight:600;color:var(--text-primary)">${g.name}</div>
          <div style="font-size:.75rem;color:var(--text-muted)">${g.codes} active code${g.codes !== 1 ? 's' : ''}</div>
        </div>
      </a>`).join('');
    results.classList.add('open');
  });

  document.addEventListener('click', e => {
    if (!input.contains(e.target) && !results.contains(e.target))
      results.classList.remove('open');
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
      btn.textContent = '✓ Done!';
      btn.disabled = true;
      inp.value = '';
      setTimeout(() => { btn.textContent = t('newsletter.btn'); btn.disabled = false; }, 3000);
    });
  });
}

/* ---- Sticky ad hide on scroll ---- */
function initStickyAd() {
  const ad = document.querySelector('.ad-sticky-bottom');
  if (!ad) return;
  let lastY = 0;
  window.addEventListener('scroll', () => {
    const y = window.scrollY;
    ad.style.transform = y > lastY && y > 200 ? 'translateY(0)' : 'translateY(0)';
    lastY = y;
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

// Cache slug → URL (évite des appels API répétés au filtrage)
const _thumbCache = {};

// Applique les URLs cachées à toutes les img[data-game] présentes dans le DOM
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
window.applyRobloxThumbs = applyRobloxThumbs; // accessible depuis codes/index.html

async function loadRobloxThumbnails() {
  // Si déjà chargé, juste appliquer le cache
  if (Object.keys(_thumbCache).length > 0) { applyRobloxThumbs(); return; }

  const idToSlug = Object.fromEntries(
    Object.entries(ROBLOX_UNIVERSE_IDS).map(([s, id]) => [id, s])
  );
  const ids = Object.values(ROBLOX_UNIVERSE_IDS).join(',');

  try {
    // Appel via notre proxy Vercel /api/thumbnails (évite le CORS de Roblox)
    const res = await fetch('/api/thumbnails', { headers: { 'Accept': 'application/json' } });
    if (!res.ok) return;
    const json = await res.json();

    // Format : item.universeId + item.thumbnails[0].imageUrl
    json.data.forEach(item => {
      const slug = idToSlug[item.universeId];
      const url  = item.thumbnails?.[0]?.imageUrl;
      if (slug && url) _thumbCache[slug] = url;
    });

    applyRobloxThumbs();
  } catch(e) {
    console.log('Roblox thumbnails API unavailable — SVG fallbacks in use.');
  }
}

/* ---- Init ---- */
document.addEventListener('DOMContentLoaded', () => {
  applyLang();
  initMobileNav();
  initSearch();
  initNewsletter();
  initStickyAd();
  highlightNav();

  // Lang buttons
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', () => switchLang(btn.dataset.lang));
  });

  // Charge les vraies images Roblox après le rendu
  loadRobloxThumbnails();
});
