from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults


from langgraph.prebuilt import create_react_agent

from langchain_core.messages import AIMessage, HumanMessage

from app.config.settings import settings

def get_response_from_agents(llm_id, query, allow_search, system_prompt):
    llm = ChatGroq(model_name=llm_id, api_key=settings.GROQ_API_KEY)
    tools = [TavilySearchResults(api_key=settings.TAV_API_KEY,max_results=5)] if allow_search else []

    agent= create_react_agent(llm, tools, prompt=system_prompt)

    state = {"messages": query}

    response = agent.invoke(state)

    messages = response.get("messages")

    ai_message = [message for message in messages if isinstance(message, AIMessage)]

    return ai_message[-1].content