@echo off
REM ============================================================
REM  GameNova – Initialisation Git + Premier push GitHub
REM  A lancer UNE SEULE FOIS depuis le dossier GameNova
REM ============================================================

cd /d "%~dp0"
echo.
echo  ================================
echo   GameNova - Configuration Git
echo  ================================
echo.

REM -- Verifier Git
where git >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERREUR] Git non installe.
    echo          Telecharge-le sur : https://git-scm.com/download/win
    pause & exit /b 1
)
echo [OK] Git detecte.
echo.

REM -- URL du repo GitHub
set /p REPO_URL="Colle l'URL de ton repo GitHub (ex: https://github.com/tonuser/gamenova-roblox-codes.git) : "

if "%REPO_URL%"=="" (
    echo [ERREUR] URL vide.
    pause & exit /b 1
)

REM -- Init git si pas encore fait
if not exist ".git" (
    echo.
    echo [INFO] Initialisation du depot Git...
    git init
    git branch -M main
)

REM -- Config utilisateur si besoin
git config user.email >nul 2>&1
if %errorlevel% neq 0 (
    set /p GIT_EMAIL="Ton email GitHub : "
    set /p GIT_NAME="Ton nom GitHub : "
    git config --global user.email "%GIT_EMAIL%"
    git config --global user.name "%GIT_NAME%"
)

REM -- Ajouter remote
git remote remove origin >nul 2>&1
git remote add origin %REPO_URL%
echo [OK] Remote GitHub configure.

REM -- Premier commit
echo.
echo [INFO] Ajout des fichiers...
git add .
git commit -m "Initial commit - GameNova Roblox Codes Site"

REM -- Push
echo.
echo [INFO] Push vers GitHub...
git push -u origin main

echo.
echo  ================================
echo   Fait ! Prochaines etapes :
echo   1. Va sur GitHub ^> Settings ^> Secrets
echo   2. Ajoute les 3 secrets FTP Hostinger
echo   3. Chaque git push deployera automatiquement
echo  ================================
echo.
pause
