from agents import Agent, Runner

# Create the agent
agent = Agent(
    name="QuestionAnswer",
    instructions="You are an AI agents that answers questions.",
)

# Create empty list (this will be contain messages)
messages = []

# Initial message, ca;; 
messages.append({"role": "user", "content": "How hot is the sun?"})

# Call agent
result = Runner.run_sync(agent, messages)
print(result.final_output)

# Add response to message
messages.append({"role": "assistant", "content": result.final_output})

# Add second question to message
messages.append({"role": "user", "content": "How big is it?"})

# Call agent
result = Runner.run_sync(agent, messages)
print(result.final_output)