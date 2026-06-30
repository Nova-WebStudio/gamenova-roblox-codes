/* ============================================================
   Zoneblox – Main JavaScript (FR)
   ============================================================ */

const ROBLOX_THUMBS = {
  'spin-a-soccer-card': 'https://tr.rbxcdn.com/180DAY-bf53b88875889ac2f4ac48047d017b4a/480/270/Image/Webp/noFilter',
  'merge-a-nuke': 'https://tr.rbxcdn.com/180DAY-559508ad864c626f049ce0870d43665b/480/270/Image/Webp/noFilter',
  'vv-ultimatum': 'https://tr.rbxcdn.com/180DAY-a1d19383f4330a2b5e1902fdcc5f5171/480/270/Image/Webp/noFilter',
  'fifa-super-soccer': 'https://tr.rbxcdn.com/180DAY-8dbf3df11aed03b0c733d41fda2bd3a4/480/270/Image/Webp/noFilter',
  'hypershot': 'https://tr.rbxcdn.com/180DAY-e640b4e4d607ef8db910b23b7adc09f4/480/270/Image/Webp/noFilter',
  'blockspin': 'https://tr.rbxcdn.com/180DAY-d2785094a0b157d6fc654e7a3c53e5d9/480/270/Image/Webp/noFilter',
  'run-a-restaurant': 'https://tr.rbxcdn.com/180DAY-abe7f648884a7c427c69f828e51c65ce/480/270/Image/Webp/noFilter',
  'squid-game-x': 'https://tr.rbxcdn.com/180DAY-2264689de7f046b3c3df5e135abd5ffa/480/270/Image/Webp/noFilter',
  'catch-a-monster': 'https://tr.rbxcdn.com/180DAY-874bb92a4550696298e41ef059e6cb57/480/270/Image/Webp/noFilter',
  'brainrot-evolution': 'https://tr.rbxcdn.com/180DAY-fc4ce9bf5f0886c17c472d7e9b291b2d/480/270/Image/Webp/noFilter',
  '100-days-at-sea': 'https://tr.rbxcdn.com/180DAY-127dc5df1f7a770cc3831c5b4b23aaa0/480/270/Image/Webp/noFilter',
  'a-dusty-trip': 'https://tr.rbxcdn.com/180DAY-c7bb56c7b813baf35d1a7335ec3e48fd/480/270/Image/Webp/noFilter',
  'war-tycoon': 'https://tr.rbxcdn.com/180DAY-002e1c99ba576f8c2f015859e13c1d83/480/270/Image/Webp/noFilter',
  'iron-soul-dungeon': 'https://tr.rbxcdn.com/180DAY-6624e54164ae1e6a970c6ba71fb6776a/480/270/Image/Webp/noFilter',
  'blox-monsters': 'https://tr.rbxcdn.com/180DAY-b5a0ea014346723cbbb5337ee7ba4ce5/480/270/Image/Webp/noFilter',
  'car-crushers-2': 'https://tr.rbxcdn.com/180DAY-caf6bc510c2bc241535541c8c41ddcf7/480/270/Image/Webp/noFilter',
  'steal-a-fish': 'https://tr.rbxcdn.com/180DAY-ed927450771fe3f6c356b5aacbb5efeb/480/270/Image/Webp/noFilter',
  'knockout': 'https://tr.rbxcdn.com/180DAY-f75a05b251c9fdb0c762a3bd997a2901/480/270/Image/Webp/noFilter',
  'my-gym': 'https://tr.rbxcdn.com/180DAY-c128e1ea9f3b870b4f2202bcefdbed8d/480/270/Image/Webp/noFilter',
  'untitled-tag-game': 'https://tr.rbxcdn.com/180DAY-cd834c110aa147df9bc89a79fece32ea/480/270/Image/Webp/noFilter',
  'bloxstrike': 'https://tr.rbxcdn.com/180DAY-38303ae0318ee323f54accc54d368609/480/270/Image/Webp/noFilter',
  'twenty-one': 'https://tr.rbxcdn.com/180DAY-20b1ac2eb8792c3d1d2b51a02ce6582d/480/270/Image/Webp/noFilter',
  'anime-astral-simulator': 'https://tr.rbxcdn.com/180DAY-779a6a4dd29ae6ddfa5c3e94b80c1735/480/270/Image/Webp/noFilter',
  'anime-battle-rng': 'https://tr.rbxcdn.com/180DAY-35864a4019d8f2c8506d114fcf24fc9d/480/270/Image/Webp/noFilter',
  'anime-fighters': 'https://tr.rbxcdn.com/180DAY-44435f032652f720d2760df1c023c472/480/270/Image/Webp/noFilter',
  'anime-fighting-simulator': 'https://tr.rbxcdn.com/180DAY-7f8e62f51167c90177bdd9d4d9476e33/768/432/Image/Png/noFilter',
  'anime-reversal': 'https://tr.rbxcdn.com/180DAY-0c85047a311b57cf6204a6f08e8f703c/480/270/Image/Webp/noFilter',
  'locked': 'https://tr.rbxcdn.com/180DAY-d25adedff694e3710158bf33115397bf/480/270/Image/Webp/noFilter',
  'defend-ur-base-with-anime': 'https://tr.rbxcdn.com/180DAY-5610a932c392b232214df24d7b73480d/480/270/Image/Webp/noFilter',
  'anime-rng': 'https://tr.rbxcdn.com/180DAY-cb52cb46f7586ef2c76773ae5ca17e0b/480/270/Image/Webp/noFilter',
  'ugc-limited': 'https://tr.rbxcdn.com/180DAY-4c03c829dd96b8bd973dab28a0dd7f8a/480/270/Image/Webp/noFilter',
  'jujutsu-shenanigans': 'https://tr.rbxcdn.com/180DAY-e27277bbda2ba2efdb47a1863df2da3d/512/512/Image/Png/noFilter',
  'kick-a-lucky-block': 'https://tr.rbxcdn.com/180DAY-3c320528b9f19497a76e238276cdeb53/512/512/Image/Png/noFilter',
  'dandys-world': 'https://tr.rbxcdn.com/180DAY-dd5fef14c5a000dba3bebfb71cf4ac64/512/512/Image/Png/noFilter',
  'slime-rng': 'https://tr.rbxcdn.com/180DAY-b3e07872193b7de060e80e2b300a94ca/480/270/Image/Webp/noFilter',
  'survive-zombie-arena': 'https://tr.rbxcdn.com/180DAY-ccfc78577119d3c8ed223f580e05f222/512/512/Image/Png/noFilter',
  'attack-on-titan-revolution': 'https://tr.rbxcdn.com/180DAY-b5b0d5438b8f70eca4dc9311ac541afc/512/512/Image/Png/noFilter',
  'broken-blade': 'https://tr.rbxcdn.com/180DAY-b4137b1c3b07478b27e38a7ee8356800/500/280/Image/Jpeg/noFilter',
  'sailor-piece': 'https://tr.rbxcdn.com/180DAY-b405eb9a7be185d2a560f8857d82fec7/500/280/Image/Jpeg/noFilter',
  'anime-apocalypse': 'https://tr.rbxcdn.com/180DAY-45c04a57026f120497361440a566ee2e/500/280/Image/Jpeg/noFilter',
  'anime-eternal': 'https://tr.rbxcdn.com/180DAY-f755ba09b84bf157f5b4b35b6a8af4c0/500/280/Image/Jpeg/noFilter',
  'universal-tower-defense-x': 'https://tr.rbxcdn.com/180DAY-d7a465629ce61d0dff9fe7b5b11c7d03/500/280/Image/Jpeg/noFilter',
  'dig': 'https://tr.rbxcdn.com/180DAY-38334daf4b8073ee8d3d9976dfc7bfe8/480/270/Image/Webp/noFilter',
  'sols-rng': 'https://tr.rbxcdn.com/180DAY-8965d16c1ee802fff15f681cae4b413e/480/270/Image/Webp/noFilter',
  'fish-it': 'https://tr.rbxcdn.com/180DAY-dfd35b1d04259ea9974c2ee8bcd9ed49/500/280/Image/Jpeg/noFilter',
  'anime-spirits': 'https://tr.rbxcdn.com/180DAY-90d479b01af3f1ed17af3643f447e915/480/270/Image/Webp/noFilter',
  'slap-battles': 'https://tr.rbxcdn.com/180DAY-01bb43634d02e38923c1543a029c95d5/480/270/Image/Webp/noFilter',
  'forsaken': 'https://tr.rbxcdn.com/180DAY-242c4d76325c453886b3382d825eb71c/500/280/Image/Jpeg/noFilter',
  'driving-empire': 'https://tr.rbxcdn.com/180DAY-134d852037dc6df76cd340199bc0eef7/480/270/Image/Webp/noFilter',
  'evasion-clavier': 'https://tr.rbxcdn.com/180DAY-82b559d4f2bd68f909d4b9bdd92d168e/480/270/Image/Webp/noFilter',
  'ferme-d-anneaux': 'https://tr.rbxcdn.com/180DAY-5c24b09b1d9bdfa44deadb955fd8d2fb/480/270/Image/Webp/noFilter',
  'vendre-des-citrons': 'https://tr.rbxcdn.com/180DAY-3bb611c1f3b4d5bfa396b1ae965134af/480/270/Image/Webp/noFilter',
  'world-fighters': 'https://tr.rbxcdn.com/180DAY-81425ab9ff608a7dbffc828b101e9583/480/270/Image/Webp/noFilter',
  'noob-incremental': 'https://tr.rbxcdn.com/180DAY-8273fdf7d5a9074bc47861d7719c5392/480/270/Image/Webp/noFilter',
  'my-gaming-cafe': 'https://tr.rbxcdn.com/180DAY-db6f62117bb769ae9f2a3ebe39e1f6c0/480/270/Image/Webp/noFilter',
  'catch-and-tame': 'https://tr.rbxcdn.com/180DAY-0d68f08d3dc380ca03a0159c40640463/480/270/Image/Webp/noFilter',
  'build-a-ring-farm': 'https://tr.rbxcdn.com/180DAY-5c24b09b1d9bdfa44deadb955fd8d2fb/480/270/Image/Webp/noFilter',
  'anime-warriors-iii': 'https://tr.rbxcdn.com/180DAY-8d6f44923235ed0d52df201e13a77715/480/270/Image/Webp/noFilter',
  'anime-squadron': 'https://tr.rbxcdn.com/180DAY-08ea7a58db9a3d940ad2977ffa4b85ae/480/270/Image/Webp/noFilter',
  'evomon': 'https://tr.rbxcdn.com/180DAY-23453891da7f91db1080a51d401a5499/480/270/Image/Webp/noFilter',
  'grow-a-garden-2': 'https://tr.rbxcdn.com/180DAY-71ae7859135fc45f2a0e6d580572d5c0/480/270/Image/Webp/noFilter',
  'mini-war': 'https://tr.rbxcdn.com/180DAY-2cb3c3df52a1e53d9b93f66fab87a861/480/270/Image/Webp/noFilter',
  '1-aura-per-click': 'https://tr.rbxcdn.com/180DAY-70de23fcc43733d92dd473b176a7dfd1/480/270/Image/Webp/noFilter',
  'anime-fighting-simulator-reborn': 'https://tr.rbxcdn.com/180DAY-ad195be47fec95664c1c3176235720b2/480/270/Image/Webp/noFilter',
  'liminalite-invisible': 'https://tr.rbxcdn.com/180DAY-3d5bc95ea145c6be0d992c91c173ef1e/480/270/Image/Webp/noFilter',
  'demonologie': 'https://tr.rbxcdn.com/180DAY-4a405de12e9812c5b154529146d0ea13/480/270/Image/Webp/noFilter',
  'mini-guerre': 'https://tr.rbxcdn.com/180DAY-c60de7bb9807464a0564c898db8d8e62/480/270/Image/Webp/noFilter',
  'cliqueur-phonk': 'https://tr.rbxcdn.com/180DAY-ae08f34ff73b587272264895a4e43bae/480/270/Image/Webp/noFilter',
  'arene-de-sniper': 'https://tr.rbxcdn.com/180DAY-e59b96a0c52acd94af855698abc72767/480/270/Image/Webp/noFilter',
  'tour-needoh': 'https://tr.rbxcdn.com/180DAY-709282c91d3fb74801b493d7987004b3/480/270/Image/Webp/noFilter',
  'blox-fruits': 'https://tr.rbxcdn.com/180DAY-e1ce51abae5188805c3fee78ec7f4d08/480/270/Image/Webp/noFilter',
  'pet-simulator-x': 'https://tr.rbxcdn.com/180DAY-a7bb14d2b3dbf586e67ba2ac7a0c3dc7/500/280/Image/Jpeg/noFilter',
  'adopt-me': 'https://tr.rbxcdn.com/180DAY-ef30533fcd5e71af2468030ffa6c176a/500/280/Image/Jpeg/noFilter',
  'murder-mystery-2': 'https://tr.rbxcdn.com/180DAY-5ba706807447783862364dfef7a465ff/500/280/Image/Jpeg/noFilter',
  'royale-high': 'https://tr.rbxcdn.com/180DAY-1c63d3971f06391b08a95400cdf2bb78/500/280/Image/Jpeg/noFilter',
  'brookhaven': 'https://tr.rbxcdn.com/180DAY-5e77d217cbda7ba5941840cfa3ab8c36/480/270/Image/Webp/noFilter',
  'tower-of-hell': 'https://tr.rbxcdn.com/180DAY-20a372111085c33de1e64004e4dca1d8/480/270/Image/Webp/noFilter',
  'work-at-a-pizza-place': 'https://tr.rbxcdn.com/180DAY-3504f0abedb16721aec2f8fcc0da4e2e/480/270/Image/Webp/noFilter',
  'shindo-life': 'https://t3.rbxcdn.com/180DAY-3b2ec062707376a89a223ea44c20d408',
  'king-legacy': 'https://tr.rbxcdn.com/180DAY-505d0cc614022636a562fd3ff8808ba0/480/270/Image/Webp/noFilter',
  'anime-adventures': 'https://t3.rbxcdn.com/180DAY-58d59bfe7584647d43085d18c3e9d679',
  'fruit-battlegrounds': 'https://tr.rbxcdn.com/180DAY-6688078543e2f947bf998f31c4601037/480/270/Image/Webp/noFilter',
  'rivals': 'https://tr.rbxcdn.com/180DAY-27507ba164fae9b46c68047d34d0078b/480/270/Image/Webp/noFilter',
  'encounters': 'https://tr.rbxcdn.com/180DAY-024bcafc4df055789126ae841598d15d/480/270/Image/Webp/noFilter',
  'grow-a-garden': 'https://tr.rbxcdn.com/180DAY-028e7742f4ef789f654bf0dd91502b41/480/270/Image/Webp/noFilter',
  'blade-ball': 'https://tr.rbxcdn.com/180DAY-aa0679c96e6ce33f961087cebcc07ce6/480/270/Image/Webp/noFilter',
  'anime-defenders': 'https://tr.rbxcdn.com/180DAY-c5a2289b4baf7194add46247482074d7/480/270/Image/Webp/noFilter',
  'toilet-tower-defense': 'https://tr.rbxcdn.com/180DAY-5a9d6ca7af3e521497366c956bbbea05/480/270/Image/Webp/noFilter',
  'pet-simulator-99': 'https://tr.rbxcdn.com/180DAY-b7b8ad3ad6f4103c91efc25da7bc1118/480/270/Image/Webp/noFilter',
  'bee-swarm-simulator': 'https://tr.rbxcdn.com/180DAY-315e29556054777604420711cb64f0b6/480/270/Image/Webp/noFilter',
  'anime-vanguards': 'https://tr.rbxcdn.com/180DAY-cb38398e8a1315ca4046f168c7504d6b/480/270/Image/Webp/noFilter',
  'arsenal': 'https://tr.rbxcdn.com/180DAY-fd5d29ef7df403915891862d02ae09bb/480/270/Image/Webp/noFilter',
  'jailbreak': 'https://tr.rbxcdn.com/180DAY-fef285ce1b8ac805b17da2a4f998ccec/480/270/Image/Webp/noFilter',
  'bedwars': 'https://tr.rbxcdn.com/180DAY-9e34b6ee9e93b7840f82d1381d14c641/480/270/Image/Webp/noFilter',
  'fisch': 'https://tr.rbxcdn.com/180DAY-0b48b36aaaebb05f29da4beb58790100/480/270/Image/Webp/noFilter',
  'dress-to-impress': 'https://tr.rbxcdn.com/180DAY-62de69073c3ab87818fa79cd9d34006b/480/270/Image/Webp/noFilter',
  'da-hood': 'https://tr.rbxcdn.com/180DAY-655a8b7fc990b48f595db9bcfd7ea70b/480/270/Image/Webp/noFilter',
  'bubble-gum-simulator-infinity': 'https://tr.rbxcdn.com/180DAY-7c76a88ace2e799826837aee08875eec/480/270/Image/Webp/noFilter',
  'blue-lock-rivals': 'https://tr.rbxcdn.com/180DAY-6c3d95dac7c3d279e20cfa9ef1b27ba5/480/270/Image/Webp/noFilter',
  'volleyball-legends': 'https://tr.rbxcdn.com/180DAY-572cf4e9e5cec5dd45074a98fa143ca0/480/270/Image/Webp/noFilter',
  'steal-a-brainrot': 'https://tr.rbxcdn.com/180DAY-64170d84ffa0cba4ee5af8bd1cd2df66/480/270/Image/Webp/noFilter',
  'build-a-boat-for-treasure': 'https://tr.rbxcdn.com/180DAY-1ca8115eb50594d19be488f3d22ac54e/480/270/Image/Webp/noFilter',
  'anime-last-stand': 'https://tr.rbxcdn.com/180DAY-b3d29df4d10633c51bd9d2a5b6585bde/480/270/Image/Webp/noFilter',
  '99-nights-in-the-forest': 'https://tr.rbxcdn.com/180DAY-c5215eabc21f46723f0084f99bb7622c/480/270/Image/Webp/noFilter',
  'plants-vs-brainrots': 'https://tr.rbxcdn.com/180DAY-2ac6fe0e69b8567ab69bc3ca5a2482a0/480/270/Image/Webp/noFilter',
  'dead-rails': 'https://tr.rbxcdn.com/180DAY-da525289338642275e4838a07d685e93/480/270/Image/Webp/noFilter',
  'jujutsu-infinite': 'https://tr.rbxcdn.com/180DAY-243b2323af958a373c24bb885e2986b5/500/280/Image/Jpeg/noFilter',
  'anime-reborn': 'https://tr.rbxcdn.com/180DAY-8b81be86b8e67cbc4db3d07b846ad7c1/500/280/Image/Jpeg/noFilter',
  'untitled-boxing-game': 'https://tr.rbxcdn.com/180DAY-5e814dc6b0ad9489cc40c4dbf9bb7d96/480/270/Image/Webp/noFilter',
  'type-soul': 'https://tr.rbxcdn.com/180DAY-8a0cfb06021a3b7813f79e9f9e6eb1b1/480/270/Image/Webp/noFilter',
  'basketball-zero': 'https://tr.rbxcdn.com/180DAY-0d7d35bbb03eca85b0bfcb0076a0435a/480/270/Image/Webp/noFilter',
  'haze-piece': 'https://tr.rbxcdn.com/180DAY-41212ff0c4a4a7105b2e1605f3666243/500/280/Image/Jpeg/noFilter',
  'all-star-tower-defense': 'https://tr.rbxcdn.com/180DAY-9fbd50db5a51699b733c9529ee542d19/480/270/Image/Webp/noFilter',
  'anime-champions-simulator': 'https://tr.rbxcdn.com/180DAY-9d4be137161ea266ba1c2c6f28832e21/480/270/Image/Webp/noFilter',
  'animal-hospital': 'https://tr.rbxcdn.com/180DAY-db27bdc698b088f2d8352327f7dc64f6/480/270/Image/Png/noFilter',
  'demonology': 'https://tr.rbxcdn.com/180DAY-2651cff28f8766658687d6df2067bf03/480/270/Image/Png/noFilter',
  'sonic-speed-simulator': 'https://tr.rbxcdn.com/180DAY-82939a396600a61e4abadd92664f8d83/480/270/Image/Webp/noFilter',
  'tower-defense-simulator': 'https://tr.rbxcdn.com/180DAY-f4a7603e22db5d7a43e966fe145a96e1/480/270/Image/Webp/noFilter',
  'project-slayers': 'https://tr.rbxcdn.com/180DAY-612b92100da817e8dc2bb8fd35ce117e/480/270/Image/Webp/noFilter',
  'the-strongest-battlegrounds': 'https://tr.rbxcdn.com/180DAY-c947df5b221c30672c3591247a8c6495/480/270/Image/Webp/noFilter',
  'spongebob-tower-defense': 'https://tr.rbxcdn.com/180DAY-c3a62fcdf7e0a60cd52456d65f267689/480/270/Image/Webp/noFilter',
  'garden-tower-defense': 'https://tr.rbxcdn.com/180DAY-ad6eccabf36c9174c02fed274ca4b5a9/480/270/Image/Webp/noFilter',
  'heroes-battlegrounds': 'https://tr.rbxcdn.com/180DAY-05b3d7fb729835a6f28de0067fac79cd/480/270/Image/Webp/noFilter',
  'mad-city': 'https://tr.rbxcdn.com/180DAY-e03eb43e97fb7031d8187b808fd7ff27/480/270/Image/Webp/noFilter',
  'combat-warriors': 'https://tr.rbxcdn.com/180DAY-a631d6d73730a77f93b02eb3b0e8b06c/480/270/Image/Webp/noFilter',
  'survive-the-killer': 'https://tr.rbxcdn.com/180DAY-4f30b695e340b41799ff15643fff9795/480/270/Image/Webp/noFilter',
  'peroxide': 'https://tr.rbxcdn.com/180DAY-be9eec5f81d445dea3b3e0971411dd2b/500/280/Image/Jpeg/noFilter',
  'grimoires-era': 'https://tr.rbxcdn.com/180DAY-4ecd0b70b1defc6a712348e3c0230be2/500/280/Image/Jpeg/noFilter',
  'pressure': 'https://tr.rbxcdn.com/180DAY-5b1179410249512e675aafa90e4fe1e0/500/280/Image/Jpeg/noFilter',
  'muscle-legends': 'https://tr.rbxcdn.com/180DAY-3a8fdfdb456058592c8a64bef231c27a/500/280/Image/Jpeg/noFilter',
  'anime-dimensions-simulator': 'https://tr.rbxcdn.com/180DAY-cd6f5a5f32c24fc32e1813f8213338da/500/280/Image/Jpeg/noFilter',
  'ro-ghoul': 'https://tr.rbxcdn.com/180DAY-114fec0205e2c92fd880fd3aa95777dd/500/280/Image/Jpeg/noFilter',
  'evade': 'https://tr.rbxcdn.com/180DAY-bf95a86e5f5e37bf61a5f33401e95deb/512/512/Image/Png/noFilter',
  'dragon-adventures': 'https://tr.rbxcdn.com/180DAY-be3b9158d0827a1a5f9ac66c51888b26/512/512/Image/Png/noFilter',
  'car-dealership-tycoon': 'https://tr.rbxcdn.com/180DAY-2f49b71e385206d055e54562a79f4b81/512/512/Image/Png/noFilter',
  'pls-donate': 'https://tr.rbxcdn.com/180DAY-a8c2faf226f0d89bed86a7d5e9683789/512/512/Image/Png/noFilter',
  'wizard-alchemy': 'https://tr.rbxcdn.com/180DAY-9446c5c0b8ba7bdc6ed1ed6de1ed5c7a/512/512/Image/Png/noFilter',
  'restaurant-tycoon-3': 'https://tr.rbxcdn.com/180DAY-5537cbddeaee05dea19e0cbf8f452353/512/512/Image/Png/noFilter',
  'clover-retribution': 'https://tr.rbxcdn.com/180DAY-d99b5a21020011e2bef430a352b3fa4b/500/280/Image/Jpeg/noFilter',
  'project-mugetsu': 'https://tr.rbxcdn.com/180DAY-45c83a7355a6e29a684259c12859f40e/500/280/Image/Jpeg/noFilter',
  'dragon-blox': 'https://tr.rbxcdn.com/180DAY-87109cd7f93a982280ded36484b331f4/480/270/Image/Webp/noFilter',
  'grand-piece-online': 'https://tr.rbxcdn.com/180DAY-5dfa86c9bab8fb4f1641f42ce7b55c17/500/280/Image/Jpeg/noFilter',
  'scroll-a-brainrot': 'https://tr.rbxcdn.com/180DAY-73e66eb0f5210e6f36122f97eb56087e/500/280/Image/Jpeg/noFilter',
  'spin-a-brainrot': 'https://tr.rbxcdn.com/180DAY-7eaffb90de4c49dfd86ff4c518e7a12a/480/270/Image/Webp/noFilter',
  'be-a-brainrot': 'https://tr.rbxcdn.com/180DAY-c41e9a9b4678a149f1fc9f9f6a737d9e/480/270/Image/Webp/noFilter',
  'anime-rift-tower-defense': 'https://tr.rbxcdn.com/180DAY-000826b5aefec382cc3367192cdb5c2f/768/432/Image/Png/noFilter',
  'doors': 'https://tr.rbxcdn.com/180DAY-09f0d9b97f35839568ec129016b18485/480/270/Image/Webp/noFilter',
  'anime-story-2': 'https://tr.rbxcdn.com/180DAY-30f248b0e384d42583a14688f1df6bf8/480/270/Image/Webp/noFilter',
  'anime-rangers-x': 'https://tr.rbxcdn.com/180DAY-4d28b5df1bb5f24b2662f5fc0e04ac0a/480/270/Image/Webp/noFilter',
  'a-one-piece-game': 'https://tr.rbxcdn.com/180DAY-8d99b87bcd9b6754aab0c1ab5fe3e56e/480/270/Image/Webp/noFilter',
  'sakura-stand': 'https://tr.rbxcdn.com/180DAY-a955d8e774a7f959d3b736311a6fee60/480/270/Image/Webp/noFilter',
  'untitled-attack-on-titan': 'https://tr.rbxcdn.com/180DAY-52684c00ebe2aadf3de4eeaf4eb435d2/480/270/Image/Webp/noFilter',
  'ninja-legends': 'https://tr.rbxcdn.com/180DAY-0616aa68474d2273776bf20eed8a8df4/480/270/Image/Webp/noFilter',
  'arm-wrestle-simulator': 'https://tr.rbxcdn.com/180DAY-46cf8a65c2fb8f84e09934980e504b69/480/270/Image/Webp/noFilter',
  'strongman-simulator': 'https://tr.rbxcdn.com/180DAY-2a05a4eb85791b120cd6aae26dac0724/480/270/Image/Webp/noFilter',
  'anime-souls-simulator-x': 'https://tr.rbxcdn.com/180DAY-cb95adeca9ea0a7700c5f437a3f1c668/480/270/Image/Webp/noFilter',
  'fire-force-online': 'https://tr.rbxcdn.com/180DAY-b35c5d95e2eda5a074b499caabe5f779/480/270/Image/Webp/noFilter',
  'skibidi-masters-tower-defense': 'https://tr.rbxcdn.com/180DAY-648b86bc997457836bbb16eb5cdad65e/480/270/Image/Webp/noFilter',
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
  { name: "Sol's RNG", slug: 'sols-rng', emoji: '🎲', codes: 8 },
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
  { name: 'Sakura Stand', slug: 'sakura-stand', emoji: '🌸', codes: 8 },
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
  'fish-it': 6701277882,
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
  'evomon': 9826885587,
  'grow-a-garden-2': 10200395747,
  'anime-fighting-simulator-reborn': 8160272434,
  'liminalite-invisible': 9885372266,
  'demonologie': 6170143659,
  'mini-guerre': 9837612476,
  'cliqueur-phonk': 10051007039,
  'arene-de-sniper': 9534705677,
  'tour-needoh': 9874419878,
  'blox-fruits':           2753915549,
  'pet-simulator-x':       6284583030,
  'adopt-me':              920587237,
  'shindo-life':           6017744795,
  'king-legacy':           1451439645,
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
  'haze-piece': 2644656496,
  'all-star-tower-defense': 4996049426,
  'project-slayers': 5956785391,
  'the-strongest-battlegrounds': 10449761463,
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
  'ro-ghoul': 914010731,
  'evade': 3647333358,
  'dragon-adventures': 1235188606,
  'car-dealership-tycoon': 605887098,
  'pls-donate': 3317679266,
  'wizard-alchemy': 10006104044,
  'restaurant-tycoon-3': 7094518649,
  'clover-retribution': 10912405603,
  'project-mugetsu': 9447079542,
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
  { slug:'sakura-stand', name:'Sakura Stand', codes:8, date:'2026-06-15', updated:'15 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-a955d8e774a7f959d3b736311a6fee60/480/270/Image/Webp/noFilter', desc:'Combat anime à Stands (JoJo, Touhou…) : farme, reroll et affronte les joueurs. 8 codes (cash, tokens, double XP).' },
  { slug:'untitled-attack-on-titan', name:'Untitled Attack on Titan', codes:6, date:'2026-06-15', updated:'15 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-52684c00ebe2aadf3de4eeaf4eb435d2/480/270/Image/Webp/noFilter', desc:'Action AoT à l\'ODM gear : tranche la nuque des Titans. 6 codes (or, gemmes).' },
  { slug:'ninja-legends', name:'Ninja Legends', codes:8, date:'2026-06-15', updated:'15 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-0616aa68474d2273776bf20eed8a8df4/480/270/Image/Webp/noFilter', desc:'Simulateur ninja culte : farme le Chi, débloque îles et rangs. 8 codes (Chi, Gems, auto-train).' },
  { slug:'arm-wrestle-simulator', name:'Arm Wrestle Simulator', codes:2, date:'2026-06-15', updated:'15 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-46cf8a65c2fb8f84e09934980e504b69/480/270/Image/Webp/noFilter', desc:'Simulateur de force : entraîne-toi et gagne au bras de fer. 2 codes (boosts ×3 de stats).' },
  { slug:'strongman-simulator', name:'Strongman Simulator', codes:8, date:'2026-06-15', updated:'15 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-2a05a4eb85791b120cd6aae26dac0724/480/270/Image/Webp/noFilter', desc:'Simulateur de musculation : soulève, gagne en force, débloque des zones. 8 codes (boosts énergie/vitesse).' },
  { slug:'anime-souls-simulator-x', name:'Anime Souls Simulator X', codes:3, date:'2026-06-15', updated:'15 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-cb95adeca9ea0a7700c5f437a3f1c668/480/270/Image/Webp/noFilter', desc:'Simulateur anime : invoque, fais évoluer et farme. 3 codes généreux (potions, shards, gold).' },
  { slug:'fire-force-online', name:'Fire Force Online', codes:3, date:'2026-06-15', updated:'15 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-b35c5d95e2eda5a074b499caabe5f779/480/270/Image/Webp/noFilter', desc:'RPG inspiré de Fire Force : gacha de générations et capacités. 3 codes (Ability Rerolls, Reroll Tokens).' },
  { slug:'skibidi-masters-tower-defense', name:'Skibidi Masters Tower Defense', codes:5, date:'2026-06-15', updated:'15 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-648b86bc997457836bbb16eb5cdad65e/480/270/Image/Webp/noFilter', desc:'Tower Defense Skibidi : invoque et améliore tes unités. 5 codes (Toilet Paper, Trait Crystals, Lucky Drops).' },
  { slug:'mini-guerre', name:'Mini-Guerre', codes:2, date:'2026-06-29', updated:'29 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-c60de7bb9807464a0564c898db8d8e62/480/270/Image/Webp/noFilter', desc:'Tycoon de stratégie militaire : bâtis ton pays, ton économie et ton armée (tanks, avions, hélicos), puis conquiers les territoires adverses. 2 codes actifs (GENERALS, DISCODOG…), vérifié chaque jour.' },
  { slug:'1-aura-per-click', name:'+1 Aura Per Click', codes:0, date:'2026-06-14', updated:'14 juin 2026', thumb:'https://tr.rbxcdn.com/180DAY-70de23fcc43733d92dd473b176a7dfd1/480/270/Image/Webp/noFilter', desc:'Clicker addictif : chaque clic donne de l\'Aura, entraîne-toi et rebirth pour de gros multiplicateurs. Codes à venir, suivi quotidien.' },
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
    return '<a href="/codes/' + g.slug + '.html" class="game-card">'
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
