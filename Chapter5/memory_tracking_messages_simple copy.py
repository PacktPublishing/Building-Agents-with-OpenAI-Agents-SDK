import requests
from agents import Agent, Runner

# Create the agent
agent = Agent(
    name="QuestionAnswer",
    instructions="You are an AI agents that answers questions.",
)

# Initial message
initial_input = "How hot is the sun?"
result = Runner.run_sync(agent, initial_input)
print(result.final_output)

# Create new Runner input by getting the message history and adding a new message
subsequent_question = "How big is it?"
subsequent_input = result.to_input_list() + [{"role": "user", "content": subsequent_question}] 

# Subsequent message 1
result = Runner.run_sync(agent, subsequent_input)
print(result.final_output)

{"role": "user", "content": "How hot is the sun?"}
