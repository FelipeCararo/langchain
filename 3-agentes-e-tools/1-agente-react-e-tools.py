from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from dotenv import load_dotenv
load_dotenv()

@tool("calculator", return_direct=True)
def calculator(expression: str) -> str:
    """Evaluate a simple mathematical expression and return the result as a string."""
    try:
        result = eval(expression)  # cuidado: apenas para exemplo didático
    except Exception as e:
        return f"Error: {e}"
    return str(result)

@tool("web_search_mock")
def web_search_mock(query: str) -> str:
    """Return the capital of a given country if it exists in the mock data."""
    data = {
        "Brazil": "Brasília",
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "United States": "Washington, D.C."
    }
    for country, capital in data.items():
        if country.lower() in query.lower():
            return f"The capital of {country} is {capital}."
    return "I don't know the capital of that country."


llm = ChatOpenAI(model="gpt-5-mini", disable_streaming=True)
tools = [calculator, web_search_mock]

system_prompt = (
    "Only use the information you get from the tools, even if you know the answer. "
    "If the information is not provided by the tools, say you don't know. "
    "Never search the internet. Only use the tools provided."
)

agent = create_agent(llm, tools, system_prompt=system_prompt)

result1 = agent.invoke({"messages": [("user", "What is the capital of Iran?")]})
print(result1["messages"][-1].content)

result2 = agent.invoke({"messages": [("user", "How much is 10 + 10?")]})
print(result2["messages"][-1].content)
