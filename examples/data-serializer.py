from datetime import datetime
from pydantic import BaseModel, field_serializer


class BroadwayTicket(BaseModel):
    show_name: str
    show_time: datetime

    @field_serializer("show_time")
    def transform_show_time(v) -> str:
        """Returns human readable show time format"""
        return v.strftime("%b %d, %Y, %I:%M %p")


def main() -> None:
    # Create an object
    my_tickets = BroadwayTicket(
        show_name="Parade", show_time=datetime(2023, 8, 5, 19)  # August 8, 7:00PM
    )

    print(my_tickets.model_dump())
    # {'show_name': 'Parade', 'show_time': 'Aug 05, 2023, 07:00 PM'}


if __name__ == "__main__":
    main()
