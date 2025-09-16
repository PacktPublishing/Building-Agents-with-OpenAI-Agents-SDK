# Required imports
import os
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool

# Load environment variables from the .env file
load_dotenv()

# Access the API key
api_key = os.getenv("OPENAI_API_KEY")

# Create a tool
@function_tool(
        name_override="Get Status of Current Order",
        description_override="Returns the status of an order given the customer's Order ID",
        docstring_style="Args: Order ID in Integer format"
)
def get_order_status(orderID: int) -> str:
    """  
    Returns the order status given an order ID
    Args:
        orderID (int) - Order ID of the customer's order
    Returns:
        string - Status message of the customer's order
    """
    if orderID in (100, 101):
        return "Delivered"
    elif orderID in (200, 201):
        return "Delayed"
    elif orderID in (300, 301):
        return "Cancelled"
    
# Define an agent
agent = Agent(name="Customer service agent", 
              instructions="You are an AI Agent that helps respond to customer queries for a local paper company",
              model="gpt-4o",
              tools=[get_order_status])

# Run the Control Logic Framework
result = Runner.run_sync(agent, "What's the status or my order? My Order ID is 200")

# Print the result
print(result.final_output)