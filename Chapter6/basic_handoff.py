from agents import Agent, Runner

# Create two agents
complaints_agent = Agent(
    name="Complaints Agent",
    instructions="Introduce yourself as the complaints agent. Handle any customer complaints with empathy and clear next steps."
)
inquiry_agent = Agent(
    name="General Inquiry Agent",
    instructions="Introduce yourself as the inquiry agent. Answer general questions about our services promptly."
)

# Create the triage agent with handoffs
triage_agent = Agent(
    name="Triage Agent",
    instructions="Triage the user's request and call the appropriate agent",
    handoffs=[complaints_agent, inquiry_agent]
)

while True:
    question = input("You: ")
    result = Runner.run_sync(triage_agent, question)
    print("Agent: ", result.final_output)