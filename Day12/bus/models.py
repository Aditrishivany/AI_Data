from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Bus(Base):
    __tablename__ = "buses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)

    bus_id = Column(Integer, ForeignKey("buses.id"))
    passenger_name = Column(String, nullable=False)
    seat_number = Column(Integer, nullable=False)