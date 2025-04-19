from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv
load_dotenv()

# This function initialize the search tool . Which performs search and return results.
def load_tavily_search_tool(tavily_search_max_results:int):
    return TavilySearchResults(max_results=tavily_search_max_results)