from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai


import os
from dotenv import load_dotenv
openai.api_key = os.getenv("OPENAI_API_KEY")


# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama3-qroq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include the sources"],
    show_tool_calls=True,
    markdown=True,    
)


# Financial Agent
financial_agent = Agent(
    name="Financial Agent",
    role="Get financial data",
    model=Groq(id="llama3-qroq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, stock_fundamentals=True, company_news=True, analyst_recommendations=True)],
    instructions=["Use tables to display the data."],
    show_tool_calls=True,
    markdown=True,
)


multi_agent = Agent(
    team=[web_search_agent, financial_agent],
    instructions=["Always include the sources", "Use tables to display the data."],
    show_tool_calls=True,
    markdown=True,
)

multi_agent.print_response("Sunmmarize analyst recommendations and share the latest news for Apple Inc.", stream=True)
