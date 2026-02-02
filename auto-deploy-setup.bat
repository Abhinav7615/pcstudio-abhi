@echo off
REM PCStudio Abhi - Fully Automated Deployment Setup
REM This script will prepare everything for deployment

echo.
echo =====================================
echo PCStudio Abhi - Deployment Setup
echo =====================================
echo.

REM Check and install Git if needed
echo Checking Git installation...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo WARNING: Git is not installed!
    echo.
    echo INSTALL GIT:
    echo 1. Download: https://git-scm.com/download/windows
    echo 2. Run installer and click Next, Next, Finish
    echo 3. Restart this script
    echo.
    pause
    exit /b 1
)

echo [OK] Git is installed
echo.

REM Initialize git repository
echo Initializing git repository...
cd /d "%~dp0"
git init
echo [OK] Git repository initialized
echo.

REM Configure git
echo Configuring git...
set /p gitname="Enter your name (for git): "
set /p gitemail="Enter your email (for git): "

git config user.name "%gitname%"
git config user.email "%gitemail%"
echo [OK] Git configured
echo.

REM Add all files
echo Adding files to git...
git add .
echo [OK] Files added
echo.

REM Create commit
echo Creating commit...
git commit -m "Initial commit - PCStudioAbhi E-commerce Platform"
echo [OK] Commit created
echo.

REM Instructions
echo.
echo =====================================
echo NEXT STEPS (Do these on GitHub.com)
echo =====================================
echo.
echo 1. Go to: https://github.com/new
echo.
echo 2. Create repository with:
echo    - Name: pcstudio-abhi
echo    - Description: E-commerce platform for refurbished laptops
echo    - Public: Yes
echo.
echo 3. Click: Create Repository
echo.
echo 4. GitHub will show you commands. Copy the commands that look like:
echo.
echo    git remote add origin https://github.com/YOUR_USERNAME/pcstudio-abhi.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo 5. Paste and run those commands in PowerShell
echo.
echo 6. After pushing, open:
echo    - https://render.com - Deploy Backend
echo    - https://vercel.com - Deploy Frontend
echo.
echo For detailed help, read:
echo - FREE_LIVE_DEPLOYMENT.md
echo - LIVE_NOW.md
echo.
pause
