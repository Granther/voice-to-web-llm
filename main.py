import os
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from whisper import transcribe
from sound import get_sound

def search_tav(query):
    search = TavilySearchResults(max_results=2)
    search_results = search.invoke("query")

    return search_results

if __name__ == "__main__":
    load_dotenv()
    os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

    get_sound()
    text = transcribe()
    print(text)
    print(search_tav(text))


#tools = [search]