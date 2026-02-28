from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)


class HotelBooking(Base):
    __tablename__ = "hotel_bookings"

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"))
    guest_name = Column(String, nullable=False)
    room_number = Column(Integer, nullable=False)