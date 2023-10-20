from pydantic.types import StrictInt

from pandantic import BaseModel
import pandas as pd


class DataFrameSchema(BaseModel):
    """Example schema for testing."""

    example_str: str
    example_int: StrictInt


def main() -> None:
    df_invalid = pd.DataFrame(
        data={
            "example_str": ["foo", "bar", "1"],
            "example_int": ["1", 2, 3.0],
        }
    )

    df_valid = pd.DataFrame(
        data={
            "example_str": ["foo", "bar", 1],
            "example_int": [1, 2, 3],
        }
    )

    df_filtered = DataFrameSchema.parse_df(
        dataframe=df_invalid,
        errors="filter",
    )

    df_filtered_2 = DataFrameSchema.parse_df(
        dataframe=df_valid,
        errors="filter",
    )

    print(df_filtered)

    print(df_filtered_2)


if __name__ == "__main__":
    main()
