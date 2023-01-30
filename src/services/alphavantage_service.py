import logging
import os
from typing import Iterable

from alpha_vantage.fundamentaldata import FundamentalData
from alpha_vantage.timeseries import TimeSeries

from src.models import CompanyOverviewModel, SearchResultswModel

log = logging.getLogger(__name__)


ALPHA_VANTAGE_SYMBOL = "Symbol"
ALPHA_VANTAGE_NAME = "Name"
ALPHA_VANTAGE_DESCRIPTION = "Description"
ALPHA_VANTAGE_CURRENCY = "Currency"
ALPHA_VANTAGE_SECTOR = "Sector"
ALPHA_VANTAGE_PE_RATIO = "PERatio"
ALPHA_VANTAGE_PROFIT_MARGIN = "ProfitMargin"
ALPHA_VANTAGE_52_WEEK_HIGH = "52WeekHigh"
ALPHA_VANTAGE_52_WEEK_LOW = "52WeekLow"
ALPHA_VANTAGE_200_DAY_MOVING_AVERAGE = "200DayMovingAverage"
ALPHA_VANTAGE_BETA = "Beta"
ALPHA_VANTAGE_DIVIDEND_YIELD = "DividendYield"


ALPHA_VANTAGE_SEARCH_RESULT_SYMBOL = "1. symbol"
ALPHA_VANTAGE_SEARCH_RESULT_NAME = "2. name"
ALPHA_VANTAGE_SEARCH_RESULT_TYPE = "3. type"
ALPHA_VANTAGE_SEARCH_RESULT_REGION = "4. region"
ALPHA_VANTAGE_SEARCH_RESULT_CURENCY = "8. currency"


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

        return CompanyOverviewModel(
            symbol=data[ALPHA_VANTAGE_SYMBOL],
            name=data[ALPHA_VANTAGE_NAME],
            description=data[ALPHA_VANTAGE_DESCRIPTION],
            currency=data[ALPHA_VANTAGE_CURRENCY],
            sector=data[ALPHA_VANTAGE_SECTOR],
            pe_ratio=data[ALPHA_VANTAGE_PE_RATIO],
            profit_margin=data[ALPHA_VANTAGE_PROFIT_MARGIN],
            high_52_week=data[ALPHA_VANTAGE_52_WEEK_HIGH],
            low_52_week=data[ALPHA_VANTAGE_52_WEEK_LOW],
            moving_200_day_average=data[ALPHA_VANTAGE_200_DAY_MOVING_AVERAGE],
            beta=data[ALPHA_VANTAGE_BETA],
            dividend_yield=data[ALPHA_VANTAGE_DIVIDEND_YIELD],
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
                SearchResultswModel(
                    symbol=row[ALPHA_VANTAGE_SEARCH_RESULT_SYMBOL],
                    name=row[ALPHA_VANTAGE_SEARCH_RESULT_NAME],
                    type=row[ALPHA_VANTAGE_SEARCH_RESULT_TYPE],
                    region=row[ALPHA_VANTAGE_SEARCH_RESULT_REGION],
                    currency=row[ALPHA_VANTAGE_SEARCH_RESULT_CURENCY],
                )
            )

        return search_results
