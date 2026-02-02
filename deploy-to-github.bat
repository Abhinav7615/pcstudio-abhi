@echo off
REM PCStudio Abhi - One-Click Deployment Script
REM This script prepares your code for GitHub push

echo.
echo ====================================
echo PCStudio Abhi - Deployment Script
echo ====================================
echo.

REM Check if Git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Git is not installed!
    echo Download from: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo [1/5] Initializing Git repository...
git init
echo [OK] Git initialized
echo.

echo [2/5] Adding all files...
git add .
echo [OK] Files staged
echo.

echo [3/5] Creating initial commit...
git commit -m "Initial commit - PCStudioAbhi e-commerce platform"
echo [OK] Commit created
echo.

echo [4/5] Instructions for GitHub...
echo.
echo NEXT STEPS:
echo ===========
echo.
echo 1. Go to: https://github.com/new
echo 2. Create repository: "pcstudio-abhi"
echo 3. Copy the commands shown (git remote add origin...)
echo 4. Paste them in terminal and run
echo.
echo Then come back and run this batch again to push!
echo.
echo Press any key to open GitHub...
pause
start https://github.com/new

echo.
echo [5/5] Waiting for you to create repository...
echo.
echo Once created, run these commands:
echo.
echo git remote add origin https://github.com/YOUR_USERNAME/pcstudio-abhi.git
echo git branch -M main
echo git push -u origin main
echo.
echo After pushing, deployment will be ready!
echo.
pause
