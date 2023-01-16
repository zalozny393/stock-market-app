import os

from alpha_vantage.fundamentaldata import FundamentalData

if os.environ.get("IS_OFFLINE") == "true" and os.environ.get("LOCAL_DEBUG") == "true":
    import debugpy

    debugpy.listen(5678)
    debugpy.wait_for_client()


def handle_request(event, context):
    try:
        result = FundamentalData(
            key=os.environ.get("ALPHAVANTAGE_API_KEY")
        ).get_company_overview(symbol=event["arguments"]["symbol"])
        data = result[0]
    except (ValueError, IndexError):
        return

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
    }
