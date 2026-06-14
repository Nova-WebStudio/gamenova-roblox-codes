/* ════════════════════════════════════════════════════════════════════════
   Zoneblox · Générateur d'avatar Roblox par budget
   Outil 100 % informatif : compose le meilleur avatar possible pour un budget
   Robux donné, à partir d'un catalogue mis en cache (data/items.json).
   Aucun achat, aucune connexion Roblox. On renseigne, on lie au catalogue.
   ════════════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  // ── Config ────────────────────────────────────────────────────────────────
  const SLOTS = [
    { key: 'hat',    label: 'Chapeau',     weight: 2, essential: false },
    { key: 'hair',   label: 'Cheveux',     weight: 5, essential: true  },
    { key: 'face',   label: 'Visage',      weight: 3, essential: false },
    { key: 'neck',   label: 'Cou',         weight: 1, essential: false },
    { key: 'top',    label: 'Haut',        weight: 4, essential: true  },
    { key: 'back',   label: 'Dos / Ailes', weight: 2, essential: false },
    { key: 'front',  label: 'Devant',      weight: 1, essential: false },
    { key: 'waist',  label: 'Taille',      weight: 1, essential: false },
    { key: 'bottom', label: 'Bas',         weight: 4, essential: true  },
  ];
  const SLOT_LABEL = Object.fromEntries(SLOTS.map((s) => [s.key, s.label]));

  // Le mannequin affiche les objets en deux colonnes qui encadrent l'avatar,
  // pour éviter tout chevauchement (tête / chapeau / masque se superposaient).
  const COL_LEFT  = ['hat', 'hair', 'face', 'neck'];
  const COL_RIGHT = ['top', 'back', 'front', 'waist', 'bottom'];

  const STYLE_LABEL = {
    anime: 'Anime', ninja: 'Ninja', cyberpunk: 'Cyberpunk', demon: 'Démon',
    futuriste: 'Futuriste', gothique: 'Gothique', ange: 'Ange',
    militaire: 'Militaire', mage: 'Mage', pirate: 'Pirate',
  };

  // ── État ─────────────────────────────────────────────────────────────────
  let DATA = { items: [], styles: [] };
  let seed = Math.floor(Math.random() * 1e9);
  let current = {};        // slot -> item (composition affichée)
  let locked = {};         // slot -> item (objets verrouillés)
  let lastBudget = 500; // budget courant (pour recalcul du résumé au verrouillage)

  // ── Utilitaires ────────────────────────────────────────────────────────────
  function rng(s) {
    return function () {
      s |= 0; s = (s + 0x6D2B79F5) | 0;
      let t = Math.imul(s ^ (s >>> 15), 1 | s);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  const fmt = (n) => n.toLocaleString('fr-FR');
  const catalogUrl = (id) => `https://www.roblox.com/catalog/${id}/`;
  function thumb(it) {
    return it.thumbUrl
      || `https://www.roblox.com/asset-thumbnail/image?assetId=${it.id}&width=150&height=150&format=png`;
  }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, (c) => (
      { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  }

  function scoreOf(it, colors) {
    let score = Math.log10((it.favorites || 0) + 10);
    if (colors && colors.length && it.colors.some((c) => colors.includes(c))) score += 2.5;
    return score;
  }

  function candidates(slot, { style, gender, colors }) {
    let pool = DATA.items.filter((it) => it.slot === slot && it.styles.includes(style));
    if (gender && gender !== 'tous') {
      pool = pool.filter((it) => it.gender === 'unisexe' || it.gender === gender);
    }
    return pool.map((it) => ({ it, score: scoreOf(it, colors) }))
      .sort((a, b) => b.score - a.score);
  }

  // ── Composition sous contrainte de budget (avec slots verrouillés) ─────────
  function compose(opts, lockedPicks) {
    const rand = rng(seed);
    const budget = opts.budget;
    const picks = {};
    let spent = 0;

    // 1) place d'abord les objets verrouillés (toujours conservés)
    for (const s of SLOTS) {
      const li = lockedPicks[s.key];
      if (li) { picks[s.key] = li; spent += li.price; }
    }

    // candidats pour les slots non verrouillés
    const cand = {};
    for (const s of SLOTS) {
      if (picks[s.key]) continue;
      const list = candidates(s.key, opts);
      const top = list.slice(0, 14);
      for (let i = top.length - 1; i > 0; i--) {
        const j = Math.floor(rand() * (i + 1));
        [top[i], top[j]] = [top[j], top[i]];
      }
      cand[s.key] = top.concat(list.slice(14));
    }

    // 2) garantir les slots essentiels (non verrouillés) au moins cher
    for (const s of SLOTS.filter((x) => x.essential && !picks[x.key])) {
      const cheapest = [...(cand[s.key] || [])].sort((a, b) => a.it.price - b.it.price)[0];
      if (cheapest && spent + cheapest.it.price <= budget) {
        picks[s.key] = cheapest.it; spent += cheapest.it.price;
      }
    }

    // 3) améliorer / compléter les slots non verrouillés avec le budget restant
    for (const s of SLOTS) {
      if (lockedPicks[s.key]) continue;
      const remaining = budget - spent;
      const cur = picks[s.key];
      let best = null;
      for (const c of (cand[s.key] || [])) {
        const delta = cur ? c.it.price - cur.price : c.it.price;
        if (delta <= remaining && c.it.id !== (cur && cur.id)) {
          if (cur && c.score <= scoreOf(cur, opts.colors)) continue;
          best = c.it; break;
        }
      }
      if (best) { spent += (cur ? best.price - cur.price : best.price); picks[s.key] = best; }
    }

    const list = SLOTS.map((s) => picks[s.key]).filter(Boolean);
    return { picks, list, spent, remaining: budget - spent };
  }

  // ── Rendu : mannequin + cartes + résumé ────────────────────────────────────
  function render(result, budget) {
    renderMannequin(result.picks);
    renderCards(result.picks);
    renderSummary(result, budget);
  }

  function equipChip(slot, picks) {
    const it = picks[slot]; if (!it) return '';
    const isLock = !!locked[slot];
    return `<a class="av-equip${isLock ? ' is-locked' : ''}" href="${catalogUrl(it.id)}"
              target="_blank" rel="noopener nofollow"
              title="${esc(SLOT_LABEL[slot])} · ${esc(it.name)} — voir sur Roblox">
              <img loading="lazy" src="${thumb(it)}" alt="${esc(it.name)}" onerror="this.style.opacity=.2">
              <span class="av-equip-tag">${esc(SLOT_LABEL[slot])}</span>
              ${isLock ? '<span class="av-equip-lock">🔒</span>' : ''}
            </a>`;
  }
  function renderMannequin(picks) {
    const el = document.getElementById('avatarMannequin');
    if (!el) return;
    const figure = `
      <svg class="av-figure" viewBox="0 0 120 200" aria-hidden="true">
        <rect x="42" y="8"  width="36" height="32" rx="5" class="av-skin"/>
        <rect x="40" y="46" width="40" height="46" rx="4" class="av-body"/>
        <rect x="22" y="46" width="15" height="44" rx="4" class="av-skin"/>
        <rect x="83" y="46" width="15" height="44" rx="4" class="av-skin"/>
        <rect x="44" y="96" width="15" height="48" rx="4" class="av-body2"/>
        <rect x="61" y="96" width="15" height="48" rx="4" class="av-body2"/>
      </svg>`;
    const left = COL_LEFT.map((s) => equipChip(s, picks)).join('');
    const right = COL_RIGHT.map((s) => equipChip(s, picks)).join('');
    const hasAny = left || right;
    el.innerHTML = `<div class="av-stage">
        <div class="av-col">${left}</div>${figure}<div class="av-col">${right}</div>
      </div>${hasAny ? '' : '<p class="av-empty" style="padding:14px">Aucun objet à afficher.</p>'}`;
  }

  function renderCards(picks) {
    const grid = document.getElementById('avatarResult');
    if (!grid) return;
    const list = SLOTS.map((s) => ({ slot: s.key, it: picks[s.key] })).filter((x) => x.it);
    if (!list.length) {
      grid.innerHTML = `<p class="av-empty">Aucun objet trouvé pour ce style dans cette gamme de budget.
        Augmente le budget ou change de style.</p>`;
      return;
    }
    grid.innerHTML = list.map(({ slot, it }) => {
      const isLock = !!locked[slot];
      return `<div class="av-card${isLock ? ' is-locked' : ''}">
        <button class="av-lock" data-slot="${slot}" type="button"
                aria-label="${isLock ? 'Déverrouiller' : 'Verrouiller'} ${esc(SLOT_LABEL[slot])}"
                title="${isLock ? 'Déverrouiller' : 'Verrouiller cet objet (ne sera pas relancé)'}">${isLock ? '🔒' : '🔓'}</button>
        <a class="av-card-link" href="${catalogUrl(it.id)}" target="_blank" rel="noopener nofollow"
           title="Voir « ${esc(it.name)} » sur le catalogue Roblox">
          <div class="av-card-img"><img loading="lazy" src="${thumb(it)}" alt="${esc(it.name)}" onerror="this.style.opacity=.25"></div>
          <div class="av-card-body">
            <span class="av-slot">${SLOT_LABEL[slot]}</span>
            <span class="av-name">${esc(it.name)}</span>
            <span class="av-price">${fmt(it.price)} <span class="av-rbx">Robux</span></span>
          </div>
        </a>
      </div>`;
    }).join('');
    grid.querySelectorAll('.av-lock').forEach((b) =>
      b.addEventListener('click', () => toggleLock(b.dataset.slot)));
  }

  function renderSummary(result, budget) {
    const summary = document.getElementById('avatarSummary');
    if (!summary) return;
    const over = result.remaining < 0;
    const usedPct = budget > 0 ? Math.min(100, Math.round((result.spent / budget) * 100)) : 0;
    const nLock = Object.keys(locked).length;
    summary.innerHTML = `
      <div class="av-sum-row"><span>Coût total</span><strong>${fmt(result.spent)} Robux</strong></div>
      <div class="av-sum-row"><span>Budget</span><strong>${fmt(budget)} Robux</strong></div>
      <div class="av-sum-row av-sum-rest"><span>${over ? 'Dépassement' : 'Reste'}</span>
        <strong style="${over ? 'color:#ff6b6b;text-shadow:none' : ''}">${fmt(Math.abs(result.remaining))} Robux</strong></div>
      <div class="av-bar"><span style="width:${usedPct}%"></span></div>
      <div class="av-sum-meta">${result.list.length} objet(s)${nLock ? ` · ${nLock} verrouillé(s) 🔒` : ''} · ${usedPct}% du budget</div>`;
  }

  // ── Verrouillage ───────────────────────────────────────────────────────────
  function toggleLock(slot) {
    if (locked[slot]) delete locked[slot];
    else if (current[slot]) locked[slot] = current[slot];
    // pas de reroll : on rafraîchit juste l'affichage du verrou
    renderMannequin(current);
    renderCards(current);
    const summary = document.getElementById('avatarSummary');
    if (summary) renderSummary(computeResult(lastBudget), lastBudget);
    persist();
  }

  function computeResult(budget) {
    const list = SLOTS.map((s) => current[s.key]).filter(Boolean);
    const spent = list.reduce((a, it) => a + it.price, 0);
    return { picks: current, list, spent, remaining: budget - spent };
  }

  // ── Lecture des entrées ────────────────────────────────────────────────────
  function readOpts() {
    const budget = Math.max(0, parseInt(document.getElementById('avBudget').value, 10) || 0);
    const style = document.getElementById('avStyle').value;
    const gender = document.getElementById('avGender').value;
    const colors = [...document.querySelectorAll('.av-color.is-on')].map((b) => b.dataset.color);
    return { budget, style, gender, colors };
  }

  // ── Partage / persistance ──────────────────────────────────────────────────
  function lockedIds() {
    const o = {};
    for (const k of Object.keys(locked)) o[k] = locked[k].id;
    return o;
  }
  function persist() {
    const opts = readOpts();
    const p = new URLSearchParams();
    p.set('b', opts.budget); p.set('s', opts.style); p.set('g', opts.gender);
    if (opts.colors.length) p.set('c', opts.colors.join(','));
    const lk = lockedIds(); if (Object.keys(lk).length) p.set('l', JSON.stringify(lk));
    p.set('seed', seed);
    history.replaceState(null, '', '#' + p.toString());
    try { localStorage.setItem('zb_avatar', JSON.stringify({ ...opts, seed, locked: lk })); } catch (e) {}
  }
  function readState() {
    let st = null;
    if (location.hash) {
      const p = new URLSearchParams(location.hash.slice(1));
      if (p.has('b')) st = {
        budget: parseInt(p.get('b'), 10) || 0, style: p.get('s') || 'anime',
        gender: p.get('g') || 'tous', colors: (p.get('c') || '').split(',').filter(Boolean),
        seed: parseInt(p.get('seed'), 10) || seed,
        locked: p.get('l') ? JSON.parse(p.get('l')) : {},
      };
    }
    if (!st) { try { st = JSON.parse(localStorage.getItem('zb_avatar')); } catch (e) {} }
    return st;
  }

  // ── Cycle principal ────────────────────────────────────────────────────────
  function run(mode) {
    if (!DATA.items.length) return;
    const opts = readOpts();
    lastBudget = opts.budget;
    if (mode === 'full') { locked = {}; seed = Math.floor(Math.random() * 1e9); }
    else if (mode === 'reroll') { seed = Math.floor(Math.random() * 1e9); }
    const result = compose(opts, locked);
    current = result.picks;
    render(result, opts.budget);
    persist();
    if (window.gtag) gtag('event', 'avatar_' + (mode || 'init'), { style: opts.style, budget: opts.budget });
  }

  function applyState(st) {
    if (!st) return;
    if (st.budget) document.getElementById('avBudget').value = st.budget;
    if (st.style) document.getElementById('avStyle').value = st.style;
    if (st.gender) document.getElementById('avGender').value = st.gender;
    document.querySelectorAll('.av-color').forEach((b) =>
      b.classList.toggle('is-on', (st.colors || []).includes(b.dataset.color)));
    if (st.seed) seed = st.seed;
    // reconstruit les objets verrouillés à partir des ids mémorisés
    locked = {};
    const lk = st.locked || {};
    for (const slot of Object.keys(lk)) {
      const it = DATA.items.find((x) => x.id === lk[slot]);
      if (it) locked[slot] = it;
    }
  }

  // ── Init ───────────────────────────────────────────────────────────────────
  function flash(msg) {
    const el = document.getElementById('avFlash'); if (!el) return;
    el.textContent = msg; el.classList.add('is-on');
    setTimeout(() => el.classList.remove('is-on'), 1800);
  }
  function bind() {
    document.getElementById('avForm')?.addEventListener('submit', (e) => { e.preventDefault(); run('full'); });
    document.getElementById('avGenerate')?.addEventListener('click', () => run('full'));
    document.getElementById('avReroll')?.addEventListener('click', () => run('reroll'));
    document.querySelectorAll('.av-color').forEach((b) =>
      b.addEventListener('click', () => b.classList.toggle('is-on')));
    document.getElementById('avShare')?.addEventListener('click', async () => {
      try { await navigator.clipboard.writeText(location.href); flash('Lien copié !'); }
      catch (e) { flash('Copie impossible — copie l\'URL manuellement.'); }
    });
  }
  function fillStyles() {
    const sel = document.getElementById('avStyle'); if (!sel) return;
    const styles = DATA.styles.length ? DATA.styles : ['anime', 'ninja', 'cyberpunk', 'demon'];
    sel.innerHTML = styles.map((s) => `<option value="${s}">${STYLE_LABEL[s] || s}</option>`).join('');
  }
  async function init() {
    bind();
    try {
      const res = await fetch('data/items.json', { cache: 'no-cache' });
      DATA = await res.json();
    } catch (e) {
      const r = document.getElementById('avatarResult');
      if (r) r.innerHTML = '<p class="av-empty">Catalogue indisponible pour le moment. Réessaie plus tard.</p>';
      return;
    }
    fillStyles();
    const st = readState();
    applyState(st);
    run('restore');
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
