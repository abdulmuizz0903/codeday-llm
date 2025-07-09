#!/bin/bash

echo "============================================================"
echo "🤖 CodeDay LLM Workshop - Unix/Linux/macOS Setup"
echo "============================================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "❌ Python is not installed"
    echo "Please install Python 3.8+ from your package manager or https://python.org"
    exit 1
fi

echo "✅ Python found"
echo

# Run the setup script
echo "🔄 Running setup script..."
if command -v python3 &> /dev/null; then
    python3 setup.py
else
    python setup.py
fi

echo
echo "============================================================"
echo "Setup complete! Check the messages above for next steps."
echo "============================================================"
