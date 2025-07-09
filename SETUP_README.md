# 🚀 CodeDay LLM Workshop - Quick Setup

This guide will help you set up everything needed for the CodeDay LLM Workshop.

## 📋 Prerequisites

- Python 3.8 or higher installed on your system
- Internet connection for downloading packages
- A GROQ API key (get one from https://console.groq.com/keys)

## 🔧 Setup Instructions

### Step 0: Check Your Environment (Recommended)
Before running the setup, you can check if everything is already working:
```bash
python check_setup.py
```
This will tell you what's missing without changing anything.

### ⚠️ Important Safety Note
**Before running the setup script, make sure you're in the correct project folder!** The script creates a virtual environment and files in the current directory.

### Option 1: Automatic Setup (Recommended)

#### Windows Users:
1. **Navigate to the project folder first**
2. Double-click `setup.bat`
3. Follow the instructions in the terminal

#### macOS/Linux Users:
1. Open Terminal
2. **Navigate to the project folder**
3. Run: `chmod +x setup.sh && ./setup.sh`

#### All Systems (Alternative):
1. Open Terminal/Command Prompt
2. **Navigate to the project folder**
3. Run: `python setup.py`

### Option 2: Manual Setup

If the automatic setup doesn't work, follow these steps:

1. **Create Virtual Environment:**
   ```bash
   python -m venv codeday-llm
   ```

2. **Activate Virtual Environment:**
   - Windows: `codeday-llm\Scripts\activate`
   - macOS/Linux: `source codeday-llm/bin/activate`

3. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create .env file:**
   ```bash
   # Create a file named .env and add:
   GROQ_KEY=your_actual_api_key_here
   ```

## 🛡️ Safety Information

**Please read this before running the setup script:**

1. **Location**: Always run the setup script from the CodeDay LLM Workshop project folder
2. **Virtual Environment**: The script will ask before removing any existing `codeday-llm` folder
3. **Files**: The script only creates files in the current directory (it won't modify files elsewhere)
4. **API Key**: Your `.env` file will be preserved if it already exists

**If you're unsure about anything, ask your mentor before running the setup!**

## 🎯 After Setup

1. **Add your API key** to the `.env` file
2. **Choose how to run:**
   - **Web Interface:** Use `run_web.bat` (Windows) or `./run_web.sh` (Unix)
   - **Terminal:** Use `run_terminal.bat` (Windows) or `./run_terminal.sh` (Unix)
   - **Manual:** Activate the virtual environment and run `python main.py`

## 🌐 Access the Web Interface

Once running, open your browser and go to: **http://localhost:2718**

## 📚 Student Guide

Check `STUDENT_GUIDE.md` for detailed instructions on using the workshop.

## 🆘 Troubleshooting

### Common Issues:

1. **"Python not found"**
   - Install Python from https://python.org
   - Make sure Python is added to your PATH

2. **"Permission denied" (macOS/Linux)**
   - Run: `chmod +x setup.sh run_web.sh run_terminal.sh`

3. **"Module not found"**
   - Make sure you activated the virtual environment
   - Run the setup script again

4. **"Port already in use"**
   - Someone else is already running the server
   - Close other instances or use a different port

### Still Having Issues?

1. Check that you're in the correct project folder
2. Make sure your internet connection is working
3. Try running the setup script again
4. Ask your mentor for help!

## 📁 Files Created by Setup

- `codeday-llm/` - Virtual environment folder
- `.env` - Environment variables (add your API key here)
- `run_web.bat` / `run_web.sh` - Easy way to start web interface
- `run_terminal.bat` / `run_terminal.sh` - Easy way to start terminal version

## 🎉 You're Ready!

Once setup is complete, you can start exploring the world of AI! Have fun! 🌟
