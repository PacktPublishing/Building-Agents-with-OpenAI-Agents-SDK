from agents import Agent, Runner, function_tool
from pydantic import BaseModel
from typing import List

# create a simulated database
TICKETS_DB = {
    "henry@gmail.com": [
        {"id": "TCKT-001", "issue": "Login not working", "status": "resolved"},
        {"id": "TCKT-002", "issue": "Password reset failed", "status": "open"},
    ],
    "tom@gmail.com": [
        {"id": "TCKT-003", "issue": "Billing error", "status": "in progress"},
    ]
}

# define Pydantic model
class CustomerQuery(BaseModel):
    email: str

# define the tool that does a database query
@function_tool
def get_customer_tickets(query: CustomerQuery) -> str:
    """Retrieve recent support tickets for a customer based on email."""
    tickets = TICKETS_DB.get(query.email.lower())
    if not tickets:
        return f"No tickets found for {query.email}."
    response = "\n".join(
        [f"ID: {t['id']}, Issue: {t['issue']}, Status: {t['status']}" for t in tickets]
    )
    return f"Tickets for {query.email}:\n{response}"

# create the agent
support_agent = Agent(
    name="SupportHelper",
    instructions="You are a customer support agent. Use tools to fetch user support history when asked about their tickets.",
    tools=[get_customer_tickets]
)

# Run the agent
result = Runner.run_sync(support_agent, "Can you show me the ticket history for henry@gmail.com?")
print(result.final_output)
