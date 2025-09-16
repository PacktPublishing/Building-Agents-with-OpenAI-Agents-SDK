from agents import Agent, Runner
import time

# Create an agent
agent = Agent(
    name="GPT4o Agent",
    instructions="You are an AI Agent",
    model="litellm/anthropic/claude-opus-4-20250514"
)

question = "How do I restart my computer? Answer in a few words."

response = Runner.run_sync(agent, question)
print(response.final_output)
