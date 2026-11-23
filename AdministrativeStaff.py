
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Base import Base
from RoomBooking import RoomBooking

class AdministrativeStaff(Base):
    # Specify table name
    __tablename__ = "AdministrativeStaff"

    # Define data base columns
    staff_id: Mapped[int] = mapped_column(
        "StaffID", Integer, primary_key=True
    )

    email: Mapped[str] = mapped_column(
        "Email", String(100), nullable=False, unique=True
    )

    first_name: Mapped[str] = mapped_column(
        "FirstName", String(100), nullable=False
    )

    last_name: Mapped[str] = mapped_column(
        "LastName", String(100), nullable=False
    )

    # Define relationship to RoomBooking (1:N)
    room_bookings: Mapped[list["RoomBooking"]] = relationship(
        "RoomBooking",
        back_populates="staff"
    )
