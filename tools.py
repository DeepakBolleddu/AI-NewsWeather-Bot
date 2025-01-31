# tools.py
import requests
from langchain_community.tools import Tool
import config

def fetch_weather(city: str = config.DEFAULT_CITY) -> str:
    """Fetch current weather for a given city"""
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': config.WEATHER_API_KEY,
            'units': 'metric'
        }
        response = requests.get(url, params=params)
        data = response.json()
        return f"Current weather in {city}: {data['main']['temp']}°C, {data['weather'][0]['description']}"
    except Exception as e:
        return f"Error fetching weather data: {str(e)}"

def fetch_news() -> str:
    """Fetch latest news headlines"""
    try:
        url = "https://newsapi.org/v2/top-headlines"
        params = {
            'country': 'in',
            'apiKey': config.NEWS_API_KEY
        }
        response = requests.get(url, params=params)
        data = response.json()
        headlines = [f"• {article['title']}" for article in data['articles'][:5]]
        return "\n".join(headlines)
    except Exception as e:
        return f"Error fetching news: {str(e)}"

# Create tool instances
weather_tool = Tool(
    name="Weather Tool",
    func=fetch_weather,
    description="Get current weather for a city"
)

news_tool = Tool(
    name="News Tool",
    func=fetch_news,
    description="Get latest news headlines"
)


#tools.py
#--> 1) Implementation part
#--> 2) Create tool instances
