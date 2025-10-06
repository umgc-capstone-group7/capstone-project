# AI Quiz Generator Configuration
import os

# OpenAI API Configuration
# Replace 'YOUR_OPENAI_API_KEY_HERE' with your actual OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'YOUR_OPENAI_API_KEY_HERE')

# Alternative: Set your key directly here (uncomment and replace)
# OPENAI_API_KEY = 'sk-proj-your-actual-openai-key-here'

# Quiz Generation Settings
DEFAULT_MODEL = "gpt-3.5-turbo"
MAX_TOKENS = 2000
TEMPERATURE = 0.7

# Rate limiting (optional)
MAX_REQUESTS_PER_HOUR = 100
