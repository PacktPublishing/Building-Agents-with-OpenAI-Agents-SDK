from agents import Agent, Runner
from dotenv import load_dotenv

load_dotenv()

# Create an agent
agent = Agent(
    name="QuestionAnswerAgent",
    instructions="You are an AI agent that answers questions in as few words as possible"
)

result = Runner.run_sync(agent, "Where is the Eiffel Tower?")
print(result.final_output)