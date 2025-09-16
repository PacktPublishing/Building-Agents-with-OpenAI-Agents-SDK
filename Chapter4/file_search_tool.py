from agents import Agent, Runner, FileSearchTool

# Instantiate the tool
filesearchtool = FileSearchTool(vector_store_ids=['vs_686ce7bc2ad081918f297d962afaee95']) # replace with your own vector store ID

# Create an agent
agent = Agent(
    name="WebTool",
    instructions="You are an AI agent that answers questions from the listed vector stores. Answer in one sentence.",
    tools=[filesearchtool]
)

result = Runner.run_sync(agent, "How high can you fly this drone?")
print(result.final_output)