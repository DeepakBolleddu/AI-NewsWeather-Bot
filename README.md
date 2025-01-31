# AI-NewsWeather-Bot

AI-NewsWeather-Bot is an intelligent chatbot that provides real-time weather updates and the latest news headlines. Built using **CrewAI** and **OpenAI's GPT**, this bot efficiently retrieves and summarizes relevant information using specialized agents.

## Features
✅ **Weather Updates** – Fetches real-time weather conditions for any city.  
✅ **Latest News** – Retrieves and summarizes the top headlines.  
✅ **AI-Powered Agents** – Uses CrewAI agents for task-specific expertise.  
✅ **Modular Design** – Easily extendable with additional functionalities.  
✅ **Error Handling** – Validates API keys before execution.  

## Tech Stack
- **Backend:** Python, CrewAI
- **AI Model:** OpenAI API
- **Utilities:** LangChain, Task Management

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/DeepakBolleddu/AI-NewsWeather-Bot.git
cd AI-NewsWeather-Bot
```

### 2. Set Up a Virtual Environment
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory and add your API keys:
```ini
OPENAI_API_KEY=your-openai-api-key
WEATHER_API_KEY=your-weather-api-key
NEWS_API_KEY=your-news-api-key
```

### 5. Run the Application
```bash
python main.py
```

## Usage
- The bot retrieves and summarizes news headlines.
- It provides weather updates for specified cities.
- Additional functionalities can be added using CrewAI agents.

## Contributing
Feel free to contribute by submitting a pull request. Ensure your code follows best practices.

## License
This project is licensed under the MIT License.

## Contact
For questions or issues, open an issue on GitHub or contact Deepak Bolleddu.
