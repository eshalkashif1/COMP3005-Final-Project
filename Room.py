
from sqlalchemy import Integer, String, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from Base import Base


class Room(Base):
    # Specify table name
    __tablename__ = "Room"

    # Define data base columns
    room_id: Mapped[int] = mapped_column(
        "RoomID", Integer, primary_key=True
    )

    room_name: Mapped[str] = mapped_column(
        "RoomName", String(100), nullable=False
    )

    room_capacity: Mapped[int] = mapped_column(
        "RoomCapacity", Integer, nullable=False
    )

    # Every room must have a capacity greater than 0
    __table_args__ = (
        CheckConstraint(
            "RoomCapacity > 0",
            name="check_room_capacity_positive"
        ),
    )
