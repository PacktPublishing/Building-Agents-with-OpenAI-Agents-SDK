# Required imports
import os
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool

# Load environment variables from the .env file
load_dotenv()

# Access the API key
api_key = os.getenv("OPENAI_API_KEY")

# Create a tool
@function_tool
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
    
# Define the customer retention agent
customer_retention_agent = Agent(
    name="Customer Retention Agent",
    instructions="You are an AI agent that responds to customers that want to close their accounts and retains their business. Be very courteous, relatable, and kind. Offer discounts up to 10% if it helps",
    model="gpt-4.1"
)

# Define an agent
agent = Agent(name="Customer service agent", 
              instructions="You are an AI Agent that helps respond to customer queries for a local paper company",
              model="gpt-4o",
              tools=[get_order_status],
              handoffs=[customer_retention_agent])

# Run the Control Logic Framework
result = Runner.run_sync(agent, "I want to cancel my order and account. You delayed by order for the 3rd time!")

# Print the result
print(result.final_output)