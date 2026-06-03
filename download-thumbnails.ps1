# ============================================================
#  GameNova — Téléchargement des vraies images Roblox
#  Lance ce script UNE FOIS depuis le dossier GameNova
# ============================================================

$OutputDir = "$PSScriptRoot\images\games"
New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

Write-Host "`n🎮 GameNova — Téléchargement des thumbnails Roblox" -ForegroundColor Cyan
Write-Host "=================================================" -ForegroundColor Cyan

# Universe IDs Roblox pour chaque jeu
$games = @(
    @{ slug="blox-fruits";          universeId=2753915549  },
    @{ slug="pet-simulator-x";      universeId=6284583030  },
    @{ slug="adopt-me";             universeId=920587237   },
    @{ slug="shindo-life";          universeId=6017744795  },
    @{ slug="king-legacy";          universeId=6096648965  },
    @{ slug="murder-mystery-2";     universeId=142823291   },
    @{ slug="fruit-battlegrounds";  universeId=10449761463 },
    @{ slug="anime-adventures";     universeId=7974552544  },
    @{ slug="rivals";               universeId=17017769292 },
    @{ slug="brookhaven";           universeId=4924922222  },
    @{ slug="royale-high";          universeId=735030788   },
    @{ slug="encounters";           universeId=16768148699 },
    @{ slug="tower-of-hell";        universeId=1962086868  },
    @{ slug="work-at-a-pizza-place";universeId=192800      }
)

$ids = ($games | ForEach-Object { $_.universeId }) -join ","

Write-Host "`n[1/3] Appel API Roblox Thumbnails..." -ForegroundColor Yellow

try {
    $apiUrl = "https://thumbnails.roblox.com/v1/games/icons?universeIds=$ids&size=512x512&format=Png&isCircular=false"
    $response = Invoke-RestMethod -Uri $apiUrl -Method Get -TimeoutSec 15
    Write-Host "[OK] API répondu — $($response.data.Count) images trouvées" -ForegroundColor Green
} catch {
    Write-Host "[ERREUR] API inaccessible : $_" -ForegroundColor Red
    Write-Host "Essaie avec l'API alternative..." -ForegroundColor Yellow
    # Fallback: utilise les thumbnails (bannières) au lieu des icons
    try {
        $apiUrl = "https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds=$ids&countPerUniverse=1&size=768x432&format=Png&isCircular=false"
        $response = Invoke-RestMethod -Uri $apiUrl -Method Get -TimeoutSec 15
        Write-Host "[OK] API alternative OK" -ForegroundColor Green
    } catch {
        Write-Host "[ERREUR] Les deux APIs échouent." -ForegroundColor Red
        Read-Host "Appuie sur Entrée pour quitter"
        exit
    }
}

Write-Host "`n[2/3] Téléchargement des images..." -ForegroundColor Yellow

$imageMap = @{}
foreach ($item in $response.data) {
    $imageMap[$item.targetId] = $item.imageUrl
}

$ok = 0; $fail = 0
foreach ($game in $games) {
    $imgUrl = $imageMap[$game.universeId]
    if ($imgUrl) {
        $outPath = "$OutputDir\$($game.slug).png"
        try {
            Invoke-WebRequest -Uri $imgUrl -OutFile $outPath -TimeoutSec 15 -ErrorAction Stop
            Write-Host "  ✅ $($game.slug).png" -ForegroundColor Green
            $ok++
        } catch {
            Write-Host "  ❌ $($game.slug) — $_" -ForegroundColor Red
            $fail++
        }
    } else {
        Write-Host "  ⚠️  $($game.slug) — pas d'image dans la réponse API" -ForegroundColor Yellow
        $fail++
    }
}

Write-Host "`n[3/3] Mise à jour des références HTML vers .png..." -ForegroundColor Yellow

# Met à jour tous les fichiers HTML pour utiliser .png au lieu de .svg
$htmlFiles = Get-ChildItem -Path $PSScriptRoot -Filter "*.html" -Recurse
$count = 0
foreach ($file in $htmlFiles) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    $newContent = $content -replace '/images/games/([^"]+)\.svg', '/images/games/$1.png'
    if ($newContent -ne $content) {
        Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8 -NoNewline
        Write-Host "  ✅ $($file.Name) mis à jour"
        $count++
    }
}

Write-Host "`n=================================================" -ForegroundColor Cyan
Write-Host "✅ $ok images téléchargées | ❌ $fail échouées | 📄 $count HTML mis à jour" -ForegroundColor Cyan
Write-Host "`nProchaine étape : git add . && git commit -m 'Real game thumbnails' && git push" -ForegroundColor Green
Write-Host ""
Read-Host "Appuie sur Entrée pour fermer"
