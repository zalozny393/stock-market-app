import os

from alpha_vantage.timeseries import TimeSeries

if os.environ.get("IS_OFFLINE") == "true" and os.environ.get("LOCAL_DEBUG") == "true":
    import debugpy

    debugpy.listen(5678)
    debugpy.wait_for_client()


def handle_request(event, context):
    result = TimeSeries(key=os.environ.get("ALPHAVANTAGE_API_KEY")).get_symbol_search(
        keywords=event["arguments"]["searchText"]
    )

    search_results = []
    for _, row in result[0].iterrows():
        search_results.append(
            {
                "symbol": row["1. symbol"],
                "name": row["2. name"],
                "type": row["3. type"],
                "region": row["4. region"],
                "currency": row["8. currency"],
            }
        )
    return search_results
