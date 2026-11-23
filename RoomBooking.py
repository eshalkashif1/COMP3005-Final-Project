
from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    DateTime,
    ForeignKey,
    CheckConstraint
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Base import Base
from AdministrativeStaff import AdministrativeStaff
from Room import Room


class RoomBooking(Base):
    # Specify table name
    __tablename__ = "RoomBooking"

    # Define data base columns
    booking_id: Mapped[int] = mapped_column(
        "BookingID", Integer, primary_key=True
    )

    staff_id: Mapped[int] = mapped_column(
        "StaffID",
        Integer,
        ForeignKey("AdministrativeStaff.StaffID"),
        nullable=False
    )

    room_id: Mapped[int] = mapped_column(
        "RoomID",
        Integer,
        ForeignKey("Room.RoomID"),
        nullable=False
    )

    start_time: Mapped[datetime] = mapped_column(
        "StartTime", DateTime, nullable=False
    )

    end_time: Mapped[datetime] = mapped_column(
        "EndTime", DateTime, nullable=False
    )

    booking_type: Mapped[str] = mapped_column(
        "BookingType", String(100), nullable=False
    )

    status: Mapped[str] = mapped_column(
        "Status", String(100), nullable=False
    )

    __table_args__ = (
        # Ensure that the end time is after the start time
        CheckConstraint(
            "EndTime > StartTime",
            name="check_booking_time"
        ),
    )

    # Define relationships to AdministrativeStaff (N:1)
    staff: Mapped["AdministrativeStaff"] = relationship(
        "AdministrativeStaff",
        back_populates="room_bookings"
    )

    # Define relationships to Room (N:1)
    room: Mapped["Room"] = relationship(
        "Room",
        back_populates="room_bookings"
    )