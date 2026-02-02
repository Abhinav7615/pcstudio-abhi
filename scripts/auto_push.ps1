<#
Auto Push Script
Usage: Run this from PowerShell. It will:
 - Verify git is installed
 - Ensure global `user.name` and `user.email` are set (prompts if missing)
 - Initialize repo if needed
 - Create an initial commit if none exists
 - Add/replace `origin` remote (default: https://github.com/Abhinav7615/pcstudio-abhi.git)
 - Rename branch to `main` and push using a Personal Access Token (PAT)

Security note: The script will temporarily use the token in a push URL to authenticate. The token is not stored on disk.
#>

Set-StrictMode -Version Latest

function Write-OK($m){ Write-Host $m -ForegroundColor Green }
function Write-Err($m){ Write-Host $m -ForegroundColor Red }

try {
    git --version > $null 2>&1
} catch {
    Write-Err "Git not found. Please install Git (https://git-scm.com/download) and re-run this script."
    exit 1
}

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location (Resolve-Path "$scriptDir\..")

Write-Host "Working directory: $(Get-Location)"

# Ensure user.name and user.email
$globalName = (git config --global user.name) -join ''
$globalEmail = (git config --global user.email) -join ''

if (-not $globalName -or $globalName -eq '') {
    $inpName = Read-Host "Enter your Git user.name (for commits)"
    if ($inpName -and $inpName.Trim() -ne '') { git config --global user.name "$inpName" }
}
if (-not $globalEmail -or $globalEmail -eq '') {
    $inpEmail = Read-Host "Enter your Git user.email (for commits)"
    if ($inpEmail -and $inpEmail.Trim() -ne '') { git config --global user.email "$inpEmail" }
}

Write-OK "Git user.name: $(git config --global user.name)"
Write-OK "Git user.email: $(git config --global user.email)"

# Init repo if needed
if (-not (Test-Path .git)) {
    Write-Host "No .git directory found — initializing repository..."
    git init
} else {
    Write-Host "Existing git repository detected."
}

# Ensure there is at least one commit
$hasCommit = $true
try {
    git rev-parse --verify HEAD > $null 2>&1
} catch {
    $hasCommit = $false
}

if (-not $hasCommit) {
    Write-Host "No commits found — creating initial commit..."
    git add .
    git commit -m "Initial commit" --allow-empty
    Write-OK "Initial commit created."
} else {
    Write-Host "Commit history exists."
}

# Default repo URL — change if you want
$defaultRepo = 'https://github.com/Abhinav7615/pcstudio-abhi.git'
$repoInput = Read-Host "Enter GitHub repository HTTPS URL (press Enter to use default: $defaultRepo)"
if (-not $repoInput -or $repoInput.Trim() -eq '') { $repo = $defaultRepo } else { $repo = $repoInput.Trim() }

# Replace existing origin if present
$remotes = git remote
if ($remotes -match 'origin') {
    Write-Host "Removing existing origin..."
    git remote remove origin
}
Write-Host "Adding origin: $repo"
git remote add origin $repo

Write-Host "Renaming branch to main..."
git branch -M main

# Ask for username + PAT to push
$username = Read-Host "GitHub username for push (press Enter to keep URL's username if present)"
$secureToken = Read-Host "Enter GitHub Personal Access Token (input hidden)" -AsSecureString

if ($secureToken.Length -eq 0) {
    Write-Err "No token provided. Attempting to push using existing credential helper..."
    git push -u origin main
    if ($LASTEXITCODE -eq 0) { Write-OK "Pushed successfully."; exit 0 } else { Write-Err "Push failed. Provide a PAT to authenticate. Exiting."; exit 2 }
}

# Convert secure string to plain text temporarily
$bstr = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureToken)
$plainToken = [System.Runtime.InteropServices.Marshal]::PtrToStringBSTR($bstr)
[System.Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr)

if (-not $username -or $username.Trim() -eq '') {
    # try to extract username from repo URL
    if ($repo -match 'https://github.com/([^/]+)/') { $username = $matches[1] }
}

$pushUrl = $repo -replace '^https://', "https://$username:$plainToken@"

Write-Host "Pushing to GitHub..."
git push $pushUrl main:main -u

if ($LASTEXITCODE -eq 0) {
    Write-OK "Push successful. Code is on GitHub."
} else {
    Write-Err "Push failed. Check token, internet and repo URL."
}

# Clear sensitive variable
$plainToken = $null

Write-Host "Done.";
