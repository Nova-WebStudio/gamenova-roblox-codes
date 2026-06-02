@echo off
REM ============================================================
REM  GameNova – Script de deploiement Vercel
REM  Utilise npx (pas besoin d'installer Vercel globalement)
REM ============================================================

echo.
echo  ==============================
echo   GameNova ^| Deploiement Vercel
echo  ==============================
echo.

cd /d "%~dp0"
echo [OK] Dossier : %cd%
echo.

REM -- Verifier Node.js
where node >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERREUR] Node.js non trouve. Telecharge-le sur https://nodejs.org
    pause
    exit /b 1
)
for /f "tokens=*" %%v in ('node --version') do set NODE_VER=%%v
echo [OK] Node.js %NODE_VER% detecte

REM -- Verifier npx (inclus avec npm 5.2+)
where npx >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERREUR] npx non trouve. Mets a jour npm : npm install -g npm
    pause
    exit /b 1
)
echo [OK] npx disponible
echo.

REM -- Sécurité : ne jamais deployer sur nova-webstudio
if exist ".vercel\project.json" (
    findstr /c:"prj_di8Qht6PwKLMDZbSxIBAS5ibVgFk" ".vercel\project.json" >nul 2>&1
    if %errorlevel% equ 0 (
        echo [!] STOP : project.json pointe sur nova-webstudio !
        echo [!] Suppression du lien incorrect...
        rmdir /s /q ".vercel"
        echo [OK] Lien supprime.
        echo.
    )
)

REM -- Premier deploiement OU mise a jour
if not exist ".vercel\project.json" (
    echo [INFO] Premier deploiement - Vercel va creer un NOUVEAU projet.
    echo.
    echo        Reponds exactement comme ceci :
    echo        - Set up and deploy?  →  Y
    echo        - Which scope?        →  nova-webstudios-projects
    echo        - Link to existing?   →  N   ^(NOUVEAU projet^)
    echo        - Project name?       →  gamenova-roblox-codes
    echo        - Directory?          →  ./  ^(Entree^)
    echo.
    npx vercel@latest
) else (
    echo [OK] Projet deja lie. Deploiement en production...
    npx vercel@latest --prod --yes
)

echo.
echo  Termine ! Verifie : https://vercel.com/nova-webstudios-projects
echo.
pause
