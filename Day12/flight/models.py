from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)
    airline = Column(String, nullable=False)


class FlightBooking(Base):
    __tablename__ = "flight_bookings"

    id = Column(Integer, primary_key=True, index=True)
    flight_id = Column(Integer, ForeignKey("flights.id"))
    passenger_name = Column(String, nullable=False)
    seat_number = Column(Integer, nullable=False)