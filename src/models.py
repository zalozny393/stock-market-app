from abc import ABC
from dataclasses import dataclass, field

import marshmallow_dataclass
from marshmallow import Schema


def camelcase(s):
    parts = iter(s.split("_"))
    return next(parts) + "".join(i.title() for i in parts)


class BaseSchema(Schema):
    """Schema that uses camel-case for its external representation
    and snake-case for its internal representation.
    """

    def on_bind_field(self, field_name, field_obj):
        field_obj.data_key = (
            field_obj.data_key if field_obj.data_key else camelcase(field_name)
        )


class BaseModel(ABC):
    @classmethod
    def get_schema(cls):
        return marshmallow_dataclass.class_schema(cls, base_schema=BaseSchema)()

    @classmethod
    def load(cls, data: dict):
        return cls.get_schema().load(data)

    @classmethod
    def dump(cls, data: dict):
        return cls.get_schema().dump(data)


@dataclass
class CompanyOverviewModel(BaseModel):
    symbol: str = field()
    name: str = field()
    description: str = field()
    currency: str = field()
    sector: str = field()
    pe_ratio: float = field(metadata={"data_key": "PERatio"})
    profit_margin: float = field()
    high_52_week: float = field()
    low_52_week: float = field()
    moving_200_day_average: float = field()
    beta: float = field()
    dividend_yield: float = field()
