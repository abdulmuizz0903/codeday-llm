#!/usr/bin/env python3
"""
CodeDay LLM Workshop - Environment Checker
This script checks if your environment is set up correctly WITHOUT making any changes
"""

import os
import sys
import platform
import subprocess

def print_header():
    """Print a nice header"""
    print("=" * 60)
    print("🔍 CodeDay LLM Workshop - Environment Checker")
    print("=" * 60)
    print(f"Operating System: {platform.system()}")
    print(f"Python Version: {sys.version}")
    print(f"Current Directory: {os.getcwd()}")
    print("=" * 60)

def check_python_version():
    """Check Python version"""
    print("\n🐍 Checking Python version...")
    if sys.version_info >= (3, 8):
        print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} is compatible")
        return True
    else:
        print(f"❌ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} is too old (need 3.8+)")
        return False

def check_virtual_environment():
    """Check if virtual environment exists"""
    print("\n🌐 Checking virtual environment...")
    venv_path = "codeday-llm"
    
    if os.path.exists(venv_path):
        print(f"✅ Virtual environment found: {venv_path}")
        
        # Check if it's actually a venv
        if platform.system() == "Windows":
            python_path = os.path.join(venv_path, "Scripts", "python.exe")
            pip_path = os.path.join(venv_path, "Scripts", "pip.exe")
        else:
            python_path = os.path.join(venv_path, "bin", "python")
            pip_path = os.path.join(venv_path, "bin", "pip")
        
        if os.path.exists(python_path):
            print("✅ Virtual environment appears to be valid")
            return True
        else:
            print("❌ Virtual environment folder exists but seems corrupted")
            return False
    else:
        print(f"❌ Virtual environment not found: {venv_path}")
        return False

def check_required_files():
    """Check if required files exist"""
    print("\n📁 Checking required files...")
    
    required_files = {
        "main.py": "Main web application",
        "demo.py": "Terminal demo application",
        "requirements.txt": "Python dependencies",
        ".env": "Environment variables (API key)",
        "STUDENT_GUIDE.md": "Student instructions"
    }
    
    all_good = True
    for filename, description in required_files.items():
        if os.path.exists(filename):
            print(f"✅ {filename} - {description}")
        else:
            print(f"❌ {filename} - {description} (MISSING)")
            all_good = False
    
    return all_good

def check_packages():
    """Check if required packages are installed in venv"""
    print("\n📦 Checking installed packages...")
    
    if not os.path.exists("codeday-llm"):
        print("❌ Cannot check packages - virtual environment not found")
        return False
    
    if platform.system() == "Windows":
        pip_path = os.path.join("codeday-llm", "Scripts", "pip")
    else:
        pip_path = os.path.join("codeday-llm", "bin", "pip")
    
    required_packages = ["groq", "flask", "flask-cors", "python-dotenv", "markdown", "requests"]
    
    try:
        result = subprocess.run([pip_path, "list"], capture_output=True, text=True)
        installed_packages = result.stdout.lower()
        
        all_installed = True
        for package in required_packages:
            if package.lower() in installed_packages:
                print(f"✅ {package}")
            else:
                print(f"❌ {package} (NOT INSTALLED)")
                all_installed = False
        
        return all_installed
    except Exception as e:
        print(f"❌ Error checking packages: {e}")
        return False

def check_env_file():
    """Check if .env file has API key"""
    print("\n🔑 Checking API key configuration...")
    
    if not os.path.exists(".env"):
        print("❌ .env file not found")
        return False
    
    try:
        with open(".env", "r") as f:
            content = f.read()
            if "GROQ_KEY=" in content:
                if "your_api_key_here" in content:
                    print("⚠️  .env file exists but API key is not set (still shows placeholder)")
                    return False
                else:
                    print("✅ .env file exists and API key appears to be set")
                    return True
            else:
                print("❌ .env file exists but no GROQ_KEY found")
                return False
    except Exception as e:
        print(f"❌ Error reading .env file: {e}")
        return False

def print_summary(results):
    """Print summary and recommendations"""
    print("\n" + "=" * 60)
    print("📊 SUMMARY")
    print("=" * 60)
    
    total_checks = len(results)
    passed_checks = sum(results.values())
    
    print(f"✅ Passed: {passed_checks}/{total_checks} checks")
    
    if passed_checks == total_checks:
        print("\n🎉 Everything looks good! You're ready to start the workshop!")
        print("\n🚀 Your mentor will show you how to run the workshop!")
    else:
        print("\n⚠️  Some issues found. Here's what to do:")
        
        if not results["python_version"]:
            print("   • Install Python 3.8 or higher")
        
        if not results["virtual_env"]:
            print("   • Run the setup script to create virtual environment")
        
        if not results["required_files"]:
            print("   • Make sure you're in the correct project folder")
        
        if not results["packages"]:
            print("   • Run the setup script to install packages")
        
        if not results["env_file"]:
            print("   • Create .env file and add your GROQ API key")
        
        print("\n💡 Try running 'python setup.py' to fix most issues")

def main():
    """Main function"""
    print_header()
    
    results = {
        "python_version": check_python_version(),
        "virtual_env": check_virtual_environment(),
        "required_files": check_required_files(),
        "packages": check_packages(),
        "env_file": check_env_file()
    }
    
    print_summary(results)
    
    print("\n🆘 Need help? Ask your mentor!")

if __name__ == "__main__":
    main()
