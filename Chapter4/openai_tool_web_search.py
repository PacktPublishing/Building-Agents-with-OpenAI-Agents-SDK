from agents import Agent, Runner, WebSearchTool

agent = Agent(
    name="WebSearcher",
    instructions="Use web search for any question about recent or factual info.",
    tools=[WebSearchTool()]
)

result = Runner.run_sync(agent, "Who won the Best Picture Oscar in 2024?")
print(result.final_output)
