from agents import Agent, Runner, CodeInterpreterTool
from agents.tool import CodeInterpreter

# Instantiate the tool
tool_config = CodeInterpreter(
    container={"type":"auto"},
    type="code_interpreter"       
)
codetool = CodeInterpreterTool(tool_config=tool_config)

# Create an agent
agent = Agent(
    name="CodeTool",
    instructions="You are an AI agent that writes and runs Python code to answer questions.",
    tools=[codetool]
)

result = Runner.run_sync(agent, "What is my monthly payment for a $800,000 mortgage at 6% for 30 years?")
print(result.final_output)