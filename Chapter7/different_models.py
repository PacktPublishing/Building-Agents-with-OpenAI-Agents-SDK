from agents import Agent, Runner
import time

# Create two agents
gpt4o_agent = Agent(
    name="GPT4o Agent",
    instructions="You are an AI Agent",
    model="gpt-4o"
)
o3pro_agent = Agent(
    name="o3-pro Agent",
    instructions="You are an AI Agent",
    model="gpt-4o"
)

prompt = "How many integers from 1 to 10000 (inclusive) are divisible by 3 or by 5 but not by both? Do reasoning but only return only the answer."

print("gpt4o agent")
start_fast = time.time()
response = Runner.run_sync(gpt4o_agent, prompt)
print(response.final_output)
end_fast = time.time()
print(f"Time taken: {end_fast - start_fast:.2f} seconds")
print("---")

start_fast = time.time()
print("o3pro agent")
response = Runner.run_sync(o3pro_agent, prompt)
print(response.final_output)
end_fast = time.time()
print(f"Time taken: {end_fast - start_fast:.2f} seconds")
print("---")