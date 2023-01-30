from src.services.alphavantage_service import AlphaVantageService

alpha_vantage_service = AlphaVantageService()


def handle_request(event, context):
    company_overview = alpha_vantage_service.get_company_overview(
        event["arguments"]["symbol"]
    )
    return company_overview.dict(by_alias=True)
