@echo off
REM Add custom domains to hosts file (Run as Administrator)

setlocal enabledelayedexpansion

echo Adding custom domains to hosts file...
echo.

REM Backup original hosts file
copy C:\Windows\System32\drivers\etc\hosts C:\Windows\System32\drivers\etc\hosts.backup
echo [OK] Backup created: hosts.backup
echo.

REM Add custom domains
(
    echo.
    echo 127.0.0.1 pcstudioabhi.com
    echo 127.0.0.1 www.pcstudioabhi.com
    echo 127.0.0.1 admin.pcstudioabhi.com
    echo 127.0.0.1 api.pcstudioabhi.com
) >> C:\Windows\System32\drivers\etc\hosts

echo [OK] Custom domains added!
echo.
echo Domains added:
echo   - pcstudioabhi.com
echo   - www.pcstudioabhi.com
echo   - admin.pcstudioabhi.com
echo   - api.pcstudioabhi.com
echo.
echo You can now access your website using these domains:
echo   http://pcstudioabhi.com:5500
echo   http://api.pcstudioabhi.com:5000
echo.
echo Press any key to exit...
pause
