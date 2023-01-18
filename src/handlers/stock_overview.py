import os

from src.services.alphavantage_service import AlphaVantageService

if os.environ.get("IS_OFFLINE") == "true" and os.environ.get("LOCAL_DEBUG") == "true":
    import debugpy

    debugpy.listen(5678)
    debugpy.wait_for_client()


alpha_vantage_service = AlphaVantageService()


def handle_request(event, context):
    data = alpha_vantage_service.get_company_overview(event["arguments"]["symbol"])
    return {
        "symbol": data["Symbol"],
        "name": data["Name"],
        "description": data["Description"],
        "currency": data["Currency"],
        "sector": data["Sector"],
        "PERatio": data["PERatio"],
        "profitMargin": data["ProfitMargin"],
        "High52Week": data["52WeekHigh"],
        "Low52Week": data["52WeekLow"],
        "Moving200DayAverage": data["200DayMovingAverage"],
        "beta": data["Beta"],
        "dividendYield": data["DividendYield"],
    }
