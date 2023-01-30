import abc

from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field


def to_camel(string: str) -> str:
    parts = iter(string.split("_"))
    return next(parts) + "".join(i.title() for i in parts)


class BaseModel(PydanticBaseModel, metaclass=abc.ABCMeta):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class CompanyOverviewModel(BaseModel):
    symbol: str
    name: str
    description: str
    currency: str
    sector: str
    pe_ratio: float = Field(alias="PERatio")
    profit_margin: float
    high_52_week: float
    low_52_week: float
    moving_200_day_average: float
    beta: float
    dividend_yield: float


class SearchResultswModel(BaseModel):
    symbol: str
    name: str
    type: str
    region: str
    currency: str
