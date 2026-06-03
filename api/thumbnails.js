// Vercel Serverless Function — thumbnails officielles Roblox
// URLs vérifiées directement sur chaque page de jeu roblox.com

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Cache-Control', 's-maxage=86400, stale-while-revalidate=604800');

  // ✅ URLs 768×432 / 500×280 extraites directement depuis les pages Roblox
  const CONFIRMED = {
    'blox-fruits':           'https://tr.rbxcdn.com/180DAY-e1ce51abae5188805c3fee78ec7f4d08/768/432/Image/Webp/noFilter',
    'pet-simulator-x':       'https://tr.rbxcdn.com/180DAY-a7bb14d2b3dbf586e67ba2ac7a0c3dc7/500/280/Image/Jpeg/noFilter',
    'adopt-me':              'https://tr.rbxcdn.com/180DAY-ef30533fcd5e71af2468030ffa6c176a/500/280/Image/Jpeg/noFilter',
    'murder-mystery-2':      'https://tr.rbxcdn.com/180DAY-5ba706807447783862364dfef7a465ff/500/280/Image/Jpeg/noFilter',
    'royale-high':           'https://tr.rbxcdn.com/180DAY-1c63d3971f06391b08a95400cdf2bb78/500/280/Image/Jpeg/noFilter',
    'brookhaven':            'https://tr.rbxcdn.com/180DAY-5e77d217cbda7ba5941840cfa3ab8c36/768/432/Image/Webp/noFilter',
    'tower-of-hell':         'https://tr.rbxcdn.com/180DAY-20a372111085c33de1e64004e4dca1d8/768/432/Image/Webp/noFilter',
    'work-at-a-pizza-place': 'https://tr.rbxcdn.com/180DAY-3504f0abedb16721aec2f8fcc0da4e2e/768/432/Image/Webp/noFilter',
  };

  // Pour les jeux restants, tentative via l'API Roblox thumbnails
  // (retourne des screenshots du jeu — images réelles mais pas le banner principal)
  const UNIVERSE_IDS_REMAINING = {
    'shindo-life':         6017744795,
    'king-legacy':         6096648965,
    'fruit-battlegrounds': 10449761463,
    'anime-adventures':    7974552544,
    'rivals':              17017769292,
    'encounters':          16768148699,
  };

  const result = { ...CONFIRMED };

  try {
    const ids = Object.values(UNIVERSE_IDS_REMAINING).join(',');
    const apiRes = await fetch(
      `https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=${ids}&countPerUniverse=1&size=768x432&format=Png&isCircular=false`,
      { headers: { 'Accept': 'application/json', 'User-Agent': 'Mozilla/5.0' } }
    );

    if (apiRes.ok) {
      const json = await apiRes.json();
      const idToSlug = Object.fromEntries(
        Object.entries(UNIVERSE_IDS_REMAINING).map(([s, id]) => [id, s])
      );
      json.data?.forEach(item => {
        const slug = idToSlug[item.universeId];
        const url  = item.thumbnails?.[0]?.imageUrl;
        if (slug && url) result[slug] = url;
      });
    }
  } catch (e) {
    // Fallback silencieux — les SVG restent pour ces jeux
  }

  res.status(200).json(result);
}
