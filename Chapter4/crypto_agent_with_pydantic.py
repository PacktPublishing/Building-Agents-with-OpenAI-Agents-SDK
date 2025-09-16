import requests
from agents import Agent, Runner, function_tool
from pydantic import BaseModel
from typing import List

class Crypto(BaseModel):
    """
    coin_ids: full name string to represent the cryptocurrency
    """
    coin_ids: List[str]


# Create the tool
@function_tool
def get_crypto_prices(crypto: Crypto) -> str:
    """Get the current prices of a list of cryptocurrencies.
    Args:
        Crypto: an object with list of coin_ids (e.g., bitcoinm ethereum, litecoin, etc.)
    """
    ids = ",".join(crypto.coin_ids)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data


# Create the agent
crypto_agent = Agent(
    name="CryptoTracker",
    instructions="You are a crypto assistant. Use tools to get real-time data. When getting cryptocurrency prices, call the tool only once for all requests.",
    tools=[get_crypto_prices]
)

# Run the agent with an example prompt
result = Runner.run_sync(crypto_agent, "What's the price of Bitcoin and Ethereum? Do this in one call")
print(result.final_output)
