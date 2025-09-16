from agents import Agent, Runner, trace, custom_span, function_tool
from dotenv import load_dotenv
import time

load_dotenv()

@function_tool
def get_fun_facts():
    return "The Eiffel Tower is in Paris"

@function_tool
def clean_up_poem(poem_string: str):
    return poem_string.upper()

# Create the research agent
research_agent = Agent(
    name="Research",
    instructions="You are an AI agent that performs research",
    tools=[get_fun_facts]
)

# Create the text generation agent
text_generation_agent = Agent(
    name="Text Generation",
    instructions="You are an AI agent that pertakes research that's performed and writes a poem",
    tools=[clean_up_poem]
)

with trace("Henry's Research Workflow"):
    with custom_span("Research Task"):
        result = Runner.run_sync(research_agent, "The Eiffel Tower")
    with custom_span("Text Generation Task"):
        result = Runner.run_sync(text_generation_agent, result.final_output)
    print(result.final_output)