# Required imports
import os
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, trace
from agents import GuardrailFunctionOutput, InputGuardrailTripwireTriggered, input_guardrail, RunContextWrapper, TResponseInputItem

# Load environment variables from the .env file
load_dotenv()

# Access the API key
api_key = os.getenv("OPENAI_API_KEY")

# Create a tool
@function_tool()
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

# Create a guardrail
@input_guardrail
def complaint_detector_guardrail( 
    ctx: RunContextWrapper[None], 
    agent: Agent, 
    prompt: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    
    tripwire_triggered = False 

    if "complaint" in prompt:
         tripwire_triggered = True

    return GuardrailFunctionOutput(
        output_info="The word Complaint has been detected", 
        tripwire_triggered=tripwire_triggered,
    ) 

# Define an agent
agent = Agent(name="Customer service agent", 
              instructions="You are an AI Agent that helps respond to customer queries for a local paper company",
              model="gpt-4o",
              tools=[get_order_status],
              input_guardrails=[ complaint_detector_guardrail])

with trace("Input Guardrails"):
    while True:
        try: 
            question = input("You: ")
            result = Runner.run_sync(agent, question)
            print("Agent: ", result.final_output)
        except InputGuardrailTripwireTriggered:
            print ("The tripwire has been triggered. Please call us instead to register complaints.")
