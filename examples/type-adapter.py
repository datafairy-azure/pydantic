from typing import List

from pydantic import BaseModel, TypeAdapter


class Item(BaseModel):
    id: int
    name: str


# `item_data` could come from an API call, eg., via something like:
# item_data = requests.get('https://my-api.com/items').json()


def main() -> None:
    """Main function."""
    item_data = [{"id": 1, "name": "My Item"}]

    items = TypeAdapter(List[Item]).validate_python(item_data)

    print(items)


if __name__ == "__main__":
    main()
