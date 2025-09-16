from agents import Agent, Runner

# Create two agents
complaints_agent = Agent(
    name="Complaints Agent",
    instructions="Handle any customer complaints with empathy and clear next steps."
)
inquiry_agent = Agent(
    name="General Inquiry Agent",
    instructions="Answer general questions about our services promptly."
)
triage_agent = Agent(
    name="Triage Agent",
    instructions="Triage the user's request and call the appropriate agent",
    tools=[
        complaints_agent.as_tool(
            tool_name="ComplaintsAgent",
            tool_description="Introduce yourself as the Complaints agent. Handle any customer complaints with empathy and clear next steps."
        ), 
        inquiry_agent.as_tool(
            tool_name="GeneralInquiryAgent",
            tool_description="Introduce yourself as the General Inquiry agent. Answer general questions about our services promptly." 
        )]
)

while True:
    question = input("You: ")
    result = Runner.run_sync(triage_agent, question)
    print("Agent: ", result.final_output)