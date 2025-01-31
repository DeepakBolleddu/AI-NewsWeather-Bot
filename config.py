# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', 'ea01ce62ea0dc6d721ccb889c984d07a') #hardcoded API
NEWS_API_KEY = os.getenv('NEWS_API_KEY', '29e02e8bb29040cca0284a4cea640a1d')
DEFAULT_CITY = "Mysore"