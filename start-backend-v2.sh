#!/bin/bash

# Second Hand PC Studio - Backend Setup & Run Script

echo ""
echo "===================================="
echo "Second Hand PC Studio - Setup Script"
echo "===================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ using: sudo apt-get install python3 python3-pip"
    exit 1
fi

echo "[1/5] Checking Python version..."
python3 --version
echo ""

echo "[2/5] Installing dependencies..."
cd backend
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi
echo "Dependencies installed successfully!"
echo ""

echo "[3/5] Configuring environment..."
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cp .env .env.backup 2>/dev/null || true
    echo ".env file needs configuration. Please update:"
    echo "  - MAIL_USERNAME"
    echo "  - MAIL_PASSWORD"
    echo "  - SECRET_KEY"
else
    echo ".env file already exists"
fi
echo ""

echo "[4/5] Database will be initialized..."
echo "Once server starts, open a new terminal and run:"
echo "  curl -X POST http://localhost:5000/api/init-db"
echo ""

echo "[5/5] Starting backend server..."
python3 server_v2.py
