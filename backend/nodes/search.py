from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_node(state):
    results = []

    try:
        for q in state["search_queries"]:
            response = client.search(
                query=q,
                search_depth="basic",
                max_results=3
            )

            for r in response["results"]:
                results.append({
                    "title": r.get("title"),
                    "body": r.get("content"),
                    "href": r.get("url")
                })

    except Exception as e:
        state["errors"].append(f"Tavily failed: {str(e)}")

    state["results"] = results
    return state