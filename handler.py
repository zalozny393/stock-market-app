import os
import yfinance as yf


if os.environ.get("IS_OFFLINE") == "true" and os.environ.get("LOCAL_DEBUG") == "true":
    import debugpy

    debugpy.listen(5678)
    debugpy.wait_for_client()


def get_stock_info(event, context):
    ticker = yf.Ticker(event["arguments"]["symbol"])

    return {
        "symbol": ticker.info["symbol"],
        "currentPrice": ticker.info["currentPrice"],
        "currency": ticker.info["financialCurrency"],
        "beta": ticker.info["beta"],
        "sector": ticker.info["sector"],
        "longBusinessSummary": ticker.info["longBusinessSummary"],
        "longName": ticker.info["longName"],
        "forwardPE": ticker.info["forwardPE"],
        "trailingPE": ticker.info["trailingPE"],
        "fiveYearAvgDividendYield": ticker.info["fiveYearAvgDividendYield"],
        "logo_url": ticker.info["logo_url"],
    }
