import requests
from agents import Agent, Runner, function_tool

# Create the tool
@function_tool
def get_price_of_bitcoin() -> str:
    """Get the price of Bitcoin."""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    price = response.json()["bitcoin"]["usd"]
    return f"${price:,.2f} USD."

# Create the agent
crypto_agent = Agent(
    name="CryptoTracker",
    instructions="You are a crypto assistant. Use tools to get real-time data.",
    tools=[get_price_of_bitcoin]
)

# Run the agent with an example prompt
result = Runner.run_sync(crypto_agent, "What's the price of Bitcoin?")
print(result.final_output)
