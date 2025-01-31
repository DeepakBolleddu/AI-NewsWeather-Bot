# agents.py
from crewai import Agent
from langchain_openai import OpenAI
import config
import tools

# Initialize OpenAI
llm = OpenAI(
    api_key=config.OPENAI_API_KEY,
    temperature=0.7 # 0-1
)

def create_agents():
    weather_agent = Agent(
        role='Weather Expert',
        goal='Provide accurate weather information',
        backstory='I am an expert at retrieving and analyzing weather data for cities.',
        tools=[tools.weather_tool],
        llm=llm,
        verbose=True
    )

    news_agent = Agent(
        role='News Reporter',
        goal='Provide latest news updates',
        backstory='I am a news expert who finds and summarizes the latest headlines.',
        tools=[tools.news_tool],
        llm=llm,
        verbose=True
    )

    return weather_agent, news_agent