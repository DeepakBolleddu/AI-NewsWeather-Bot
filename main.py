# main.py
from crewai import Crew
import sys
import config
import tasks

def validate_environment():
    """Validate that all required API keys are present"""
    if not config.OPENAI_API_KEY:
        print("Error: OPENAI_API_KEY not found in environment variables")
        print("Please set your OpenAI API key in the .env file or environment variables")
        sys.exit(1)

def main():
    try:
        # Validate environment
        validate_environment()
        
        # Get tasks and agents
        crew_tasks, crew_agents = tasks.create_tasks()
        
        # Initialize crew
        crew = Crew(
            agents=crew_agents,
            tasks=crew_tasks,
            verbose=True
        )
        
        # Execute tasks
        result = crew.kickoff()
        
        print("\n=== Results ===")
        print(result)
        
    except Exception as e:
        print(f"Error running crew: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()