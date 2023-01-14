import os
from urllib.parse import urlencode
import requests


if os.environ.get("IS_OFFLINE") == "true" and os.environ.get("LOCAL_DEBUG") == "true":
    import debugpy

    debugpy.listen(5678)
    debugpy.wait_for_client()


def handle_request(event, context):
    params = {
        "function": "SYMBOL_SEARCH",
        "apikey": os.environ.get("ALPHAVANTAGE_API_KEY"),
        "keywords": event["arguments"]["searchText"],
    }
    url = f"https://www.alphavantage.co/query?{urlencode(params)}"
    r = requests.get(url)
    data = r.json()

    search_results = []
    for item in data.get("bestMatches", []):
        search_results.append(
            {
                "symbol": item["1. symbol"],
                "name": item["2. name"],
                "type": item["3. type"],
                "region": item["4. region"],
                "currency": item["8. currency"],
            }
        )

    return search_results
