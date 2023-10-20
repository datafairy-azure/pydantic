from typing import Any
from typing_extensions import Annotated

from pydantic import BaseModel
from pydantic.functional_validators import AfterValidator, BeforeValidator


def remove_currency(v: Any) -> int:
    """Remove currency symbol from any input"""
    if isinstance(v, str):
        v = v.replace("$", "")
    return v


def truncate_max_number(v: int) -> int:
    """Any number greater than 100 will be set at 100"""
    return min(v, 100)


# Create a custom type (importable!)
Price = Annotated[
    int, BeforeValidator(remove_currency), AfterValidator(truncate_max_number)
]


class Model(BaseModel):
    price: Price


# Instantiate the model to demonstrate
m = Model(price="$12")  # price=12
m = Model(price=12)  # price=12
m = Model(price=101)  # price=100
print(m)
