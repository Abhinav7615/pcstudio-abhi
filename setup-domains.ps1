$hostsPath = "C:\Windows\System32\drivers\etc\hosts"
$domains = @(
    "127.0.0.1 pcstudioabhi.com",
    "127.0.0.1 www.pcstudioabhi.com",
    "127.0.0.1 admin.pcstudioabhi.com",
    "127.0.0.1 api.pcstudioabhi.com"
)

Write-Host "==================================" -ForegroundColor Cyan
Write-Host "PCStudio Abhi - Domain Setup" -ForegroundColor Cyan
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""

# Check if running as admin
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")

if (-not $isAdmin) {
    Write-Host "ERROR: This script must run as Administrator!" -ForegroundColor Red
    Write-Host "Please right-click PowerShell and select 'Run as Administrator'" -ForegroundColor Yellow
    exit
}

# Backup hosts file
Write-Host "Creating backup of hosts file..." -ForegroundColor Yellow
Copy-Item $hostsPath "$hostsPath.backup" -Force
Write-Host "[OK] Backup created: hosts.backup" -ForegroundColor Green
Write-Host ""

# Read current hosts file
$hostsContent = Get-Content $hostsPath

# Add domains
Write-Host "Adding custom domains..." -ForegroundColor Yellow
$newContent = $hostsContent + "`n`n# PCStudio Abhi Domains`n" + ($domains -join "`n")

# Write to hosts file
$newContent | Set-Content $hostsPath
Write-Host "[OK] Custom domains added!" -ForegroundColor Green
Write-Host ""

# Verify
Write-Host "Verifying domains..." -ForegroundColor Yellow
foreach ($domain in $domains) {
    Write-Host "  ✓ $domain" -ForegroundColor Green
}

Write-Host ""
Write-Host "==================================" -ForegroundColor Cyan
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "You can now access:" -ForegroundColor Cyan
Write-Host "  Frontend:  http://pcstudioabhi.com:5500" -ForegroundColor White
Write-Host "  Backend:   http://api.pcstudioabhi.com:5000" -ForegroundColor White
Write-Host "  Admin:     http://admin.pcstudioabhi.com:5500" -ForegroundColor White
Write-Host ""
Write-Host "Test domain:" -ForegroundColor Cyan
Write-Host "  ping pcstudioabhi.com" -ForegroundColor White
Write-Host ""
