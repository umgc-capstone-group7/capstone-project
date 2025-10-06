#!/usr/bin/env python3
"""
OpenAI API Key Setup Script
Run this script to set up your OpenAI API key for the AI Quiz Generator
"""

import os
import sys

def setup_openai_key():
    print("🤖 AI Quiz Generator - OpenAI API Key Setup")
    print("=" * 50)
    
    # Check if key is already set
    current_key = os.getenv('OPENAI_API_KEY')
    if current_key and current_key != 'sk-proj-your-key-here':
        print(f"✅ OpenAI API key is already set: {current_key[:10]}...")
        return True
    
    print("\n📝 To get your OpenAI API key:")
    print("1. Go to: https://platform.openai.com/api-keys")
    print("2. Sign up or log in")
    print("3. Click 'Create new secret key'")
    print("4. Copy the key (starts with 'sk-')")
    
    print("\n🔑 Enter your OpenAI API key:")
    api_key = input("API Key: ").strip()
    
    if not api_key or not api_key.startswith('sk-'):
        print("❌ Invalid API key format. Key should start with 'sk-'")
        return False
    
    # Set the environment variable for current session
    os.environ['OPENAI_API_KEY'] = api_key
    
    # Update the config file
    config_path = 'app/ai_config.py'
    try:
        with open(config_path, 'r') as f:
            content = f.read()
        
        # Replace the placeholder with the actual key
        updated_content = content.replace(
            "OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'sk-proj-your-key-here')",
            f"OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '{api_key}')"
        )
        
        with open(config_path, 'w') as f:
            f.write(updated_content)
        
        print("✅ API key configured successfully!")
        print("🚀 You can now use the AI Quiz Generator!")
        return True
        
    except Exception as e:
        print(f"❌ Error updating config: {e}")
        return False

if __name__ == "__main__":
    if setup_openai_key():
        print("\n🎉 Setup complete! Restart your Flask app to use the AI Quiz Generator.")
    else:
        print("\n❌ Setup failed. Please try again.")
        sys.exit(1)
