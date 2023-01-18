import logging
import os

from alpha_vantage.fundamentaldata import FundamentalData
from alpha_vantage.timeseries import TimeSeries

log = logging.getLogger(__name__)


class AlphaVantageException(Exception):
    pass


class AlphaVantageInputErrorException(AlphaVantageException):
    pass


class AlphaVantageService:
    def __init__(self) -> None:
        self._fundamental_data = FundamentalData(
            key=os.environ.get("ALPHAVANTAGE_API_KEY")
        )

        self._time_series = TimeSeries(key=os.environ.get("ALPHAVANTAGE_API_KEY"))

    def get_company_overview(self, symbol: str) -> dict:
        if not symbol:
            log.error("Symbol is not provided")
            raise AlphaVantageInputErrorException("Symbol is not provided")
        try:
            data, meta_data = self._fundamental_data.get_company_overview(symbol)
        except ValueError as e:
            log.error("Failed to get Company overview", e)
            raise AlphaVantageException(e)

        return data

    def search_symbol(self, search_text: str) -> dict:
        try:
            findings, meta_data = self._time_series.get_symbol_search(
                keywords=search_text
            )
        except ValueError as e:
            log.error("Failed to get search results", e)
            raise AlphaVantageException(e)

        search_results = []
        for _, row in findings.iterrows():
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
