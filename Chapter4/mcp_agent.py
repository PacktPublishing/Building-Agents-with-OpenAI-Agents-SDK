from agents import Agent, Runner, HostedMCPTool
from agents.tool import Mcp

# Create the tool
tool_config = Mcp(
        server_label="CryptocurrencyPriceFetcher",
        server_url="https://mcp.api.coingecko.com/sse",
        type="mcp",
        require_approval="never"
    )
mcp_tool = HostedMCPTool(tool_config=tool_config)

# Create the agent
agent = Agent(
    name="Crypto Agent",
    instructions="You are an AI agent that returns crypto prices.",
    tools=[mcp_tool]
)

result = Runner.run_sync(agent, "What's the price of bitcoin?")
print(result.final_output)
