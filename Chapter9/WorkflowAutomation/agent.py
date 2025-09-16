from agents import Agent, Runner, SQLiteSession, trace, function_tool, WebSearchTool
import sqlite3
from pydantic import BaseModel
from dotenv import load_dotenv
from agents.extensions.visualization import draw_graph
import json

load_dotenv()

@function_tool
def query_users(sql_query: str):
    """
    Executes the given SQL query on the users table and returns the result.
    Table: users
        user_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        location TEXT,
        business_type TEXT,
        phone_number TEXT
    """
    db_path = "customer_details.db"
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()
        conn.close()
        return result
    except Exception as e:
        return f"Error querying users: {e}"
    
@function_tool
def get_user_transcripts(user_id: int) -> str:
    """
    Extracts and returns all transcripts for the given user_id from customer_transcripts.json as one long string.
    """
    json_path = "Chapter9/WorkflowAutomation/customer_transcripts.json"
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        transcripts = [
            conv["transcripts"]
            for conv in data.get("conversations", [])
            if conv.get("user_id") == user_id
        ]
        return "\n\n".join(transcripts) if transcripts else ""
    except Exception as e:
        return f"Error reading transcripts: {e}"


web_search_tool = WebSearchTool()

customer_research_agent = Agent(
    name="Customer Research Agent",
    instructions=(
        "You are an AI agent that performs research on customers to create a customer profile."
        "Given a customer ID, you should create a customer report that:"
            "- retrieves customer details"
            "- reads previous customer transcripts on the customer interests, to be used to personalize emails"
            "- summarized latest news (search the web) on things related to their interests they've noted in the transcript"
    ),
    tools=[web_search_tool, query_users, get_user_transcripts]
)

class EmailOutput(BaseModel):
    to_email: str
    from_email: str
    subject: str
    html_email: str

email_creation_agent = Agent(
    name="Email Creation Agent",
    instructions=(
        "You are an AI agent that generates emails to keep in touch with customers of PaperCo."
        "You goal is to create an email given the information that you have been provided from another agent"
        "Use the information in a subtle way, like you're trying to share with them a news story related to their interests or a personal feature"
        "The goal of the email is to be personable and catch up with them, and also to let them know about our newest offer on Paper Products"
        "The newest offer in Paper products includes a premium subscription plan where all their orders are 10 percent off"
        "The email should be very concise, just a few sentences, and to the point"
    ),
    output_type=EmailOutput,
    model="gpt-4.1-2025-04-14"
)

for user_id in ["1", "2", "3", "4"]:
    with trace(f"Workflow automation agent for user: {user_id}"):
        result = Runner.run_sync(customer_research_agent, input=user_id)
        print(result.final_output)
        email = Runner.run_sync(email_creation_agent, result.final_output)
        print(email.final_output)
        # Write email to a new JSON file with title equal to the user_id
        with open(f"Chapter9/WorkflowAutomation/{user_id}.json", "w", encoding="utf-8") as f:
            json.dump(email.final_output.dict(), f, ensure_ascii=False, indent=2)