from agents import Agent, Runner, WebSearchTool

# Instantiate the tool
websearchtool = WebSearchTool()

# Create an agent
agent = Agent(
    name="WebTool",
    instructions="You are an AI agent that answers web questions. Answer in one sentence.",
    tools=[websearchtool]
)

result = Runner.run_sync(agent, "Who won the 2025 Stanley Cup?")
print(result.final_output)