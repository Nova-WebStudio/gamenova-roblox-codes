# ============================================================
#  GameNova – Deploiement Vercel (PowerShell)
#  Projet : gamenova-roblox-codes  |  NE TOUCHE PAS nova-webstudio
# ============================================================

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

Write-Host ""
Write-Host "==============================" -ForegroundColor Cyan
Write-Host "  GameNova | Deploiement Vercel" -ForegroundColor Cyan
Write-Host "==============================" -ForegroundColor Cyan
Write-Host ""

# -- Verifier Node.js
try {
    $nodeVer = node --version
    Write-Host "[OK] Node.js $nodeVer detecte" -ForegroundColor Green
} catch {
    Write-Host "[ERREUR] Node.js introuvable. Telecharge : https://nodejs.org" -ForegroundColor Red
    Read-Host "Appuie sur Entree pour quitter"
    exit 1
}

# -- Verifier le projet lie (ne pas toucher nova-webstudio)
$projectFile = ".vercel\project.json"
if (Test-Path $projectFile) {
    $proj = Get-Content $projectFile | ConvertFrom-Json
    Write-Host "[OK] Projet lie : $($proj.projectName)" -ForegroundColor Green
    Write-Host "     Project ID : $($proj.projectId)" -ForegroundColor Gray

    # Securite : bloquer si c'est nova-webstudio
    if ($proj.projectId -eq "prj_di8Qht6PwKLMDZbSxIBAS5ibVgFk") {
        Write-Host ""
        Write-Host "[STOP] Ce projet pointe sur nova-webstudio !" -ForegroundColor Red
        Write-Host "       Supprime le dossier .vercel\ et relance ce script." -ForegroundColor Red
        Read-Host "Appuie sur Entree pour quitter"
        exit 1
    }
} else {
    Write-Host "[INFO] Aucun projet lie. Vercel va creer gamenova-roblox-codes." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Deploiement en cours..." -ForegroundColor Cyan
Write-Host ""

# -- Deployer avec npx (pas besoin d'installation globale)
try {
    npx vercel@latest --prod --yes
    Write-Host ""
    Write-Host "[SUCCES] GameNova deploye en production !" -ForegroundColor Green
    Write-Host "Dashboard : https://vercel.com/nova-webstudios-projects/gamenova-roblox-codes" -ForegroundColor Cyan
} catch {
    Write-Host ""
    Write-Host "[ERREUR] Deploiement echoue :" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
}

Write-Host ""
Read-Host "Appuie sur Entree pour fermer"
