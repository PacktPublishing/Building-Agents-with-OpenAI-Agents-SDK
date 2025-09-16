# Required imports
import os
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, trace
from agents import GuardrailFunctionOutput, InputGuardrailTripwireTriggered, input_guardrail, RunContextWrapper, TResponseInputItem
from pydantic import BaseModel

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
    
class GuardrailTrueFalse(BaseModel):
    is_relevant_to_customer_service_orders: bool
    
# Create a guardrail agent
guardrail_agent = Agent( 
    name="Guardrail check",
    instructions="You are an AI agent that checks if the user's prompt is relevant to answering customer service and order related questions",
    output_type=GuardrailTrueFalse,
)

# Create a guardrail
@input_guardrail
async def relevant_detector_guardrail( 
    ctx: RunContextWrapper[None], 
    agent: Agent, 
    prompt: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    
    result = await Runner.run(guardrail_agent, input=prompt)

    tripwire_triggered = False 

    if result.final_output.is_relevant_to_customer_service_orders == False:
         tripwire_triggered = True

    return GuardrailFunctionOutput(
        output_info="", 
        tripwire_triggered=tripwire_triggered
    ) 

# Define an agent
agent = Agent(name="Customer service agent", 
              instructions="You are an AI Agent that helps respond to customer queries for a local paper company",
              model="gpt-4o",
              tools=[get_order_status],
              input_guardrails=[relevant_detector_guardrail])

with trace("Input Guardrails"):
    while True:
        try: 
            question = input("You: ")
            result = Runner.run_sync(agent, question)
            print("Agent: ", result.final_output)
        except InputGuardrailTripwireTriggered:
            print ("This comment is irrelevant to customer service.")
