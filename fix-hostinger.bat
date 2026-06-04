@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ============================================
echo   Correction du build Hostinger - Zoneblox
echo ============================================
echo.

REM 1) Retirer un eventuel verrou git bloque
if exist ".git\index.lock" (
  echo - Suppression du verrou git...
  del /f /q ".git\index.lock"
)

REM 2) Supprimer les fichiers herites de Vercel (inutiles + provoquent le build)
if exist "vercel.json" (
  echo - Suppression de vercel.json...
  del /f /q "vercel.json"
)
if exist "api" (
  echo - Suppression du dossier api...
  rmdir /s /q "api"
)

echo.
echo - Envoi vers GitHub (Hostinger deploiera automatiquement)...
git add -A
git commit -m "Retire fichiers Vercel (fix build Hostinger)"
git push origin main

echo.
echo ============================================
echo   Termine. Attends 1-2 min puis recharge
echo   le site avec Ctrl+F5.
echo ============================================
pause
