# Required imports
import os
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool
from pydantic import BaseModel

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
    
# Define an agent
agent = Agent(name="Customer service agent", 
              instructions="You are an AI Agent that helps respond to customer queries for a local paper company",
              model="gpt-4o",
              tools=[get_order_status])

# create Scenario class
class Scenario(BaseModel):
    scenario: str
    input: str
    expected_output: str 

list_of_scenarios  = [
    Scenario(
        scenario="Delivered example",
        input="Hi there, could you check my customer order? It's 101",
        expected_output="The order is delivered"
    ),
    Scenario(
        scenario="Delayed",
        input="My order ID is two hundred, why has my package not been delivered yet?",
        expected_output="The order is delayed"
    ),
    Scenario(
        scenario="Order does not exist",
        input="What's the status of my Order? Its number is 400",
        expected_output="No status or order can be found"
    )
]

# create output type 
class OutputTrueFalse(BaseModel):
    test_succeeded: bool

# create testing agent
testing_agent = Agent(name="Testing agent", 
              instructions="You are an AI Agent that tests expected outputs from desired outputs of an agentic AI system",
              output_type=OutputTrueFalse)

# Run test
for scenario in list_of_scenarios:
    print(f"Running scenario {scenario.scenario}")
    result = Runner.run_sync(testing_agent, f"Input: {scenario.input} ||| Expected Output: {scenario.expected_output}")
    print(result.final_output)
    print('---')

from agents import ToolCallItem

# Run a unit test to check if the function_tool was called
result = Runner.run_sync(agent, "Please provide me the status of order 101")

# Inspect items in the result
items = result.new_items

print("Tool calls made during this run:")
for item in items:
    if isinstance(item, ToolCallItem):
        print(f"- {item.raw_item.name} was called")

# Assert that get_order_status was called
if any(item.raw_item.name == "get_order_status" for item in items if isinstance(item, ToolCallItem)):
    print("get_order_status was called as expected")
else:
    print("get_order_status was not called")