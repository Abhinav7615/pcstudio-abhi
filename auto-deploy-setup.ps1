#!/usr/bin/env pwsh

Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "PCStudio Abhi - Automated Deployment" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""

# Check if Git is installed
Write-Host "Checking Git installation..." -ForegroundColor Yellow
$gitCheck = git --version 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Git is not installed!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Git:" -ForegroundColor Yellow
    Write-Host "  1. Go to: https://git-scm.com/download/windows"
    Write-Host "  2. Download and install"
    Write-Host "  3. Restart PowerShell"
    Write-Host "  4. Run this script again"
    Write-Host ""
    pause
    exit 1
}

Write-Host "[OK] Git is installed: $gitCheck" -ForegroundColor Green
Write-Host ""

# Get to project directory
$projectPath = $PSScriptRoot
Set-Location $projectPath
Write-Host "Working directory: $projectPath" -ForegroundColor Cyan
Write-Host ""

# Initialize Git
Write-Host "Initializing Git repository..." -ForegroundColor Yellow
git init
Write-Host "[OK] Git initialized" -ForegroundColor Green
Write-Host ""

# Configure Git
Write-Host "Configuring Git..." -ForegroundColor Yellow
$gitName = Read-Host "Enter your name (for git commits)"
$gitEmail = Read-Host "Enter your email (for git commits)"

git config user.name $gitName
git config user.email $gitEmail
Write-Host "[OK] Git configured" -ForegroundColor Green
Write-Host ""

# Add all files
Write-Host "Adding files to Git..." -ForegroundColor Yellow
git add .
Write-Host "[OK] All files added" -ForegroundColor Green
Write-Host ""

# Create commit
Write-Host "Creating initial commit..." -ForegroundColor Yellow
git commit -m "Initial commit - PCStudioAbhi E-commerce Platform ($(Get-Date -Format 'yyyy-MM-dd'))"
Write-Host "[OK] Commit created" -ForegroundColor Green
Write-Host ""

# Show git status
Write-Host "Git status:" -ForegroundColor Cyan
git status
Write-Host ""

# Show next steps
Write-Host "=====================================" -ForegroundColor Green
Write-Host "NEXT STEPS - DO THESE NOW!" -ForegroundColor Green
Write-Host "=====================================" -ForegroundColor Green
Write-Host ""

Write-Host "1. CREATE GITHUB ACCOUNT (Free)" -ForegroundColor Yellow
Write-Host "   Go to: https://github.com/signup"
Write-Host ""

Write-Host "2. CREATE GITHUB REPOSITORY" -ForegroundColor Yellow
Write-Host "   Go to: https://github.com/new"
Write-Host "   Name: pcstudio-abhi"
Write-Host "   Description: E-commerce platform"
Write-Host "   Public: Yes"
Write-Host "   Create"
Write-Host ""

Write-Host "3. COPY COMMANDS FROM GITHUB" -ForegroundColor Yellow
Write-Host "   GitHub will show you:"
Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/pcstudio-abhi.git"
Write-Host "   git branch -M main"
Write-Host "   git push -u origin main"
Write-Host ""

Write-Host "4. RUN THOSE COMMANDS HERE" -ForegroundColor Yellow
Write-Host "   Paste and run in PowerShell"
Write-Host ""

Write-Host "5. THEN DEPLOY" -ForegroundColor Yellow
Write-Host "   Render: https://render.com"
Write-Host "   Vercel: https://vercel.com"
Write-Host ""

Write-Host "Read detailed guide:" -ForegroundColor Cyan
Write-Host "  FREE_LIVE_DEPLOYMENT.md"
Write-Host "  LIVE_NOW.md"
Write-Host ""

Write-Host "=====================================" -ForegroundColor Green
Write-Host "Ready! Press Enter to continue..." -ForegroundColor Green
Write-Host "=====================================" -ForegroundColor Green
Read-Host ""
