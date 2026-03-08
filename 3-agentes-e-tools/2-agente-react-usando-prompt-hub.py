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

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)
tools = [web_search_mock]

agent = create_agent(llm, tools)

result = agent.invoke({"messages": [("user", "What is the capital of Iran?")]})
print(result["messages"][-1].content)
