import os
import yfinance as yf


if os.environ.get("IS_OFFLINE") == "true" and os.environ.get("LOCAL_DEBUG") == "true":
    import debugpy

    debugpy.listen(5678)
    debugpy.wait_for_client()


def handle_request(event, context):
    symbols = " ".join(event["arguments"]["symbols"])
    tickers = yf.Tickers(symbols)

    stocks_info = []
    for symbol, ticker in tickers.tickers.items():
        if not ticker.info:
            continue
        stocks_info.append(
            {
                "symbol": symbol,
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
        )
    return stocks_info
