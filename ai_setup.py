#!/usr/bin/env python3
"""
AI Setup for Smart Quiz Generator
=================================

This script helps you set up AI-powered text analysis for the Smart Quiz Generator.

To enable AI analysis:
1. Get an OpenAI API key from: https://platform.openai.com/api-keys
2. Set the environment variable: export OPENAI_API_KEY="your-api-key-here"
3. Or create a .env file with: OPENAI_API_KEY=your-api-key-here

Without an API key, the quiz generator will use enhanced basic text analysis.
"""

import os

def setup_ai_analysis():
    """Setup AI analysis for the quiz generator"""
    
    print("🤖 AI-Powered Smart Quiz Generator Setup")
    print("=" * 50)
    
    # Check if API key is already set
    api_key = os.environ.get('OPENAI_API_KEY')
    
    if api_key and api_key != "your-openai-api-key":
        print("✅ OpenAI API key is already configured!")
        print(f"   Key: {api_key[:10]}...{api_key[-4:]}")
        print("   AI analysis is ENABLED")
        return True
    else:
        print("❌ No OpenAI API key found")
        print("\nTo enable AI analysis:")
        print("1. Get an API key from: https://platform.openai.com/api-keys")
        print("2. Set environment variable:")
        print("   export OPENAI_API_KEY='your-api-key-here'")
        print("3. Or create a .env file with:")
        print("   OPENAI_API_KEY=your-api-key-here")
        print("\nWithout API key: Enhanced basic analysis will be used")
        return False

if __name__ == "__main__":
    setup_ai_analysis()
