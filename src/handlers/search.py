import os

from src.models import SearchResultswModel
from src.services.alphavantage_service import AlphaVantageService

if os.environ.get("IS_OFFLINE") == "true" and os.environ.get("LOCAL_DEBUG") == "true":
    import debugpy

    debugpy.listen(5678)
    debugpy.wait_for_client()


alpha_vantage_service = AlphaVantageService()


def handle_request(event, context):
    search_results = alpha_vantage_service.search_symbol(
        event["arguments"]["searchText"]
    )
    return [SearchResultswModel.dump(result) for result in search_results]
