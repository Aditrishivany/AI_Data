from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from models import Flight, FlightBooking

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/addflight")
def add_flight(flight: dict):

    if "airline" not in flight:
        raise HTTPException(status_code=400, detail="Airline name required")

    db: Session = SessionLocal()

    new_flight = Flight(airline=flight["airline"])
    db.add(new_flight)
    db.commit()
    db.refresh(new_flight)
    db.close()

    return {
        "message": "Flight added successfully",
        "flight": {
            "id": new_flight.id,
            "airline": new_flight.airline
        }
    }


@app.get("/flights")
def get_all_flights():
    db: Session = SessionLocal()

    flights = db.query(Flight).all()
    db.close()

    return {"available_flights": [{"id": f.id, "airline": f.airline} for f in flights]}


@app.post("/bookflightseat")
def book_flight_seat(data: dict):

    required = ["flight_id", "passenger_name", "seat_number"]
    for field in required:
        if field not in data:
            raise HTTPException(status_code=400, detail=f"{field} is required")

    db: Session = SessionLocal()

    flight = db.query(Flight).filter(Flight.id == data["flight_id"]).first()
    if not flight:
        db.close()
        raise HTTPException(status_code=404, detail="Flight not found")

    seat_taken = db.query(FlightBooking).filter(
        FlightBooking.flight_id == data["flight_id"],
        FlightBooking.seat_number == data["seat_number"]
    ).first()

    if seat_taken:
        db.close()
        raise HTTPException(status_code=400, detail="Seat already booked")

    booking = FlightBooking(
        flight_id=data["flight_id"],
        passenger_name=data["passenger_name"],
        seat_number=data["seat_number"]
    )

    db.add(booking)
    db.commit()
    db.refresh(booking)
    db.close()

    return {
        "message": "Flight seat booked successfully",
        "booking": {
            "booking_id": booking.id,
            "flight_id": booking.flight_id,
            "passenger": booking.passenger_name,
            "seat": booking.seat_number
        }
    }


@app.put("/bookflightseat/{booking_id}")
def change_flight_seat(booking_id: int, data: dict):

    if "new_seat_number" not in data:
        raise HTTPException(status_code=400, detail="new_seat_number required")

    db: Session = SessionLocal()

    booking = db.query(FlightBooking).filter(FlightBooking.id == booking_id).first()
    if not booking:
        db.close()
        raise HTTPException(status_code=404, detail="Booking not found")

    seat_taken = db.query(FlightBooking).filter(
        FlightBooking.flight_id == booking.flight_id,
        FlightBooking.seat_number == data["new_seat_number"]
    ).first()

    if seat_taken:
        db.close()
        raise HTTPException(status_code=400, detail="Seat already taken")

    booking.seat_number = data["new_seat_number"]
    db.commit()
    db.refresh(booking)
    db.close()

    return {"message": "Flight seat changed", "new_seat": booking.seat_number}


@app.get("/bookflightseat/{booking_id}")
def confirm_flight_booking(booking_id: int):

    db: Session = SessionLocal()

    booking = db.query(FlightBooking).filter(FlightBooking.id == booking_id).first()
    db.close()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    return {
        "message": "Flight booking confirmed",
        "details": {
            "booking_id": booking.id,
            "flight_id": booking.flight_id,
            "passenger": booking.passenger_name,
            "seat": booking.seat_number
        }
    }