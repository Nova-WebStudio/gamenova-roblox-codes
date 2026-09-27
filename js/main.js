/* ============================================================
   Zoneblox – Main JavaScript (FR)
   ============================================================ */

const ROBLOX_THUMBS = {
  'steal-from-the-rich': '/images/games/steal-from-the-rich.svg',
  'ride-a-pet': '/images/games/ride-a-pet.svg',
  '1-loot-to-forge': '/images/games/1-loot-to-forge.svg',
  'slayers-2': '/images/games/slayers-2.svg',
  'illegal-soccer': '/images/games/illegal-soccer.svg',
  'search-for-the-needle': '/images/games/search-for-the-needle.svg',
  'dungeon-quest-reborn': '/images/games/dungeon-quest-reborn.svg','anime-origins': 'https://tr.rbxcdn.com/180DAY-08bf47e71d016cba2881cf9d67114527/768/432/Image/Webp/noFilter',
  'grow-a-chicken-fighter': 'https://tr.rbxcdn.com/180DAY-8403e52cfc77a0fb4df895e64943deab/768/432/Image/Webp/noFilter',
  'dig-and-clean': 'https://tr.rbxcdn.com/180DAY-1912ba1aee413f812eeb5cc59ba88416/768/432/Image/Webp/noFilter',
  'fish-an-anime-rng': 'https://tr.rbxcdn.com/180DAY-ec9205660a2677cf225c249a16440ae6/768/432/Image/Webp/noFilter',
  'anime-stars': 'https://tr.rbxcdn.com/180DAY-a8f70d05eb255217c5a971cfdf9ec0cc/768/432/Image/Webp/noFilter',
  'anime-expeditions': 'https://tr.rbxcdn.com/180DAY-dfa52552ffbbe27fd044e99ce02374bd/768/432/Image/Webp/noFilter',
  'spin-a-soccer-card': 'https://tr.rbxcdn.com/180DAY-a0f9478a80687a2fb6285996ba9ee941/768/432/Image/Webp/noFilter',
  'merge-a-nuke': 'https://tr.rbxcdn.com/180DAY-d982f25e675f798daa6b9c444e6b4503/768/432/Image/Webp/noFilter',
  'vv-ultimatum': 'https://tr.rbxcdn.com/180DAY-a4811bdac3671e6bbad994bfd27a4ccc/768/432/Image/Webp/noFilter',
  'fifa-super-soccer': 'https://tr.rbxcdn.com/180DAY-3afe0db053cec46ec55afc65bad20685/768/432/Image/Webp/noFilter',
  'hypershot': 'https://tr.rbxcdn.com/180DAY-ce76a2089e0f151c197c100c98804acf/768/432/Image/Webp/noFilter',
  'blockspin': 'https://tr.rbxcdn.com/180DAY-faec41dafa29c7f849b7cc61a6dc6759/768/432/Image/Webp/noFilter',
  'run-a-restaurant': 'https://tr.rbxcdn.com/180DAY-fc866f9e65452bc24084fff8a650876f/768/432/Image/Webp/noFilter',
  'squid-game-x': 'https://tr.rbxcdn.com/180DAY-2264689de7f046b3c3df5e135abd5ffa/768/432/Image/Webp/noFilter',
  'catch-a-monster': 'https://tr.rbxcdn.com/180DAY-c780f871c7d5d8fe666d32bdca058804/768/432/Image/Webp/noFilter',
  'brainrot-evolution': 'https://tr.rbxcdn.com/180DAY-fc4ce9bf5f0886c17c472d7e9b291b2d/768/432/Image/Webp/noFilter',
  '100-days-at-sea': 'https://tr.rbxcdn.com/180DAY-59561ce01bc1ebaffa01b7739feca185/768/432/Image/Webp/noFilter',
  'a-dusty-trip': 'https://tr.rbxcdn.com/180DAY-3b3cb9373ed64fd6b4a4a825c9f3244b/768/432/Image/Webp/noFilter',
  'war-tycoon': 'https://tr.rbxcdn.com/180DAY-a41a3effdfee1e6817c271de2ff57349/768/432/Image/Webp/noFilter',
  'iron-soul-dungeon': 'https://tr.rbxcdn.com/180DAY-6624e54164ae1e6a970c6ba71fb6776a/768/432/Image/Webp/noFilter',
  'blox-monsters': 'https://tr.rbxcdn.com/180DAY-6ac6108ce5f7f6cb26ac0ebd3c4c7032/768/432/Image/Webp/noFilter',
  'car-crushers-2': 'https://tr.rbxcdn.com/180DAY-53a6829816ea76371d67a8a5c451c6ac/768/432/Image/Webp/noFilter',
  'steal-a-fish': 'https://tr.rbxcdn.com/180DAY-ed927450771fe3f6c356b5aacbb5efeb/768/432/Image/Webp/noFilter',
  'steal-an-egg': 'https://tr.rbxcdn.com/180DAY-875b2a6dc156ce6dd64eb637e73238ce/768/432/Image/Webp/noFilter',
  'knockout': 'https://tr.rbxcdn.com/180DAY-152a83c0bc4a22f667e0a4d5f7e51c98/768/432/Image/Webp/noFilter',
  'my-gym': 'https://tr.rbxcdn.com/180DAY-265e5dc28c6962bc622cf1fa0f2d632c/768/432/Image/Webp/noFilter',
  'untitled-tag-game': 'https://tr.rbxcdn.com/180DAY-b155b23d5ee6e19361f330cd8cc34aa6/768/432/Image/Webp/noFilter',
  'bloxstrike': 'https://tr.rbxcdn.com/180DAY-5de034057184c82666b530ef54e2898e/768/432/Image/Webp/noFilter',
  'twenty-one': 'https://tr.rbxcdn.com/180DAY-20b1ac2eb8792c3d1d2b51a02ce6582d/768/432/Image/Webp/noFilter',
  'anime-astral-simulator': 'https://tr.rbxcdn.com/180DAY-f77df8e34b5d302dbf226e6d410aad72/768/432/Image/Webp/noFilter',
  'anime-battle-rng': 'https://tr.rbxcdn.com/180DAY-b5f0338da21f70ba8ef711f683bab91c/768/432/Image/Webp/noFilter',
  'anime-fighters': 'https://tr.rbxcdn.com/180DAY-18d9514866cd1a74d6d101afe93dcbf3/768/432/Image/Webp/noFilter',
  'anime-fighting-simulator': 'https://tr.rbxcdn.com/180DAY-cdc3b2796a06e36e3e1b881d39d5f17d/768/432/Image/Webp/noFilter',
  'anime-reversal': 'https://tr.rbxcdn.com/180DAY-3dd41927149f59a9fe0b6b04dd84e3a5/768/432/Image/Webp/noFilter',
  'locked': 'https://tr.rbxcdn.com/180DAY-d25adedff694e3710158bf33115397bf/768/432/Image/Webp/noFilter',
  'defend-ur-base-with-anime': 'https://tr.rbxcdn.com/180DAY-9257c2e2a16497b2b8cc7fc8e6d3ce67/768/432/Image/Webp/noFilter',
  'anime-rng': 'https://tr.rbxcdn.com/180DAY-2e902476693aa77ed9910207c0e6e16f/768/432/Image/Webp/noFilter',
  'ugc-limited': 'https://tr.rbxcdn.com/180DAY-4c03c829dd96b8bd973dab28a0dd7f8a/768/432/Image/Webp/noFilter',
  'jujutsu-shenanigans': 'https://tr.rbxcdn.com/180DAY-decec85a41b80e4ac0beca8bc2952a7f/768/432/Image/Webp/noFilter',
  'kick-a-lucky-block': 'https://tr.rbxcdn.com/180DAY-829dd7deb9a2a04609c27a366096f07d/768/432/Image/Webp/noFilter',
  'dandys-world': 'https://tr.rbxcdn.com/180DAY-511e5c6e680e60d7b068cdff1b94a4d8/768/432/Image/Webp/noFilter',
  'slime-rng': 'https://tr.rbxcdn.com/180DAY-7c0d8efb96170a959f139c3f27c73233/768/432/Image/Webp/noFilter',
  'survive-zombie-arena': 'https://tr.rbxcdn.com/180DAY-5fdeee22007259bdf80543463dbb0003/768/432/Image/Webp/noFilter',
  'attack-on-titan-revolution': 'https://tr.rbxcdn.com/180DAY-d72c3cae696292e59f459d51dc79e17d/768/432/Image/Webp/noFilter',
  'broken-blade': '/images/games/broken-blade.svg',
  'sailor-piece': '/images/games/sailor-piece.svg',
  'anime-apocalypse': '/images/games/anime-apocalypse.svg',
  'anime-eternal': '/images/games/anime-eternal.svg',
  'universal-tower-defense-x': '/images/games/universal-tower-defense-x.svg',
  'dig': 'https://tr.rbxcdn.com/180DAY-117cc5b2e7d12b527b2b5edeb1985c80/768/432/Image/Webp/noFilter',
  'sols-rng': 'https://tr.rbxcdn.com/180DAY-7f9646a805ee3348b35916fdd0d05911/768/432/Image/Webp/noFilter',
  'jules-rng': 'https://tr.rbxcdn.com/180DAY-17445b6851425eb6de2f0e338ded937f/768/432/Image/Webp/noFilter',
  'weapon-rng': 'https://tr.rbxcdn.com/180DAY-c56b4edacb31854ea7e337199096cdbf/768/432/Image/Webp/noFilter',
  'character-rng': 'https://tr.rbxcdn.com/180DAY-b34e867b2650f1ed95a063422864ddab/768/432/Image/Webp/noFilter',
  'case-simulator-rng': 'https://tr.rbxcdn.com/180DAY-da13783f5b902532142af5ec7480b368/768/432/Image/Webp/noFilter',
  'button-rng-2': 'https://tr.rbxcdn.com/180DAY-ca5bbbd2e2bc42d6d070b8f05ee992e4/768/432/Image/Webp/noFilter',
  'rng-heroes': 'https://tr.rbxcdn.com/180DAY-67d8d731787391608a925ccda724bfde/768/432/Image/Webp/noFilter',
  'fish-it': 'https://tr.rbxcdn.com/180DAY-663e97ff6d18b7b048a6af98a5c58666/768/432/Image/Webp/noFilter',
  'be-a-fish-bait': 'https://tr.rbxcdn.com/180DAY-fd0ab7c320853a922b46f9fb1d360459/768/432/Image/Webp/noFilter',
  'anime-spirits': 'https://tr.rbxcdn.com/180DAY-b686085630a466659f79829aeca68585/768/432/Image/Webp/noFilter',
  'slap-battles': 'https://tr.rbxcdn.com/180DAY-76fedd397e6cb8051ba34ec7fd008737/768/432/Image/Webp/noFilter',
  'forsaken': 'https://tr.rbxcdn.com/180DAY-ade3a7a657babdc426cad38911362395/768/432/Image/Webp/noFilter',
  'driving-empire': 'https://tr.rbxcdn.com/180DAY-89a1aafd7f921f62bf914c9297401578/768/432/Image/Webp/noFilter',
  'evasion-clavier': 'https://tr.rbxcdn.com/180DAY-9c367a6529b84f4f199fd85dd8ad83bd/768/432/Image/Webp/noFilter',
  'ferme-d-anneaux': 'https://tr.rbxcdn.com/180DAY-5c24b09b1d9bdfa44deadb955fd8d2fb/768/432/Image/Webp/noFilter',
  'vendre-des-citrons': 'https://tr.rbxcdn.com/180DAY-3bb611c1f3b4d5bfa396b1ae965134af/768/432/Image/Webp/noFilter',
  'world-fighters': 'https://tr.rbxcdn.com/180DAY-81425ab9ff608a7dbffc828b101e9583/768/432/Image/Webp/noFilter',
  'noob-incremental': 'https://tr.rbxcdn.com/180DAY-8273fdf7d5a9074bc47861d7719c5392/768/432/Image/Webp/noFilter',
  'my-gaming-cafe': 'https://tr.rbxcdn.com/180DAY-1098acc33826a62e14631c304530f427/768/432/Image/Webp/noFilter',
  'catch-and-tame': 'https://tr.rbxcdn.com/180DAY-85b284be6afe5891082495b9d5dfb1c3/768/432/Image/Webp/noFilter',
  'build-a-ring-farm': 'https://tr.rbxcdn.com/180DAY-5c24b09b1d9bdfa44deadb955fd8d2fb/480/270/Image/Webp/noFilter',
  'anime-warriors-iii': 'https://tr.rbxcdn.com/180DAY-aa717796314d2704ad5951d6a79b5d35/768/432/Image/Webp/noFilter',
  'anime-squadron': 'https://tr.rbxcdn.com/180DAY-8765e83249c912e589677cf9ead08426/768/432/Image/Webp/noFilter',
  'anime-card-farm': 'https://tr.rbxcdn.com/180DAY-ddbb8f3b68bef5516e2b6365d0cd08c8/768/432/Image/Webp/noFilter',
  'chicken-farm': 'https://tr.rbxcdn.com/180DAY-64e9d478a689042124f98d8cce7edea9/768/432/Image/Webp/noFilter',
  '1-mine-per-click': 'https://tr.rbxcdn.com/180DAY-7e0a7a6a606be71764918483ef5a9084/768/432/Image/Webp/noFilter',
  'world-cup-album': '/images/games/world-cup-album.svg',
  'storage-hunters-open-world': 'https://tr.rbxcdn.com/180DAY-03760010d55285753fa05552ecf8851a/768/432/Image/Webp/noFilter',
  '1-magic-evolution': 'https://tr.rbxcdn.com/180DAY-984161a5bc54067ad08e78d512a2cc58/768/432/Image/Webp/noFilter',
  'evomon': 'https://tr.rbxcdn.com/180DAY-43e63528aeba863fc3c6164575c7bedb/768/432/Image/Webp/noFilter',
  'grow-a-garden-2': 'https://tr.rbxcdn.com/180DAY-7dce127c50d46bb92b9601335b8363b3/768/432/Image/Webp/noFilter',
  'mini-war': 'https://tr.rbxcdn.com/180DAY-7451c6f9d2637ca3b106eb665f1b21a2/768/432/Image/Webp/noFilter',
  '1-aura-per-click': 'https://tr.rbxcdn.com/180DAY-1bc2e3071dbb1b27e139a6ec18f4f166/768/432/Image/Webp/noFilter',
  'anime-fighting-simulator-reborn': 'https://tr.rbxcdn.com/180DAY-ad195be47fec95664c1c3176235720b2/768/432/Image/Webp/noFilter',
  'liminalite-invisible': 'https://tr.rbxcdn.com/180DAY-9716808bc266a9880f22263ca9fa98bc/768/432/Image/Webp/noFilter',
  'demonologie': 'https://tr.rbxcdn.com/180DAY-2651cff28f8766658687d6df2067bf03/768/432/Image/Webp/noFilter',
  'mini-guerre': 'https://tr.rbxcdn.com/180DAY-c60de7bb9807464a0564c898db8d8e62/480/270/Image/Webp/noFilter',
  'cliqueur-phonk': 'https://tr.rbxcdn.com/180DAY-ae08f34ff73b587272264895a4e43bae/768/432/Image/Webp/noFilter',
  'arene-de-sniper': 'https://tr.rbxcdn.com/180DAY-41326a752aca93f2fd10aa7e8f5c911d/768/432/Image/Webp/noFilter',
  'tour-needoh': 'https://tr.rbxcdn.com/180DAY-709282c91d3fb74801b493d7987004b3/768/432/Image/Webp/noFilter',
  'blox-fruits': 'https://tr.rbxcdn.com/180DAY-09e621f1df2e404a391adf389d2bea47/768/432/Image/Webp/noFilter',
  'pet-simulator-x': 'https://tr.rbxcdn.com/180DAY-ff6798cca7069bfa88247713f7626eb5/768/432/Image/Webp/noFilter',
  'adopt-me': 'https://tr.rbxcdn.com/180DAY-0118acd181f1ac414e29923804ac17ba/768/432/Image/Webp/noFilter',
  'murder-mystery-2': 'https://tr.rbxcdn.com/180DAY-69fa49d885010bebd6a2d0187b66d106/768/432/Image/Webp/noFilter',
  'royale-high': 'https://tr.rbxcdn.com/180DAY-dfc7b7da37efc4e4d9a7d207370a1966/768/432/Image/Webp/noFilter',
  'brookhaven': 'https://tr.rbxcdn.com/180DAY-9db1e3b71951f8732226b526b32580e3/768/432/Image/Webp/noFilter',
  'tower-of-hell': 'https://tr.rbxcdn.com/180DAY-30df204e4a0188e05ea2dcd225dab32d/768/432/Image/Webp/noFilter',
  'work-at-a-pizza-place': 'https://tr.rbxcdn.com/180DAY-d2cec03db65c18174cf85059e43ccbdf/768/432/Image/Webp/noFilter',
  'shindo-life': 'https://tr.rbxcdn.com/180DAY-e0736769672017234e02eb8938cb684d/768/432/GameMediaItem12/Webp/noFilter',
  'king-legacy': 'https://tr.rbxcdn.com/180DAY-505d0cc614022636a562fd3ff8808ba0/768/432/Image/Webp/noFilter',
  'anime-adventures': 'https://tr.rbxcdn.com/180DAY-b630f8fd329cf5f0c9b57451f4c1f47a/768/432/Image/Webp/noFilter',
  'fruit-battlegrounds': 'https://tr.rbxcdn.com/180DAY-6688078543e2f947bf998f31c4601037/768/432/Image/Webp/noFilter',
  'rivals': 'https://tr.rbxcdn.com/180DAY-fb02f48458ff689309df8d52bf516d04/768/432/Image/Webp/noFilter',
  'encounters': 'https://tr.rbxcdn.com/180DAY-024bcafc4df055789126ae841598d15d/768/432/Image/Webp/noFilter',
  'grow-a-garden': 'https://tr.rbxcdn.com/180DAY-c211ffafea69a9d9d4956c500ba011e1/768/432/Image/Webp/noFilter',
  'blade-ball': 'https://tr.rbxcdn.com/180DAY-bb25a2cda73447c7c7b8179e4869cab0/768/432/Image/Webp/noFilter',
  'anime-defenders': 'https://tr.rbxcdn.com/180DAY-c5a2289b4baf7194add46247482074d7/768/432/Image/Webp/noFilter',
  'toilet-tower-defense': 'https://tr.rbxcdn.com/180DAY-5a9d6ca7af3e521497366c956bbbea05/768/432/Image/Webp/noFilter',
  'pet-simulator-99': 'https://tr.rbxcdn.com/180DAY-74ad983d94134f8afd21b47c1e2c4e02/768/432/Image/Webp/noFilter',
  'bee-swarm-simulator': 'https://tr.rbxcdn.com/180DAY-315e29556054777604420711cb64f0b6/768/432/Image/Webp/noFilter',
  'anime-vanguards': 'https://tr.rbxcdn.com/180DAY-64a091a75b4a67bfd15439b058a0b2da/768/432/Image/Webp/noFilter',
  'arsenal': 'https://tr.rbxcdn.com/180DAY-409cfd2e6dcb5afa3fe41b545752733a/768/432/Image/Webp/noFilter',
  'jailbreak': 'https://tr.rbxcdn.com/180DAY-9ac64d7e310270d0f886363f4159ce0c/768/432/Image/Webp/noFilter',
  'bedwars': 'https://tr.rbxcdn.com/180DAY-290ed0caee58521cdbfd5eb01f7f6d2e/768/432/Image/Webp/noFilter',
  'fisch': 'https://tr.rbxcdn.com/180DAY-0b48b36aaaebb05f29da4beb58790100/768/432/Image/Webp/noFilter',
  'dress-to-impress': 'https://tr.rbxcdn.com/180DAY-e0eb9abac582821ff220475817ba45be/768/432/Image/Webp/noFilter',
  'da-hood': 'https://tr.rbxcdn.com/180DAY-655a8b7fc990b48f595db9bcfd7ea70b/768/432/Image/Webp/noFilter',
  'bubble-gum-simulator-infinity': 'https://tr.rbxcdn.com/180DAY-8aac6f41f4d2b8739680ff87aaf3a4f2/768/432/Image/Webp/noFilter',
  'blue-lock-rivals': 'https://tr.rbxcdn.com/180DAY-d3badd2fb676c817355951c5fa8525a6/768/432/Image/Webp/noFilter',
  'volleyball-legends': 'https://tr.rbxcdn.com/180DAY-9bd05bd03c4d265eb5e9306d8523064d/768/432/Image/Webp/noFilter',
  'steal-a-brainrot': 'https://tr.rbxcdn.com/180DAY-cdcba985adea2b974ef0160869d555f1/768/432/Image/Webp/noFilter',
  'build-a-boat-for-treasure': 'https://tr.rbxcdn.com/180DAY-3f2c3612b14d208abf0231afaf6dec1a/768/432/Image/Webp/noFilter',
  'anime-last-stand': 'https://tr.rbxcdn.com/180DAY-a2d20bf051ff960d44f7805f9e029890/768/432/Image/Webp/noFilter',
  '99-nights-in-the-forest': 'https://tr.rbxcdn.com/180DAY-c5215eabc21f46723f0084f99bb7622c/768/432/Image/Webp/noFilter',
  'plants-vs-brainrots': 'https://tr.rbxcdn.com/180DAY-9bbceb61dc59ed62eab8c2d475f13133/768/432/Image/Webp/noFilter',
  'dead-rails': 'https://tr.rbxcdn.com/180DAY-ffa0a3617465f28976b9b18485e0ac50/768/432/Image/Webp/noFilter',
  'jujutsu-infinite': '/images/games/jujutsu-infinite.svg',
  'anime-reborn': '/images/games/anime-reborn.svg',
  'untitled-boxing-game': '/images/games/untitled-boxing-game.svg',
  'type-soul': '/images/games/type-soul.svg',
  'basketball-zero': '/images/games/basketball-zero.svg',
  'haze-piece': 'https://tr.rbxcdn.com/180DAY-cb214d97a5fc8f31e1b47ea17fe6abaa/768/432/Image/Webp/noFilter',
  'all-star-tower-defense': 'https://tr.rbxcdn.com/180DAY-9fbd50db5a51699b733c9529ee542d19/768/432/Image/Webp/noFilter',
  'anime-champions-simulator': 'https://tr.rbxcdn.com/180DAY-9d4be137161ea266ba1c2c6f28832e21/768/432/Image/Webp/noFilter',
  'animal-hospital': 'https://tr.rbxcdn.com/180DAY-db27bdc698b088f2d8352327f7dc64f6/768/432/Image/Webp/noFilter',
  'demonology': 'https://tr.rbxcdn.com/180DAY-2651cff28f8766658687d6df2067bf03/768/432/Image/Webp/noFilter',
  'sonic-speed-simulator': '/images/games/sonic-speed-simulator.svg',
  'tower-defense-simulator': 'https://tr.rbxcdn.com/180DAY-2073cd486b40c4a8a517f577292dd335/768/432/Image/Webp/noFilter',
  'project-slayers': 'https://tr.rbxcdn.com/180DAY-612b92100da817e8dc2bb8fd35ce117e/768/432/Image/Webp/noFilter',
  'the-strongest-battlegrounds': 'https://tr.rbxcdn.com/180DAY-c947df5b221c30672c3591247a8c6495/768/432/Image/Webp/noFilter',
  'spongebob-tower-defense': 'https://tr.rbxcdn.com/180DAY-c3a62fcdf7e0a60cd52456d65f267689/768/432/Image/Webp/noFilter',
  'garden-tower-defense': 'https://tr.rbxcdn.com/180DAY-5cdf91e7a673dac3be39b1f4b759ba8c/768/432/Image/Webp/noFilter',
  'heroes-battlegrounds': 'https://tr.rbxcdn.com/180DAY-c2134d77865609146932437200b1418b/768/432/Image/Webp/noFilter',
  'mad-city': 'https://tr.rbxcdn.com/180DAY-e03eb43e97fb7031d8187b808fd7ff27/768/432/Image/Webp/noFilter',
  'combat-warriors': 'https://tr.rbxcdn.com/180DAY-a631d6d73730a77f93b02eb3b0e8b06c/768/432/Image/Webp/noFilter',
  'survive-the-killer': 'https://tr.rbxcdn.com/180DAY-4f30b695e340b41799ff15643fff9795/768/432/Image/Webp/noFilter',
  'peroxide': 'https://tr.rbxcdn.com/180DAY-e7f44a8b2564e076c8cfd0ba8341473c/768/432/Image/Webp/noFilter',
  'grimoires-era': 'https://tr.rbxcdn.com/180DAY-22ad2395f8b1adb51e1e61059b2c516e/768/432/Image/Webp/noFilter',
  'pressure': 'https://tr.rbxcdn.com/180DAY-d1c2185252b44ef983fb68b650296ba1/768/432/Image/Webp/noFilter',
  'muscle-legends': 'https://tr.rbxcdn.com/180DAY-445ec13cdfdb598442a03dc8ec35cbe2/768/432/Image/Webp/noFilter',
  'anime-dimensions-simulator': 'https://tr.rbxcdn.com/180DAY-a4da959bad60ef36277dc0045c2fa21b/768/432/Image/Webp/noFilter',
  'ro-ghoul': 'https://tr.rbxcdn.com/180DAY-107ea4bd02b186b6b0cf1bcd53c63c1b/768/432/Image/Webp/noFilter',
  'evade': 'https://tr.rbxcdn.com/180DAY-1365aa6b6a73daf189f6be9ffffaa44f/768/432/Image/Webp/noFilter',
  'dragon-adventures': 'https://tr.rbxcdn.com/180DAY-378f465f5b2232102139d19d1f8f0c03/768/432/Image/Webp/noFilter',
  'car-dealership-tycoon': 'https://tr.rbxcdn.com/180DAY-1be6204b082e09b83b2d7c0a55929fdf/768/432/Image/Webp/noFilter',
  'pls-donate': 'https://tr.rbxcdn.com/180DAY-3b749df76d352f98ef704c75c538be57/768/432/Image/Webp/noFilter',
  'wizard-alchemy': 'https://tr.rbxcdn.com/180DAY-cbe05e8cd15a5080d304489b02f92018/768/432/Image/Webp/noFilter',
  'restaurant-tycoon-3': 'https://tr.rbxcdn.com/180DAY-b5aa3d1ad2c1524816211fb343ce4086/768/432/Image/Webp/noFilter',
  'clover-retribution': '/images/games/clover-retribution.svg',
  'project-mugetsu': 'https://tr.rbxcdn.com/180DAY-95701e9021e5e6350539af488d158997/768/432/Image/Webp/noFilter',
  'dragon-blox': 'https://tr.rbxcdn.com/180DAY-1519fcceff39d331ec4f461f7c6da19b/768/432/Image/Webp/noFilter',
  'grand-piece-online': 'https://tr.rbxcdn.com/180DAY-ae088ebacf2ae4de364c56acaf635bb8/768/432/GameMediaItem6/Webp/noFilter',
  'scroll-a-brainrot': 'https://tr.rbxcdn.com/180DAY-3aa2a4e5a9735f356026b0ee84215e99/768/432/Image/Webp/noFilter',
  'spin-a-brainrot': 'https://tr.rbxcdn.com/180DAY-61d8cd3b3a89a6122467c49e746dc194/768/432/Image/Webp/noFilter',
  'be-a-brainrot': 'https://tr.rbxcdn.com/180DAY-c41e9a9b4678a149f1fc9f9f6a737d9e/768/432/Image/Webp/noFilter',
  'anime-rift-tower-defense': 'https://tr.rbxcdn.com/180DAY-000826b5aefec382cc3367192cdb5c2f/768/432/Image/Webp/noFilter',
  'doors': 'https://tr.rbxcdn.com/180DAY-ee22e20e38a2496ec796168071deb670/768/432/Image/Webp/noFilter',
  'anime-story-2': 'https://tr.rbxcdn.com/180DAY-30f248b0e384d42583a14688f1df6bf8/768/432/Image/Webp/noFilter',
  'anime-rangers-x': 'https://tr.rbxcdn.com/180DAY-c0b8f9f306b6f4363e21223df1e04d3b/768/432/Image/Webp/noFilter',
  'a-one-piece-game': 'https://tr.rbxcdn.com/180DAY-7657e3f8af6ae0c9d28b20119b31d24c/768/432/Image/Webp/noFilter',
  'sakura-stand': 'https://tr.rbxcdn.com/180DAY-491780744f6da1bb87bd844514d2215d/768/432/Image/Webp/noFilter',
  'untitled-attack-on-titan': 'https://tr.rbxcdn.com/180DAY-52684c00ebe2aadf3de4eeaf4eb435d2/768/432/Image/Webp/noFilter',
  'ninja-legends': 'https://tr.rbxcdn.com/180DAY-0616aa68474d2273776bf20eed8a8df4/768/432/Image/Webp/noFilter',
  'arm-wrestle-simulator': 'https://tr.rbxcdn.com/180DAY-a975190850087e76565d9601aef9ffe6/768/432/Image/Webp/noFilter',
  'strongman-simulator': 'https://tr.rbxcdn.com/180DAY-2a05a4eb85791b120cd6aae26dac0724/768/432/Image/Webp/noFilter',
  'anime-souls-simulator-x': 'https://tr.rbxcdn.com/180DAY-cb95adeca9ea0a7700c5f437a3f1c668/768/432/Image/Webp/noFilter',
  'fire-force-online': 'https://tr.rbxcdn.com/180DAY-fda3e9fc1df7894ef7f8a5c5b75db606/768/432/Image/Webp/noFilter',
  'skibidi-masters-tower-defense': 'https://tr.rbxcdn.com/180DAY-648b86bc997457836bbb16eb5cdad65e/768/432/Image/Webp/noFilter',
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
const GAMES_INDEX = [{ name: 'Steal From The Rich', slug: 'steal-from-the-rich', emoji: '💰', codes: 0 },
{ name: 'Ride A Pet', slug: 'ride-a-pet', emoji: '🐶', codes: 0 },
  { name: '+1 Loot To Forge', slug: '1-loot-to-forge', emoji: '⚒️', codes: 2 },
  { name: 'Slayers 2', slug: 'slayers-2', emoji: '⚔️', codes: 2 },
  { name: 'Illegal Soccer', slug: 'illegal-soccer', emoji: '⚽', codes: 0 },
{ name: 'Search For The Needle', slug: 'search-for-the-needle', emoji: '🪡', codes: 2 },
  { name: 'Dungeon Quest Reborn', slug: 'dungeon-quest-reborn', emoji: '⚔️', codes: 0 },
{ name: "Anime Origins", slug: 'anime-origins', emoji: '⚔️', codes: 9 },
  { name: "Grow a Chicken Fighter", slug: 'grow-a-chicken-fighter', emoji: '🐔', codes: 4 },
  { name: "Dig and Clean", slug: 'dig-and-clean', emoji: '🧼', codes: 3 },
  { name: "Fish an Anime RNG", slug: 'fish-an-anime-rng', emoji: '🎣', codes: 5 },
  { name: "Anime Stars", slug: 'anime-stars', emoji: '⭐', codes: 6 },
  { name: "Anime Expeditions", slug: 'anime-expeditions', emoji: '🛡️', codes: 10 },
  { name: "Be a Fish Bait", slug: 'be-a-fish-bait', emoji: '🐟', codes: 8 },
  { name: "Spin a Soccer Card", slug: 'spin-a-soccer-card', emoji: '⚽', codes: 6 },
  { name: "Merge a Nuke", slug: 'merge-a-nuke', emoji: '☢️', codes: 3 },
  { name: "VV: ULTIMATUM", slug: 'vv-ultimatum', emoji: '⚔️', codes: 1 },
  { name: "FIFA Super Soccer", slug: 'fifa-super-soccer', emoji: '⚽', codes: 4 },
  { name: "Hypershot", slug: 'hypershot', emoji: '🔫', codes: 4 },
  { name: "BlockSpin", slug: 'blockspin', emoji: '🔪', codes: 3 },
  { name: "Run a Restaurant", slug: 'run-a-restaurant', emoji: '🍔', codes: 1 },
  { name: "Squid Game X", slug: 'squid-game-x', emoji: '🦑', codes: 6 },
  { name: "Catch a Monster", slug: 'catch-a-monster', emoji: '👾', codes: 6 },
  { name: "Brainrot Evolution", slug: 'brainrot-evolution', emoji: '🧠', codes: 6 },
  { name: "100 Days at Sea", slug: '100-days-at-sea', emoji: '🌊', codes: 0 },
  { name: "A Dusty Trip", slug: 'a-dusty-trip', emoji: '🚗', codes: 3 },
  { name: "War Tycoon", slug: 'war-tycoon', emoji: '🪖', codes: 4 },
  { name: "Iron Soul: Dungeon", slug: 'iron-soul-dungeon', emoji: '⚒️', codes: 11 },
  { name: "Blox Monsters", slug: 'blox-monsters', emoji: '🐾', codes: 5 },
  { name: "Car Crushers 2", slug: 'car-crushers-2', emoji: '💥', codes: 6 },
  { name: "Steal a Fish", slug: 'steal-a-fish', emoji: '🐟', codes: 3 },
  { name: 'Steal An Egg', slug: 'steal-an-egg', emoji: '🥚', codes: 0 },
  { name: "Knockout", slug: 'knockout', emoji: '🥊', codes: 8 },
  { name: "My Gym", slug: 'my-gym', emoji: '🏋️', codes: 3 },
  { name: "Untitled Tag Game", slug: 'untitled-tag-game', emoji: '🏃', codes: 0 },
  { name: "BloxStrike", slug: 'bloxstrike', emoji: '🔫', codes: 1 },
  { name: "Twenty One", slug: 'twenty-one', emoji: '🔪', codes: 2 },
  { name: "Anime Astral Simulator", slug: 'anime-astral-simulator', emoji: '⭐', codes: 9 },
  { name: "Anime Battle RNG", slug: 'anime-battle-rng', emoji: '🎲', codes: 8 },
  { name: "Anime Fighters Simulator", slug: 'anime-fighters', emoji: '👊', codes: 8 },
  { name: "Anime Fighting Simulator", slug: 'anime-fighting-simulator', emoji: '⚔️', codes: 4 },
  { name: "Anime Reversal", slug: 'anime-reversal', emoji: '🌀', codes: 2 },
  { name: "LOCKED", slug: 'locked', emoji: '⚽', codes: 9 },
  { name: "Defend ur base with anime", slug: 'defend-ur-base-with-anime', emoji: '🛡️', codes: 5 },
  { name: "Anime RNG", slug: 'anime-rng', emoji: '🎲', codes: 5 },
  { name: "UGC Limited", slug: 'ugc-limited', emoji: '🎁', codes: 32 },
  { name: "Jujutsu Shenanigans", slug: 'jujutsu-shenanigans', emoji: '🌀', codes: 5 },
  { name: "Kick a Lucky Block", slug: 'kick-a-lucky-block', emoji: '🎁', codes: 0 },
  { name: "Dandy's World", slug: 'dandys-world', emoji: '🧸', codes: 1 },
  { name: "Slime RNG", slug: 'slime-rng', emoji: '🟢', codes: 11 },
  { name: "Survive Zombie Arena", slug: 'survive-zombie-arena', emoji: '🧟', codes: 2 },
  { name: "Attack on Titan Revolution", slug: 'attack-on-titan-revolution', emoji: '⚔️', codes: 21 },
  { name: "Broken Blade", slug: 'broken-blade', emoji: '⚔️', codes: 11 },
  { name: "Sailor Piece", slug: 'sailor-piece', emoji: '⚓', codes: 16 },
  { name: "Anime Apocalypse", slug: 'anime-apocalypse', emoji: '🧟', codes: 15 },
  { name: "Anime Eternal", slug: 'anime-eternal', emoji: '⭐', codes: 13 },
  { name: "Universal Tower Defense X", slug: 'universal-tower-defense-x', emoji: '🏰', codes: 18 },
  { name: 'DIG', slug: 'dig', emoji: '⛏️', codes: 1 },
  { name: "Sol's RNG", slug: 'sols-rng', emoji: '🎲', codes: 8 }, { name: "Jule's RNG", slug: 'jules-rng', emoji: '🎲', codes: 16 }, { name: "Weapon RNG", slug: 'weapon-rng', emoji: '⚔️', codes: 4 }, { name: "Character RNG", slug: 'character-rng', emoji: '🎭', codes: 10 }, { name: "Case Simulator RNG", slug: 'case-simulator-rng', emoji: '📦', codes: 1 }, { name: "Button RNG 2", slug: 'button-rng-2', emoji: '🔘', codes: 0 }, { name: "RNG Heroes", slug: 'rng-heroes', emoji: '🏹', codes: 2 },
  { name: 'Fish It', slug: 'fish-it', emoji: '🎣', codes: 0 },
  { name: 'Anime Spirits', slug: 'anime-spirits', emoji: '🗡️', codes: 6 },
  { name: 'Slap Battles', slug: 'slap-battles', emoji: '👏', codes: 3 },
  { name: 'Forsaken', slug: 'forsaken', emoji: '🔪', codes: 0 },
  { name: 'Driving Empire', slug: 'driving-empire', emoji: '🏎️', codes: 19 },
  { name: 'Évasion Clavier', slug: 'evasion-clavier', emoji: '⌨️', codes: 0 },
  { name: 'Construire une Ferme d\'Anneaux', slug: 'ferme-d-anneaux', emoji: '💍', codes: 0 },
  { name: 'Vendre des Citrons', slug: 'vendre-des-citrons', emoji: '🍋', codes: 0 },
  { name: 'World Fighters', slug: 'world-fighters', emoji: '🥋', codes: 11 },
  { name: 'Noob Incremental', slug: 'noob-incremental', emoji: '🧱', codes: 17 },
  { name: 'My Gaming Cafe', slug: 'my-gaming-cafe', emoji: '💻', codes: 0 },
  { name: 'Catch and Tame', slug: 'catch-and-tame', emoji: '🐟', codes: 0 },
  { name: 'Build A Ring Farm', slug: 'build-a-ring-farm', emoji: '🌽', codes: 9 },
  { name: 'Anime Warriors III', slug: 'anime-warriors-iii', emoji: '⛩️', codes: 0 },
  { name: 'Anime Squadron', slug: 'anime-squadron', emoji: '⚔️', codes: 11 },
  { name: 'Anime Card Farm', slug: 'anime-card-farm', emoji: '🃏', codes: 2 },
  { name: 'Chicken Farm', slug: 'chicken-farm', emoji: '🐔', codes: 0 },
  { name: '+1 Mine Per Click', slug: '1-mine-per-click', emoji: '⛏️', codes: 0 },
  { name: 'World Cup Album', slug: 'world-cup-album', emoji: '⚽', codes: 0 },
  { name: 'Storage Hunters Open World', slug: 'storage-hunters-open-world', emoji: '📦', codes: 0 },
  { name: '+1 Magic Evolution', slug: '1-magic-evolution', emoji: '🪄', codes: 0 },
  { name: 'Evomon', slug: 'evomon', emoji: '🐲', codes: 4 },
  { name: 'Grow a Garden 2', slug: 'grow-a-garden-2', emoji: '🌱', codes: 1 },
  { name: '+1 Aura Per Click', slug: '1-aura-per-click', emoji: '🌀', codes: 0 },
  { name: 'Anime Fighting Simulator Reborn', slug: 'anime-fighting-simulator-reborn', emoji: '🥋', codes: 4 },
  { name: 'Liminalité Invisible', slug: 'liminalite-invisible', emoji: '🌫️', codes: 0 },
  { name: 'Démonologie', slug: 'demonologie', emoji: '👹', codes: 0 },
  { name: 'Mini-Guerre', slug: 'mini-guerre', emoji: '🪖', codes: 2 },
  { name: 'Cliqueur Phonk', slug: 'cliqueur-phonk', emoji: '🎵', codes: 0 },
  { name: 'Arène de Sniper', slug: 'arene-de-sniper', emoji: '🎯', codes: 0 },
  { name: 'Tour Needoh', slug: 'tour-needoh', emoji: '🗼', codes: 0 },
  { name: 'Blox Fruits',          slug: 'blox-fruits',          emoji: '🍎', codes: 23 },
  { name: 'Pet Simulator X',      slug: 'pet-simulator-x',      emoji: '🐾', codes: 8 },
  { name: 'Adopt Me',             slug: 'adopt-me',             emoji: '🐣', codes: 0 },
  { name: 'Anime Adventures',     slug: 'anime-adventures',     emoji: '⚔️', codes: 6 },
  { name: 'Brookhaven',           slug: 'brookhaven',           emoji: '🏙️', codes: 0 },
  { name: 'Tower of Hell',        slug: 'tower-of-hell',        emoji: '🗼', codes: 0 },
  { name: 'Murder Mystery 2',     slug: 'murder-mystery-2',     emoji: '🔪', codes: 0 },
  { name: 'Shindo Life',          slug: 'shindo-life',          emoji: '🌀', codes: 11 },
  { name: 'Royale High',          slug: 'royale-high',          emoji: '👑', codes: 1 },
  { name: 'Fruit Battlegrounds',  slug: 'fruit-battlegrounds',  emoji: '💥', codes: 5 },
  { name: 'King Legacy',          slug: 'king-legacy',          emoji: '⚡', codes: 5 },
  { name: 'Encounters',           slug: 'encounters',           emoji: '👾', codes: 1 },
  { name: 'Rivals',               slug: 'rivals',               emoji: '🎯', codes: 9 },
  { name: 'Work at a Pizza Place',slug: 'work-at-a-pizza-place',emoji: '🍕', codes: 0 },
  { name: 'Grow a Garden',        slug: 'grow-a-garden',        emoji: '🌱', codes: 2 },
  { name: 'Blade Ball',           slug: 'blade-ball',           emoji: '⚔️', codes: 23 },
  { name: 'Anime Defenders',      slug: 'anime-defenders',      emoji: '🗡️', codes: 0 },
  { name: 'Toilet Tower Defense', slug: 'toilet-tower-defense', emoji: '🚽', codes: 0 },
  { name: 'Pet Simulator 99',     slug: 'pet-simulator-99',     emoji: '🐹', codes: 0 },
  { name: 'Bee Swarm Simulator', slug: 'bee-swarm-simulator',  emoji: '🐝', codes: 17 },
  { name: 'Anime Vanguards',     slug: 'anime-vanguards',      emoji: '⚔️', codes: 10 },
  { name: 'Arsenal',             slug: 'arsenal',              emoji: '🔫', codes: 5 },
  { name: 'Jailbreak',           slug: 'jailbreak',            emoji: '🚔', codes: 4 },
  { name: 'BedWars',             slug: 'bedwars',              emoji: '🛏️', codes: 0 },
  { name: 'Fisch', slug: 'fisch', emoji: '🐟', codes: 4 },
  { name: 'Dress to Impress', slug: 'dress-to-impress', emoji: '👗', codes: 41 },
  { name: 'Da Hood', slug: 'da-hood', emoji: '🔫', codes: 18 },
  { name: 'Bubble Gum Simulator Infinity', slug: 'bubble-gum-simulator-infinity', emoji: '🫧', codes: 5 },
  { name: 'Blue Lock Rivals', slug: 'blue-lock-rivals', emoji: '⚽', codes: 8 },
  { name: 'Volleyball Legends', slug: 'volleyball-legends', emoji: '🏐', codes: 3 },
  { name: 'Steal a Brainrot', slug: 'steal-a-brainrot', emoji: '🧠', codes: 0 },
  { name: 'Build a Boat for Treasure', slug: 'build-a-boat-for-treasure', emoji: '🚤', codes: 7 },
  { name: 'Anime Last Stand', slug: 'anime-last-stand', emoji: '🗡️', codes: 21 },
  { name: '99 Nights in the Forest', slug: '99-nights-in-the-forest', emoji: '🔦', codes: 2 },
  { name: 'Plants Vs Brainrots', slug: 'plants-vs-brainrots', emoji: '🌻', codes: 5 },
  { name: 'Dead Rails', slug: 'dead-rails', emoji: '🚂', codes: 0 },
  { name: 'Jujutsu Infinite', slug: 'jujutsu-infinite', emoji: '🌀', codes: 0 },
  { name: 'Anime Reborn', slug: 'anime-reborn', emoji: '🗡️', codes: 0 },
  { name: 'Untitled Boxing Game', slug: 'untitled-boxing-game', emoji: '🥊', codes: 9 },
  { name: 'Type Soul', slug: 'type-soul', emoji: '💀', codes: 11 },
  { name: 'Basketball Zero', slug: 'basketball-zero', emoji: '🏀', codes: 10 },
  { name: 'Haze Piece', slug: 'haze-piece', emoji: '🌊', codes: 3 },
  { name: 'All Star Tower Defense', slug: 'all-star-tower-defense', emoji: '🌟', codes: 4 },
  { name: 'Anime Champions Simulator', slug: 'anime-champions-simulator', emoji: '🌌', codes: 11 },
  { name: 'Animal Hospital', slug: 'animal-hospital', emoji: '🏥', codes: 0 },
  { name: 'Demonology', slug: 'demonology', emoji: '🕯️', codes: 0 },
  { name: 'Sonic Speed Simulator', slug: 'sonic-speed-simulator', emoji: '💨', codes: 8 },
  { name: 'Tower Defense Simulator', slug: 'tower-defense-simulator', emoji: '🧟', codes: 0 },
  { name: 'Project Slayers', slug: 'project-slayers', emoji: '🌸', codes: 0 },
  { name: 'The Strongest Battlegrounds', slug: 'the-strongest-battlegrounds', emoji: '👊', codes: 0 },
  { name: 'SpongeBob Tower Defense', slug: 'spongebob-tower-defense', emoji: '🍍', codes: 2 },
  { name: 'Garden Tower Defense', slug: 'garden-tower-defense', emoji: '🥕', codes: 19 },
  { name: 'Heroes Battlegrounds', slug: 'heroes-battlegrounds', emoji: '🦸', codes: 21 },
  { name: 'Mad City: Chapter 2', slug: 'mad-city', emoji: '🚁', codes: 6 },
  { name: 'Combat Warriors', slug: 'combat-warriors', emoji: '🗡️', codes: 0 },
  { name: 'Survive the Killer', slug: 'survive-the-killer', emoji: '🔪', codes: 0 },
  { name: 'Peroxide', slug: 'peroxide', emoji: '💀', codes: 4 },
  { name: 'Grimoires Era', slug: 'grimoires-era', emoji: '📖', codes: 11 },
  { name: 'Pressure', slug: 'pressure', emoji: '🌊', codes: 4 },
  { name: 'Muscle Legends', slug: 'muscle-legends', emoji: '💪', codes: 14 },
  { name: 'Anime Dimensions Simulator', slug: 'anime-dimensions-simulator', emoji: '🌌', codes: 10 },
  { name: 'Ro-Ghoul', slug: 'ro-ghoul', emoji: '👁️', codes: 5 },
  { name: 'Evade', slug: 'evade', emoji: '👻', codes: 0 },
  { name: 'Dragon Adventures', slug: 'dragon-adventures', emoji: '🐉', codes: 6 },
  { name: 'Car Dealership Tycoon', slug: 'car-dealership-tycoon', emoji: '🚗', codes: 14 },
  { name: 'PLS DONATE', slug: 'pls-donate', emoji: '💸', codes: 7 },
  { name: 'Wizard Alchemy', slug: 'wizard-alchemy', emoji: '🧙', codes: 10 },
  { name: 'Restaurant Tycoon 3', slug: 'restaurant-tycoon-3', emoji: '🍕', codes: 11 },
  { name: 'Clover Retribution', slug: 'clover-retribution', emoji: '🍀', codes: 28 },
  { name: 'Project Mugetsu', slug: 'project-mugetsu', emoji: '⚡', codes: 4 },
  { name: 'Dragon Blox', slug: 'dragon-blox', emoji: '🐉', codes: 82 },
  { name: 'Grand Piece Online', slug: 'grand-piece-online', emoji: '🌊', codes: 3 },
  { name: 'Scroll a Brainrot', slug: 'scroll-a-brainrot', emoji: '📜', codes: 32 },
  { name: 'Spin a Brainrot', slug: 'spin-a-brainrot', emoji: '🎲', codes: 4 },
  { name: 'Be a Brainrot', slug: 'be-a-brainrot', emoji: '🧠', codes: 2 },
  { name: 'Anime Rift Tower Defense', slug: 'anime-rift-tower-defense', emoji: '⚔️', codes: 7 },
  { name: 'Doors', slug: 'doors', emoji: '🚪', codes: 31 },
  { name: 'Anime Story 2', slug: 'anime-story-2', emoji: '📖', codes: 17 },
  { name: 'Anime Rangers X', slug: 'anime-rangers-x', emoji: '🗼', codes: 6 },
  { name: 'A One Piece Game', slug: 'a-one-piece-game', emoji: '🏴‍☠️', codes: 8 },
  { name: 'Sakura Stand', slug: 'sakura-stand', emoji: '🌸', codes: 2 },
  { name: 'Untitled Attack on Titan', slug: 'untitled-attack-on-titan', emoji: '🗡️', codes: 6 },
  { name: 'Ninja Legends', slug: 'ninja-legends', emoji: '🥷', codes: 8 },
  { name: 'Arm Wrestle Simulator', slug: 'arm-wrestle-simulator', emoji: '💪', codes: 2 },
  { name: 'Strongman Simulator', slug: 'strongman-simulator', emoji: '🏋️', codes: 8 },
  { name: 'Anime Souls Simulator X', slug: 'anime-souls-simulator-x', emoji: '👹', codes: 3 },
  { name: 'Fire Force Online', slug: 'fire-force-online', emoji: '🔥', codes: 3 },
  { name: 'Skibidi Masters Tower Defense', slug: 'skibidi-masters-tower-defense', emoji: '🚽', codes: 5 },
];

function gameResultHTML(g) {
  return `
    <a class="search-result-item" href="/codes-${g.slug}.html">
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
  'steal-from-the-rich': 10753751277,
  'ride-a-pet': 10035204815,
  '1-loot-to-forge': 10684750879,
  'slayers-2': 5595353122,
  'illegal-soccer': 10155360168,
  'search-for-the-needle': 10756011174,
  'dungeon-quest-reborn': 9931749389,'anime-origins': 8946565814,
  'grow-a-chicken-fighter': 10338952197,
  'dig-and-clean': 10475794799,
  'fish-an-anime-rng': 9582986239,
  'anime-stars': 10697889407,
  'anime-expeditions': 7613921865,
  'anime-champions-simulator': 4986566693,
  'animal-hospital': 10148749921,
  'demonology': 6170143659,
  'spin-a-soccer-card': 9272693470,
  'merge-a-nuke': 10199301628,
  'vv-ultimatum': 2309918273,
  'fifa-super-soccer': 4293374620,
  'hypershot': 5995470825,
  'blockspin': 6765805766,
  'run-a-restaurant': 9970645639,
  'squid-game-x': 2936053166,
  'catch-a-monster': 9141743926,
  'brainrot-evolution': 7332711118,
  '100-days-at-sea': 9167377564,
  'anime-fighting-simulator': 10321202755,
  'mini-war': 9837612476,
  '1-aura-per-click': 10067258922,
  'steal-a-fish': 7907828295,
  'steal-an-egg': 10563114921,
  'knockout': 9384605736,
  'my-gym': 7628753636,
  'untitled-tag-game': 4864117649,
  'bloxstrike': 7633926880,
  'twenty-one': 5665954430,
  'anime-astral-simulator': 9797806474,
  'anime-battle-rng': 10140039361,
  'anime-fighters': 2324662457,
  'anime-reversal': 8966502575,
  'a-dusty-trip': 5650396773,
  'war-tycoon': 1526814825,
  'iron-soul-dungeon': 9910245722,
  'blox-monsters': 10086454767,
  'car-crushers-2': 274816972,
  'locked': 4324259364,
  'defend-ur-base-with-anime': 10111742174,
  'anime-rng': 10062593318,
  'ugc-limited': 5114363215,
  'jujutsu-shenanigans': 3508322461,
  'kick-a-lucky-block': 10004244222,
  'dandys-world': 5569032992,
  'slime-rng': 9792947201,
  'survive-zombie-arena': 9348272796,
  'attack-on-titan-revolution': 4658598196,
  'dig': 7218065222,
  'sols-rng': 5361032378,
  'jules-rng': 5800312217,
  'weapon-rng': 9495474341,
  'character-rng': 5931899687,
  'case-simulator-rng': 8829204428,
  'button-rng-2': 10103262728,
  'rng-heroes': 10153098880,
  'fish-it': 6701277882,
  'be-a-fish-bait': 9330616906,
  'anime-spirits': 4161970303,
  'slap-battles': 2380077519,
  'forsaken': 6331902150,
  'driving-empire': 1202096104,
  'evasion-clavier': 9584852943,
  'ferme-d-anneaux': 10039338037,
  'vendre-des-citrons': 7395930870,
  'world-fighters': 10032271327,
  'noob-incremental': 9965411707,
  'my-gaming-cafe': 10168229420,
  'catch-and-tame': 9091133975,
  'build-a-ring-farm': 10039338037,
  'anime-warriors-iii': 6409513651,
  'anime-squadron': 8356066619,
  'anime-card-farm': 10144587520,
  'chicken-farm': 10209534490,
  '1-mine-per-click': 10178802449,
  'world-cup-album': 10221849724,
  'storage-hunters-open-world': 10261267004,
  '1-magic-evolution': 10123898404,
  'evomon': 9826885587,
  'grow-a-garden-2': 10200395747,
  'anime-fighting-simulator-reborn': 8160272434,
  'liminalite-invisible': 9885372266,
  'demonologie': 6170143659,
  'mini-guerre': 9837612476,
  'cliqueur-phonk': 10051007039,
  'arene-de-sniper': 9534705677,
  'tour-needoh': 9874419878,
  'blox-fruits':           994732206,
  'pet-simulator-x':       2316994223,
  'adopt-me':              383310974,
  'shindo-life':           6017744795,
  'king-legacy':           1451439645,
  'murder-mystery-2':      66654135,
  'fruit-battlegrounds':   3457700596,
  'anime-adventures':      6930929888,
  'rivals':                6035872082,
  'brookhaven':            1686885941,
  'royale-high':           321778215,
  'encounters':            2918970982,
  'tower-of-hell':         703124385,
  'work-at-a-pizza-place': 47545,
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
  'haze-piece': 2644656496,
  'all-star-tower-defense': 1720936166,
  'project-slayers': 2142948266,
  'the-strongest-battlegrounds': 3808081382,
  'spongebob-tower-defense': 6594435384,
  'garden-tower-defense': 7703614594,
  'heroes-battlegrounds': 4568630521,
  'mad-city': 498490399,
  'combat-warriors': 1390601379,
  'survive-the-killer': 1489026993,
  'peroxide': 3419284255,
  'grimoires-era': 4886369361,
  'pressure': 4367208330,
  'muscle-legends': 1268927906,
  'anime-dimensions-simulator': 2655311011,
  'ro-ghoul': 380704901,
  'evade': 3647333358,
  'dragon-adventures': 1235188606,
  'car-dealership-tycoon': 605887098,
  'pls-donate': 3317679266,
  'wizard-alchemy': 10006104044,
  'restaurant-tycoon-3': 7094518649,
  'clover-retribution': 10912405603,
  'project-mugetsu': 3525075510,
  'dragon-blox': 1147304238,
  'grand-piece-online': 1730877806,
  'scroll-a-brainrot': 9063849985,
  'spin-a-brainrot': 8497165255,
  'be-a-brainrot': 9875383684,
  'anime-rift-tower-defense': 7651084572,
  'doors': 2440500124,
  'anime-story-2': 7585079192,
  'anime-rangers-x': 9774981774,
  'a-one-piece-game': 3213362013,
  'sakura-stand': 3256689155,
  'untitled-attack-on-titan': 2232507648,
  'ninja-legends': 1335695570,
  'arm-wrestle-simulator': 4582358979,
  'strongman-simulator': 2564505263,
  'anime-souls-simulator-x': 5300677688,
  'fire-force-online': 2880808628,
  'skibidi-masters-tower-defense': 5207621753,
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

  const m = location.pathname.match(/\/codes[-\/]([a-z0-9-]+)\.html/i);
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
  // Miniatures live : différées hors du chemin critique (les vraies miniatures en dur s'affichent déjà)
  if ('requestIdleCallback' in window) requestIdleCallback(loadRobloxThumbnails, { timeout: 4000 });
  else setTimeout(loadRobloxThumbnails, 2500);
  initYouTubeVideos();
  renderNewGames();
});

/* ---- Nouveaux jeux (accueil) : rendu dynamique trié par date ----
   Source unique : tableau NEW_GAMES ci-dessous. Pour mettre un jeu en avant,
   ajoute simplement une entrée en tête (date au format AAAA-MM-JJ). Les 8 plus
   récents s'affichent automatiquement ; les cartes statiques du HTML servent de
   repli SEO et sont remplacées au chargement. */
const NEW_GAMES = [
  { slug:'a-dusty-trip', name:'A Dusty Trip', codes:3, date:'2026-06-16', updated:'16 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-c7bb56c7b813baf35d1a7335ec3e48fd/480/270/Image/Webp/noFilter', desc:'Survie au volant dans un désert sans fin : ravitaille, répare et survis. 3 codes (Dusty Coins).' },
  { slug:'war-tycoon', name:'War Tycoon', codes:4, date:'2026-06-16', updated:'16 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-002e1c99ba576f8c2f015859e13c1d83/480/270/Image/Webp/noFilter', desc:'Tycoon militaire + combat : bâtis ta base, débloque chars et avions, pars en guerre. 4 codes (cash, médailles, skins).' },
  { slug:'iron-soul-dungeon', name:'Iron Soul: Dungeon', codes:11, date:'2026-06-16', updated:'16 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-6624e54164ae1e6a970c6ba71fb6776a/480/270/Image/Webp/noFilter', desc:'RPG d\'action de donjon : combats, récolte du minerai et forge des armes. 11 codes (Race Rerolls, Cave Tickets).' },
  { slug:'blox-monsters', name:'Blox Monsters', codes:5, date:'2026-06-16', updated:'16 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-b5a0ea014346723cbbb5337ee7ba4ce5/480/270/Image/Webp/noFilter', desc:'RPG de collection : capture des monstres, fais-les évoluer et bats des boss. 5 codes (fruits, rerolls, cristaux).' },
  { slug:'car-crushers-2', name:'Car Crushers 2', codes:6, date:'2026-06-16', updated:'16 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-caf6bc510c2bc241535541c8c41ddcf7/480/270/Image/Webp/noFilter', desc:'Destruction physique : broie des voitures, derby et bombe nucléaire. 6 codes (crédits, argent, Platina).' },
  { slug:'anime-rangers-x', name:'Anime Rangers X', codes:6, date:'2026-06-15', updated:'15 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-4d28b5df1bb5f24b2662f5fc0e04ac0a/480/270/Image/Webp/noFilter', desc:'Tower Defense anime : invoque tes rangers et défends contre les vagues. 6 codes (Trait Reroll, Shadow Orbs, gemmes).' },
  { slug:'a-one-piece-game', name:'A One Piece Game', codes:8, date:'2026-06-15', updated:'15 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-8d99b87bcd9b6754aab0c1ab5fe3e56e/480/270/Image/Webp/noFilter', desc:'RPG pirate inspiré de One Piece : Fruits du Démon, Haki, mers à explorer. 8 codes (boosts EXP/drop, Gems, Beli).' },
  { slug:'sakura-stand', name:'Sakura Stand', codes:2, date:'2026-07-28', updated:'28 juillet 2026', thumb:'https://tr.rbxcdn.com/180DAY-a955d8e774a7f959d3b736311a6fee60/480/270/Image/Webp/noFilter', desc:'Combat anime à Stands (JoJo, Touhou…) : farme, reroll et affronte les joueurs. 2 codes (cash, tokens, double XP).' },
  { slug:'untitled-attack-on-titan', name:'Untitled Attack on Titan', codes:6, date:'2026-06-15', updated:'15 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-52684c00ebe2aadf3de4eeaf4eb435d2/480/270/Image/Webp/noFilter', desc:'Action AoT à l\'ODM gear : tranche la nuque des Titans. 6 codes (or, gemmes).' },
  { slug:'ninja-legends', name:'Ninja Legends', codes:8, date:'2026-06-15', updated:'15 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-0616aa68474d2273776bf20eed8a8df4/480/270/Image/Webp/noFilter', desc:'Simulateur ninja culte : farme le Chi, débloque îles et rangs. 8 codes (Chi, Gems, auto-train).' },
  { slug:'arm-wrestle-simulator', name:'Arm Wrestle Simulator', codes:2, date:'2026-06-15', updated:'15 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-46cf8a65c2fb8f84e09934980e504b69/480/270/Image/Webp/noFilter', desc:'Simulateur de force : entraîne-toi et gagne au bras de fer. 2 codes (boosts ×3 de stats).' },
  { slug:'strongman-simulator', name:'Strongman Simulator', codes:8, date:'2026-06-15', updated:'15 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-2a05a4eb85791b120cd6aae26dac0724/480/270/Image/Webp/noFilter', desc:'Simulateur de musculation : soulève, gagne en force, débloque des zones. 8 codes (boosts énergie/vitesse).' },
  { slug:'anime-souls-simulator-x', name:'Anime Souls Simulator X', codes:3, date:'2026-06-15', updated:'15 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-cb95adeca9ea0a7700c5f437a3f1c668/480/270/Image/Webp/noFilter', desc:'Simulateur anime : invoque, fais évoluer et farme. 3 codes généreux (potions, shards, gold).' },
  { slug:'fire-force-online', name:'Fire Force Online', codes:3, date:'2026-06-15', updated:'15 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-b35c5d95e2eda5a074b499caabe5f779/480/270/Image/Webp/noFilter', desc:'RPG inspiré de Fire Force : gacha de générations et capacités. 3 codes (Ability Rerolls, Reroll Tokens).' },
  { slug:'skibidi-masters-tower-defense', name:'Skibidi Masters Tower Defense', codes:5, date:'2026-06-15', updated:'15 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-648b86bc997457836bbb16eb5cdad65e/480/270/Image/Webp/noFilter', desc:'Tower Defense Skibidi : invoque et améliore tes unités. 5 codes (Toilet Paper, Trait Crystals, Lucky Drops).' },
  { slug:'mini-guerre', name:'Mini-Guerre', codes:2, date:'2026-06-29', updated:'29 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-c60de7bb9807464a0564c898db8d8e62/480/270/Image/Webp/noFilter', desc:'Tycoon de stratégie militaire : bâtis ton pays, ton économie et ton armée (tanks, avions, hélicos), puis conquiers les territoires adverses. 2 codes actifs (GENERALS, DISCODOG…), vérifié chaque jour.' },
  { slug:'1-aura-per-click', name:'+1 Aura Per Click', codes:0, date:'2026-06-14', updated:'14 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-70de23fcc43733d92dd473b176a7dfd1/480/270/Image/Webp/noFilter', desc:'Clicker addictif : chaque clic donne de l\'Aura, entraîne-toi et rebirth pour de gros multiplicateurs. Codes à venir, suivi quotidien.' },
  { slug:'anime-card-farm', name:'Anime Card Farm', codes:2, date:'2026-06-30', updated:'30 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-ddbb8f3b68bef5516e2b6365d0cd08c8/480/270/Image/Webp/noFilter', desc:'Idle de cartes anime : ouvre des packs, améliore tes cartes et chasse les cartes mutées — même hors ligne. 2 codes actifs + tier list + guide.' },
  { slug:'chicken-farm', name:'Chicken Farm', codes:0, date:'2026-06-30', updated:'30 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-40884ecbf2fafe47e78befbff75cdef8/480/270/Image/Webp/noFilter', desc:'Tycoon de ferme : achète des poulets, transforme les œufs en argent et fusionne pour des poulets rares — même hors ligne. Guide + tier list.' },
  { slug:'1-mine-per-click', name:'+1 Mine Per Click', codes:0, date:'2026-06-30', updated:'30 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-7e0a7a6a606be71764918483ef5a9084/480/270/Image/Webp/noFilter', desc:'Clicker minier incrémental : entraîne ta force, creuse, améliore ta pioche et renais pour atteindre le fond. Guide + tier list des priorités.' },
  { slug:'world-cup-album', name:'World Cup Album', codes:0, date:'2026-06-30', updated:'30 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-42bab5b30fdcdf497550faf9ac97308e/480/270/Image/Webp/noFilter', desc:'Album d’autocollants façon Panini : ouvre des packs, collectionne les joueurs et complète ton album de la Coupe du monde. Guide + tier list.' },
  { slug:'storage-hunters-open-world', name:'Storage Hunters Open World', codes:0, date:'2026-06-30', updated:'30 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-d399877b4e90fba495d22ee7e9c388b8/480/270/Image/Webp/noFilter', desc:'Sim d’enchères en monde ouvert : enchéris sur des casiers, revends tes trouvailles et deviens magnat du stockage. Guide + tier list.' },
  { slug:'1-magic-evolution', name:'+1 Magic Evolution', codes:0, date:'2026-06-30', updated:'30 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-23eaddae50b790b4f2d4daf6a405e805/480/270/Image/Webp/noFilter', desc:'Simulateur incrémental magique : clique, renais (rebirth) et empile les multiplicateurs. Guide complet + tier list des priorités (pas encore de codes).' },
  { slug:'evomon', name:'Evomon', codes:4, date:'2026-06-30', updated:'30 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-23453891da7f91db1080a51d401a5499/480/270/Image/Webp/noFilter', desc:'Le carton monster-catching de Roblox façon Pokémon : capture et fais évoluer 200+ Evomons. 4 codes actifs + tier list + guide complet.' },
  { slug:'grow-a-garden-2', name:'Grow a Garden 2', codes:1, date:'2026-06-13', updated:'13 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-71ae7859135fc45f2a0e6d580572d5c0/480/270/Image/Webp/noFilter', desc:'La suite du plus gros jeu Roblox : cultive le jour, défends ton jardin du vol la nuit. Code TEAMGREENBEAN + tier list des graines.' },
  { slug:'anime-squadron', name:'Anime Squadron', codes:11, date:'2026-06-10', updated:'10 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-08ea7a58db9a3d940ad2977ffa4b85ae/480/270/Image/Webp/noFilter', desc:'Lane battler anime : invoque ta squad et défends contre les vagues et les boss. 11 codes (Gems, Trait Shards).' },
  { slug:'anime-warriors-iii', name:'Anime Warriors III', codes:0, date:'2026-06-10', updated:'10 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-8d6f44923235ed0d52df201e13a77715/480/270/Image/Webp/noFilter', desc:'RPG de summon anime : invoque des guerriers et combats des boss. Récompenses via la boîte mail.' },
  { slug:'build-a-ring-farm', name:'Build A Ring Farm', codes:9, date:'2026-06-10', updated:'10 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-5c24b09b1d9bdfa44deadb955fd8d2fb/480/270/Image/Webp/noFilter', desc:'Farm incrémental : plante, mute et revends tes cultures sur une ferme en anneaux. 9 codes (seeds, sprays).' },
  { slug:'broken-blade', name:'Broken Blade', codes:11, date:'2026-06-10', updated:'10 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-b3b88034a0ab46ab369abeab783409da/480/270/Image/Webp/noFilter', desc:'ARPG nordique sans cooldown : forge tes armes et farme le Boss Rush. 11 codes (Holy, Sky Keys).' },
  { slug:'dandys-world', name:'Dandy’s World', codes:1, date:'2026-06-10', updated:'10 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-46c53b6213dcedc7dc3738e6f20d3baa/480/270/Image/Webp/noFilter', desc:'Survie-horreur : complète les machines et fuis les Twisteds. 1 code actif (Ichor).' },
  { slug:'universal-tower-defense-x', name:'Universal Tower Defense X', codes:18, date:'2026-06-10', updated:'10 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-6f54847ff8c83474f83f01eb49b55054/480/270/Image/Webp/noFilter', desc:'Tower defense crossover : invoque tes unités et défends les vagues. 18 codes (Rerolls, Gems).' },
  { slug:'99-nights-in-the-forest', name:'99 Nights in the Forest', codes:2, date:'2026-06-10', updated:'10 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-c5215eabc21f46723f0084f99bb7622c/480/270/Image/Webp/noFilter', desc:'Survie coopérative : tiens 99 nuits face au Cerf et aux cultistes. 2 codes (gemmes).' },
  { slug:'adopt-me', name:'Adopt Me!', codes:0, date:'2026-06-10', updated:'10 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-eccebfe3d7d1f3ca377768227d829eb1/480/270/Image/Webp/noFilter', desc:'Jeu de rôle d’adoption et de trading de familiers. Pas de codes actifs actuellement.' },
  { slug:'anime-fighting-simulator-reborn', name:'Anime Fighting Simulator Reborn', codes:4, date:'2026-06-09', updated:'9 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-ad195be47fec95664c1c3176235720b2/480/270/Image/Webp/noFilter', desc:'Entraîne tes 6 stats et deviens le plus fort. 4 codes (Yen, Chikara Shards).' },
  { slug:'kick-a-lucky-block', name:'Kick a Lucky Block', codes:8, date:'2026-06-09', updated:'9 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-829dd7deb9a2a04609c27a366096f07d/480/270/Image/Webp/noFilter', desc:'Frappe des lucky blocks, collectionne pets et mutations. 8 codes actifs.' },
  { slug:'catch-and-tame', name:'Catch and Tame', codes:1, date:'2026-06-08', updated:'8 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-0d68f08d3dc380ca03a0159c40640463/480/270/Image/Webp/noFilter', desc:'Capture et apprivoise des créatures dans un monde ouvert. 1 code actif.' },
  { slug:'blue-lock-rivals', name:'Blue Lock Rivals', codes:5, date:'2026-06-08', updated:'8 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-6c3d95dac7c3d279e20cfa9ef1b27ba5/480/270/Image/Webp/noFilter', desc:'Football inspiré de Blue Lock : styles, flows et abilities. 5 codes (spins, rerolls).' }
];

function renderNewGames(){
  const grid = document.getElementById('newGamesGrid');
  if (!grid || !Array.isArray(NEW_GAMES) || !NEW_GAMES.length) return;
  const games = NEW_GAMES.slice().sort((a,b)=> (b.date||'').localeCompare(a.date||'')).slice(0, 8);
  const esc = s => String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  grid.innerHTML = games.map(g => {
    const codesLabel = g.codes > 0
      ? ('✅ ' + g.codes + ' code' + (g.codes>1?'s':'') + ' actif' + (g.codes>1?'s':''))
      : 'ℹ️ Pas de codes';
    const thumb = g.thumb || ('/images/games/' + g.slug + '.svg');
    return '<a href="/codes-' + g.slug + '.html" class="game-card">'
      + '<div class="game-card-thumb">'
      + '<img data-game="' + g.slug + '" src="' + thumb + '" onerror="this.onerror=null;this.src=\'/images/games/' + g.slug + '.svg\'" alt="' + esc(g.name) + '" loading="lazy" decoding="async" class="thumb-svg">'
      + '<span class="card-badge badge-hot">🆕 NOUVEAU</span>'
      + '</div>'
      + '<div class="game-card-body">'
      + '<div class="game-card-title">' + esc(g.name) + '</div>'
      + '<div class="game-card-meta"><span class="meta-codes">' + codesLabel + '</span><span class="meta-date">Mis à jour le ' + esc(g.updated) + '</span></div>'
      + '<div class="game-card-desc">' + esc(g.desc) + '</div>'
      + '<span class="card-cta">🎁 Voir les codes</span>'
      + '</div></a>';
  }).join('');
}
