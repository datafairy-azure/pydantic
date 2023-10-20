from datetime import datetime
from typing import Tuple

from pydantic import BaseModel, PositiveInt, ValidationError


class Delivery(BaseModel):
    timestamp: datetime
    dimensions: Tuple[int, int]


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]


def main() -> None:
    m = Delivery(timestamp="2020-01-02T03:04:05Z", dimensions=["10", "20"])

    print(repr(m.timestamp))
    print(m.dimensions)

    external_data = {
        "id": 123,
        "signup_ts": "2019-06-01 12:22",
        "tastes": {
            "wine": 9,
            b"cheese": 7,
            "cabbage": "1",
        },
    }

    user = User(**external_data)

    print(user.id)
    print(user.model_dump())

    external_data_invalid = {"id": "not an int", "tastes": {}}

    try:
        User(**external_data_invalid)
    except ValidationError as e:
        print(e.errors())


if __name__ == "__main__":
    main()
