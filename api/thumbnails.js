// Vercel Serverless Function — proxy vers l'API Roblox Thumbnails
// Évite les problèmes CORS en appelant Roblox depuis le serveur

export default async function handler(req, res) {
  // CORS headers pour que le navigateur puisse appeler /api/thumbnails
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Cache-Control', 's-maxage=3600, stale-while-revalidate=86400');

  const UNIVERSE_IDS = [
    2753915549,   // Blox Fruits
    6284583030,   // Pet Simulator X
    920587237,    // Adopt Me
    6017744795,   // Shindo Life
    6096648965,   // King Legacy
    142823291,    // Murder Mystery 2
    10449761463,  // Fruit Battlegrounds
    7974552544,   // Anime Adventures
    17017769292,  // Rivals
    4924922222,   // Brookhaven
    735030788,    // Royale High
    16768148699,  // Encounters
    1962086868,   // Tower of Hell
    192800,       // Work at a Pizza Place
  ];

  const ids = UNIVERSE_IDS.join(',');

  try {
    const robloxRes = await fetch(
      `https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=${ids}&countPerUniverse=1&size=768x432&format=Png&isCircular=false`,
      { headers: { 'Accept': 'application/json', 'User-Agent': 'GameNova/1.0' } }
    );

    if (!robloxRes.ok) {
      return res.status(502).json({ error: 'Roblox API error', status: robloxRes.status });
    }

    const data = await robloxRes.json();
    res.status(200).json(data);

  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch Roblox thumbnails', message: err.message });
  }
}
