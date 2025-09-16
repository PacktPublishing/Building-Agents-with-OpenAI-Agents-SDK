from agents import Agent, Runner, SQLiteSession

# Create the agent
agent = Agent(
    name="QuestionAnswer",
    instructions="You are an AI agents that answers questions.",
)

# Create a session
session = SQLiteSession("first_session", db_path="messages.db")

while True:
    question = input("You: ")
    result = Runner.run_sync(agent, question, session=session)
    print("Agent: ", result.final_output)