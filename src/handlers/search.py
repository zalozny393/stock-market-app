from src.services.alphavantage_service import AlphaVantageService

alpha_vantage_service = AlphaVantageService()


def handle_request(event, context):
    search_results = alpha_vantage_service.search_symbol(
        event["arguments"]["searchText"]
    )
    return [result.dict(by_alias=True) for result in search_results]
