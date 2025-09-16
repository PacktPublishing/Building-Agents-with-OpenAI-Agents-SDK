# Required imports
import os
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, trace
from agents import GuardrailFunctionOutput, OutputGuardrailTripwireTriggered, output_guardrail, RunContextWrapper
from pydantic import BaseModel

# Load environment variables from the .env file
load_dotenv()

# Access the API key
api_key = os.getenv("OPENAI_API_KEY")

class MessageOutput(BaseModel): 
    response: str
    
class GuardrailTrueFalse(BaseModel):
    is_relevant_to_customer_service: bool
    
# Create a guardrail agent
guardrail_agent = Agent( 
    name="Guardrail check",
    instructions="You are an AI agent that checks if the agent response is relevant to answering a customer service question and not hallucinating",
    output_type=GuardrailTrueFalse
)

# Create a guardrail
@output_guardrail
async def relevant_detector_guardrail( 
    ctx: RunContextWrapper[None], 
    agent: Agent, 
    output: MessageOutput
) -> GuardrailFunctionOutput:
    
    result = await Runner.run(guardrail_agent, input=output)

    tripwire_triggered = False 

    if result.final_output.is_relevant_to_customer_service == False:
         tripwire_triggered = True

    return GuardrailFunctionOutput(
        output_info="", 
        tripwire_triggered=tripwire_triggered
    ) 

# Define an agent
agent = Agent(name="Customer service agent", 
              instructions="You are an AI Agent that outputs random song lines and poems", # to force model to hallucinate and trigger the output guardrail
              output_guardrails=[relevant_detector_guardrail])

with trace("Output Guardrails"):
    while True:
        try: 
            question = input("You: ")
            result = Runner.run_sync(agent, question)
            print("Agent: ", result.final_output)
        except OutputGuardrailTripwireTriggered:
            print ("The agent system did not produce an output. Please try again")
