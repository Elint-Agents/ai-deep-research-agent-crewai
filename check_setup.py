#!/usr/bin/env python3
"""
Setup verification script for AI Deep Research Agent (CrewAI)
Checks Python version and key dependencies
"""

import sys
import subprocess
import importlib

def check_python_version():
    """Check if Python version is 3.11+"""
    print("🐍 Checking Python version...")
    version = sys.version_info
    print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major == 3 and version.minor >= 11:
        print("   ✅ Python 3.11+ detected - OK")
        return True
    else:
        print("   ❌ Python 3.11+ required!")
        print("   Please upgrade to Python 3.11 or higher")
        return False

def check_sqlite_version():
    """Check sqlite3 version"""
    print("\n🗄️ Checking sqlite3 version...")
    try:
        import sqlite3
        version = sqlite3.sqlite_version
        print(f"   Current version: {version}")
        
        # Parse version string (e.g., "3.35.0")
        major, minor, patch = map(int, version.split('.'))
        if major >= 3 and minor >= 35:
            print("   ✅ sqlite3 >= 3.35.0 detected - OK")
            return True
        else:
            print("   ❌ sqlite3 >= 3.35.0 required!")
            return False
    except Exception as e:
        print(f"   ❌ Error checking sqlite3: {e}")
        return False

def check_dependencies():
    """Check if key dependencies are available"""
    print("\n📦 Checking key dependencies...")
    
    dependencies = [
        ("streamlit", "Streamlit"),
        ("crewai", "CrewAI"),
        ("langchain", "LangChain"),
        ("openai", "OpenAI"),
        ("firecrawl", "Firecrawl"),
        ("beautifulsoup4", "BeautifulSoup4"),
        ("requests", "Requests")
    ]
    
    all_ok = True
    for module, name in dependencies:
        try:
            importlib.import_module(module)
            print(f"   ✅ {name} - OK")
        except ImportError:
            print(f"   ❌ {name} - NOT FOUND")
            all_ok = False
    
    return all_ok

def check_api_keys():
    """Check if API keys are set in environment (optional)"""
    print("\n🔑 Checking API keys...")
    
    import os
    keys = {
        "OPENAI_API_KEY": "OpenAI",
        "GROQ_API_KEY": "Groq", 
        "FIRECRAWL_API_KEY": "Firecrawl"
    }
    
    found_keys = []
    for key, name in keys.items():
        if os.getenv(key):
            print(f"   ✅ {name} API key found in environment")
            found_keys.append(name)
        else:
            print(f"   ⚠️ {name} API key not in environment (will enter in app)")
    
    if found_keys:
        print(f"   Found {len(found_keys)} API key(s) in environment")
    else:
        print("   ℹ️ No API keys in environment - you'll enter them in the Streamlit app")
    
    print("   💡 Note: This app uses Streamlit session state for API keys, not .env files")
    return True

def main():
    """Run all checks"""
    print("🔍 AI Deep Research Agent (CrewAI) - Setup Verification")
    print("=" * 60)
    
    checks = [
        check_python_version(),
        check_sqlite_version(),
        check_dependencies(),
        check_api_keys()
    ]
    
    print("\n" + "=" * 60)
    if all(checks):
        print("🎉 All checks passed! You're ready to run the app.")
        print("\n🚀 To start the app, run:")
        print("   streamlit run deep_research_crewai.py")
    else:
        print("❌ Some checks failed. Please fix the issues above.")
        print("\n💡 Installation help:")
        print("   1. Ensure Python 3.11+ is installed")
        print("   2. Create virtual environment: python3.11 -m venv venv311")
        print("   3. Activate: source venv311/bin/activate")
        print("   4. Install: pip install -r requirements.txt")

if __name__ == "__main__":
    main() 