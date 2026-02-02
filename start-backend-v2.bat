@echo off
REM Second Hand PC Studio - Backend Setup & Run Script

echo.
echo ====================================
echo Second Hand PC Studio - Setup Script
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ and add it to PATH
    pause
    exit /b 1
)

echo [1/5] Checking Python version...
python --version
echo.

echo [2/5] Installing dependencies...
cd backend
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo Dependencies installed successfully!
echo.

echo [3/5] Configuring environment...
if not exist .env (
    echo Creating .env file...
    copy .env .env.backup >nul 2>&1
    echo .env file needs configuration. Please update:
    echo   - MAIL_USERNAME
    echo   - MAIL_PASSWORD
    echo   - SECRET_KEY
) else (
    echo .env file already exists
)
echo.

echo [4/5] Initializing database...
echo Starting Flask server for database initialization...
echo Please wait (this may take 30 seconds)...
echo.
echo Once server starts, open a new terminal and run:
echo   curl -X POST http://localhost:5000/api/init-db
echo.
echo Then press Ctrl+C to stop the server when initialization is complete.
echo.

echo [5/5] Starting backend server...
python server_v2.py

pause
