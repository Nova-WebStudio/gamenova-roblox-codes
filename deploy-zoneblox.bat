@echo off
REM ============================================================
REM  Deploiement automatique ZoneBlox
REM  Commit + push uniquement s'il y a des changements.
REM  Utilise les identifiants Git deja en cache sous Windows.
REM ============================================================
cd /d "C:\Users\peter\Documents\Claude\Projects\GameNova"

REM Nettoie un eventuel verrou git reste coince
if exist ".git\index.lock" del /f /q ".git\index.lock"

REM Prepare tous les changements
git add -A

REM S'il n'y a rien a committer, on s'arrete (pas de commit vide)
git diff --cached --quiet
if %errorlevel%==0 (
  echo [%date% %time%] Aucun changement - rien a deployer.>> deploy-log.txt
  exit /b 0
)

REM Commit + push
git commit -m "MAJ Zoneblox auto (%date%)" >> deploy-log.txt 2>&1
git push origin main >> deploy-log.txt 2>&1
if %errorlevel%==0 (
  echo [%date% %time%] Deploiement OK - pousse sur main.>> deploy-log.txt
) else (
  echo [%date% %time%] ECHEC du push - voir ci-dessus.>> deploy-log.txt
)
exit /b %errorlevel%
