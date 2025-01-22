from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio

llm = ChatOpenAI(model="gpt-4o-mini")

async def main():
    agent = Agent(
        task="Find a one-way flight from Bali to Oman on 18 January 2025 on Google Flights. Return me the cheapest option.",
        llm=llm,
        use_vision=False,
        save_conversation_path="logs/conversation.json",
    )
    result = await agent.run()
    print(result)

asyncio.run(main())

# LOOUP AT: 
# https://docs.browser-use.com/introduction
