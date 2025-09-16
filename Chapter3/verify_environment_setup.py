import os
from dotenv import load_dotenv
from agents import Agent, Runner

# Load environment variables from the .env file
load_dotenv()

# Access the API key
api_key = os.getenv("OPENAI_API_KEY")

# Check to confirm API key is accessible:
if not api_key:
    print("Error: OPENAI_API_KEY not found. Please set it in your.env file.")
else:
    print("API Key loaded successfully.")

# Create an agent and run it
agent = Agent(name="Echo Agent", instructions="Return the words 'Setup successful'")
result = Runner.run_sync(agent, "Run setup")
print(result.final_output)