from src.models import SearchResultswModel
from src.services.alphavantage_service import AlphaVantageService

alpha_vantage_service = AlphaVantageService()


def handle_request(event, context):
    search_results = alpha_vantage_service.search_symbol(
        event["arguments"]["searchText"]
    )
    return [SearchResultswModel.dump(result) for result in search_results]
