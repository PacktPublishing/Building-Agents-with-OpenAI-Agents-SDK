# Required imports
from typing import List
from pydantic import BaseModel
from agents import Agent, Runner, function_tool

# Define the first tool to get all orders for a given customer
@function_tool
def get_customer_orders(customer_id: str) -> str:
    """
    Retrieve all order IDs associated with a given customer ID.
    Args:
        customer_id: the customer ID
    """
    # Dummy implementation
    if customer_id == "CUST123":
        return ["ORD001", "ORD002", "ORD003"]

# Define the second tool to get status of a specific order
@function_tool
def get_order_information(order_id: str) -> str:
    """
    Fetch detailed information about a specific order.
    """
    # Dummy implementation
    status_map = {
        "ORD001": "Shipped",
        "ORD002": "Processing",
        "ORD003": "Delivered"
    }
    return f"Order {order_id} is currently {status_map.get(order_id, 'Unknown')}."

# Define the agent
customer_service_agent = Agent(
    name="CustomerSupportAgent",
    instructions="You are a customer service assistant.",
    tools=[get_customer_orders, get_order_information]
)

# Run the agent
result = Runner.run_sync(customer_service_agent, "Please check the status of my orders? My customer ID is CUST123.")
print(result.final_output)
