from agents import Agent, Runner, WebSearchTool

# Instantiate the tool
websearchtool = WebSearchTool(user_location={
            "type": "approximate",
            "country": "CA",
            "city": "Toronto",
            "region": "Ontario",
        })

# Create an agent
agent = Agent(
    name="WebTool",
    instructions="You are an AI agent that answers web questions. Answer in one sentence.",
    tools=[websearchtool]
)

result = Runner.run_sync(agent, "What are the top 3 Italian restaurants?")
print(result.final_output)