@echo off
echo ============================================================
echo 🤖 CodeDay LLM Workshop - Windows Setup
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

echo ✅ Python found
echo.

REM Run the setup script
echo 🔄 Running setup script...
python setup.py

echo.
echo ============================================================
echo Setup complete! Check the messages above for next steps.
echo ============================================================
pause
