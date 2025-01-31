# tasks.py
from crewai import Task
import agents

def create_tasks():
    weather_agent, news_agent = agents.create_agents()
    
    tasks = [
        Task(
            description='What is the current weather in Mysore?',
            expected_output='A detailed weather report for Mysore including temperature and conditions.',
            agent=weather_agent
        ),
        Task(
            description='What are the latest news headlines?',
            expected_output='A list of the top 5 latest news headlines from India.',
            agent=news_agent
        )
    ]
    
    return tasks, [weather_agent, news_agent]