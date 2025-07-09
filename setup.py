#!/usr/bin/env python3
"""
CodeDay LLM Workshop - Universal Setup Script
This script works on Windows, macOS, and Linux
"""

import os
import sys
import subprocess
import platform
import shutil
from pathlib import Path

def print_header():
    """Print a nice header for the setup script"""
    print("=" * 60)
    print("🤖 CodeDay LLM Workshop - Setup Script")
    print("=" * 60)
    print(f"Operating System: {platform.system()}")
    print(f"Python Version: {sys.version}")
    print("=" * 60)

def check_python_version():
    """Check if Python version is compatible"""
    try:
        # Check if we're running Python 3.8 or higher
        if sys.version_info >= (3, 8):
            print("✅ Python version is compatible")
            return True
        else:
            print("❌ Error: Python 3.8 or higher is required!")
            print(f"Current version: {sys.version}")
            print("Please install a newer version of Python and try again.")
            return False
    except:
        # This might happen in very old Python versions
        print("❌ Error: Cannot determine Python version or version is too old!")
        print("Please install Python 3.8 or higher and try again.")
        return False

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        if platform.system() == "Windows":
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        else:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}")
        print(f"Command: {command}")
        print(f"Error: {e.stderr}")
        return False

def create_virtual_environment():
    """Create a virtual environment"""
    venv_name = "codeday-llm"
    
    # Check if virtual environment already exists
    if os.path.exists(venv_name):
        print(f"⚠️  Virtual environment '{venv_name}' already exists")
        choice = input("Do you want to (k)eep it, (r)ecreate it, or (a)bort? [k/r/a]: ").lower().strip()
        
        if choice == 'a':
            print("❌ Setup aborted by user")
            return False
        elif choice == 'r':
            print(f"🗑️  Removing existing virtual environment: {venv_name}")
            try:
                shutil.rmtree(venv_name)
            except Exception as e:
                print(f"❌ Error removing virtual environment: {e}")
                return False
        elif choice == 'k':
            print(f"✅ Keeping existing virtual environment: {venv_name}")
            return True
        else:
            print("❌ Invalid choice. Setup aborted.")
            return False
    
    # Create new virtual environment
    if not run_command(f"python -m venv {venv_name}", "Creating virtual environment"):
        # Try with python3 if python doesn't work
        if not run_command(f"python3 -m venv {venv_name}", "Creating virtual environment with python3"):
            print("❌ Failed to create virtual environment")
            return False
    
    return True

def get_activation_command():
    """Get the command to activate virtual environment based on OS"""
    if platform.system() == "Windows":
        return "codeday-llm\\Scripts\\activate"
    else:
        return "source codeday-llm/bin/activate"

def install_requirements():
    """Install required packages"""
    venv_name = "codeday-llm"
    
    if platform.system() == "Windows":
        pip_path = os.path.join(venv_name, "Scripts", "pip")
        python_path = os.path.join(venv_name, "Scripts", "python")
    else:
        pip_path = os.path.join(venv_name, "bin", "pip")
        python_path = os.path.join(venv_name, "bin", "python")
    
    # Install requirements
    if os.path.exists("requirements.txt"):
        if not run_command(f"{pip_path} install -r requirements.txt", "Installing requirements"):
            print("❌ Failed to install requirements")
            return False
    else:
        print("⚠️  requirements.txt not found. Installing basic packages...")
        packages = [
            "groq",
            "flask",
            "flask-cors",
            "python-dotenv",
            "markdown",
            "requests"
        ]
        
        for package in packages:
            if not run_command(f"{pip_path} install {package}", f"Installing {package}"):
                print(f"❌ Failed to install {package}")
                return False
    
    return True

def create_env_file():
    """Create a sample .env file if it doesn't exist"""
    env_file = ".env"
    
    if not os.path.exists(env_file):
        print("📝 Creating sample .env file...")
        with open(env_file, "w") as f:
            f.write("# CodeDay LLM Workshop - Environment Variables\n")
            f.write("# Get your API key from: https://console.groq.com/keys\n")
            f.write("GROQ_KEY=your_api_key_here\n")
        print("✅ Sample .env file created")
        print("⚠️  IMPORTANT: You need to add your GROQ API key to the .env file!")
    else:
        print("✅ .env file already exists")
        print("⚠️  Make sure your GROQ API key is set in the .env file!")
        
        # Check if the .env file has the API key set
        try:
            with open(env_file, "r") as f:
                content = f.read()
                if "your_api_key_here" in content or "GROQ_KEY=" not in content:
                    print("⚠️  Don't forget to update your API key in the .env file!")
        except:
            pass

def print_completion_message():
    """Print completion message with instructions"""
    print("\n" + "=" * 60)
    print("🎉 Setup completed successfully!")
    print("=" * 60)
    
    print("\n📋 Next steps:")
    print("1. Add your GROQ API key to the .env file")
    print("2. Your mentor will show you how to run the workshop")
    
    print("\n🔗 Web Interface URL: http://localhost:2718")
    print("📚 Check STUDENT_GUIDE.md for more information")
    print("\n🆘 Need help? Ask your mentor!")

def main():
    """Main setup function"""
    print_header()
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create virtual environment
    if not create_virtual_environment():
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        sys.exit(1)
    
    # Create .env file
    create_env_file()
    
    # Print completion message
    print_completion_message()

if __name__ == "__main__":
    main()
