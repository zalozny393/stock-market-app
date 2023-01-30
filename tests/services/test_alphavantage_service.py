import os
from unittest import mock

from src.services.alphavantage_service import *

shopify_company_overview = {
    ALPHA_VANTAGE_SYMBOL: "SHOP",
    ALPHA_VANTAGE_NAME: "Shopify Inc",
    ALPHA_VANTAGE_DESCRIPTION: "Shopify Inc.",
    ALPHA_VANTAGE_CURRENCY: "USD",
    ALPHA_VANTAGE_SECTOR: "TECHNOLOGY",
    ALPHA_VANTAGE_PE_RATIO: "385.23",
    ALPHA_VANTAGE_PROFIT_MARGIN: "-0.612",
    ALPHA_VANTAGE_52_WEEK_HIGH: "98.85",
    ALPHA_VANTAGE_52_WEEK_LOW: "23.63",
    ALPHA_VANTAGE_200_DAY_MOVING_AVERAGE: "36.17",
    ALPHA_VANTAGE_BETA: "1.882",
    ALPHA_VANTAGE_DIVIDEND_YIELD: "0",
}


@mock.patch.dict(os.environ, {"ALPHAVANTAGE_API_KEY": "test"})
@mock.patch(
    "src.services.alphavantage_service.FundamentalData.get_company_overview",
    return_value=(shopify_company_overview, None),
)
def test_company_overview_mapping(mocker):
    alpha_vantage_service = AlphaVantageService()
    company_overview = alpha_vantage_service.get_company_overview("SHOP")
    assert company_overview.symbol == shopify_company_overview[ALPHA_VANTAGE_SYMBOL]
    assert company_overview.name == shopify_company_overview[ALPHA_VANTAGE_NAME]
    assert (
        company_overview.description
        == shopify_company_overview[ALPHA_VANTAGE_DESCRIPTION]
    )
    assert company_overview.currency == shopify_company_overview[ALPHA_VANTAGE_CURRENCY]
    assert company_overview.pe_ratio == float(
        shopify_company_overview[ALPHA_VANTAGE_PE_RATIO]
    )
    assert company_overview.profit_margin == float(
        shopify_company_overview[ALPHA_VANTAGE_PROFIT_MARGIN]
    )
    assert company_overview.high_52_week == float(
        shopify_company_overview[ALPHA_VANTAGE_52_WEEK_HIGH]
    )
    assert company_overview.low_52_week == float(
        shopify_company_overview[ALPHA_VANTAGE_52_WEEK_LOW]
    )
    assert company_overview.beta == float(shopify_company_overview[ALPHA_VANTAGE_BETA])
    assert company_overview.dividend_yield == float(
        shopify_company_overview[ALPHA_VANTAGE_DIVIDEND_YIELD]
    )
