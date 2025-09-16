from agents import Agent, Runner
from agents.model_settings import ModelSettings

# create agents
creative_agent = Agent(
    name="CreativeAgent",
    instructions="You are an AI agent that answers questions.",
    model="gpt-4o",
    model_settings=ModelSettings(
        temperature=1.0,
        max_tokens=300
    )
)

precise_agent = Agent(
    name="PreciseAgent",
    instructions="You are an AI agent that answers questions.",
    model="gpt-4o",
    model_settings=ModelSettings(
        temperature=0.2,
        max_tokens=50
    )
)

prompt = "Describe the future of AI in customer service."

print("Creative agent:")
response = Runner.run_sync(creative_agent, prompt)
print(response.final_output)
print("---")

print("Precise agent:")
response = Runner.run_sync(precise_agent, prompt)
print(response.final_output)
print("---")
