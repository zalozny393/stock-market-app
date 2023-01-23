import logging
import os
from typing import Iterable

from alpha_vantage.fundamentaldata import FundamentalData
from alpha_vantage.timeseries import TimeSeries

from src.models import CompanyOverviewModel, SearchResultswModel

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

    def get_company_overview(self, symbol: str) -> CompanyOverviewModel:
        if not symbol:
            log.error("Symbol is not provided")
            raise AlphaVantageInputErrorException("Symbol is not provided")
        try:
            data, meta_data = self._fundamental_data.get_company_overview(symbol)
        except ValueError as e:
            log.error("Failed to get Company overview", e)
            raise AlphaVantageException(e)

        return CompanyOverviewModel.load(
            {
                "symbol": data["Symbol"],
                "name": data["Name"],
                "description": data["Description"],
                "currency": data["Currency"],
                "sector": data["Sector"],
                "PERatio": data["PERatio"],
                "profitMargin": data["ProfitMargin"],
                "high52Week": data["52WeekHigh"],
                "low52Week": data["52WeekLow"],
                "moving200DayAverage": data["200DayMovingAverage"],
                "beta": data["Beta"],
                "dividendYield": data["DividendYield"],
            }
        )

    def search_symbol(self, search_text: str) -> Iterable[SearchResultswModel]:
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
                SearchResultswModel.load(
                    {
                        "symbol": row["1. symbol"],
                        "name": row["2. name"],
                        "type": row["3. type"],
                        "region": row["4. region"],
                        "currency": row["8. currency"],
                    }
                )
            )

        return search_results
