from agents import Agent, Runner, SQLiteSession

# Create two agents
complaints_agent = Agent(
    name="Complaints Agent",
    instructions="Handle any customer complaints with empathy and clear next steps."
)
inquiry_agent = Agent(
    name="General Inquiry Agent",
    instructions="Answer general questions about our services promptly."
)

# Create orchestration
def orchestrate(user_message: str):
    # Deterministically redirects requests to the right agent.
    if "complaint" in user_message.lower() or "problem" in user_message.lower():
        print('Redirecting you to the Complaints agent')
        chosen_agent = complaints_agent
    else:
        print('Redirecting you to the Inquiry agent')
        chosen_agent = inquiry_agent
    result = Runner.run_sync(chosen_agent, user_message)
    return result.final_output

while True:
    question = input("You: ")
    result = orchestrate(question)
    print("Agent: ", result)