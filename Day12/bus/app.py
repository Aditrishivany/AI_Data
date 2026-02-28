from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import engine, SessionLocal, Base
from models import Bus, Booking

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/addbus")
def add_bus(bus: dict):

    if "name" not in bus:
        raise HTTPException(status_code=400, detail="Bus name required")

    db: Session = SessionLocal()

    new_bus = Bus(name=bus["name"])
    db.add(new_bus)
    db.commit()
    db.refresh(new_bus)
    db.close()

    return {"message": "Bus added successfully", "bus": {"id": new_bus.id, "name": new_bus.name}}


@app.get("/buses")
def get_all_buses():

    db: Session = SessionLocal()
    buses = db.query(Bus).all()
    db.close()

    return {"available_buses": [{"id": b.id, "name": b.name} for b in buses]}

@app.post("/bookseat")
def book_seat(data: dict):

    required = ["bus_id", "passenger_name", "seat_number"]

    for field in required:
        if field not in data:
            raise HTTPException(status_code=400, detail=f"{field} is required")

    db: Session = SessionLocal()

    bus = db.query(Bus).filter(Bus.id == data["bus_id"]).first()
    if not bus:
        db.close()
        raise HTTPException(status_code=404, detail="Bus not found")

    existing = db.query(Booking).filter(
        Booking.bus_id == data["bus_id"],
        Booking.seat_number == data["seat_number"]
    ).first()

    if existing:
        db.close()
        raise HTTPException(status_code=400, detail="Seat already booked")

    booking = Booking(
        bus_id=data["bus_id"],
        passenger_name=data["passenger_name"],
        seat_number=data["seat_number"]
    )

    db.add(booking)
    db.commit()
    db.refresh(booking)
    db.close()

    return {
        "message": "Seat booked successfully",
        "booking": {
            "booking_id": booking.id,
            "bus_id": booking.bus_id,
            "passenger": booking.passenger_name,
            "seat_number": booking.seat_number
        }
    }


@app.put("/bookseat/{booking_id}")
def change_seat(booking_id: int, data: dict):

    if "new_seat_number" not in data:
        raise HTTPException(status_code=400, detail="new_seat_number required")

    db: Session = SessionLocal()

    booking = db.query(Booking).filter(Booking.id == booking_id).first()

    if not booking:
        db.close()
        raise HTTPException(status_code=404, detail="Booking not found")

    seat_taken = db.query(Booking).filter(
        Booking.bus_id == booking.bus_id,
        Booking.seat_number == data["new_seat_number"]
    ).first()

    if seat_taken:
        db.close()
        raise HTTPException(status_code=400, detail="Seat already taken")

    booking.seat_number = data["new_seat_number"]

    db.commit()
    db.refresh(booking)
    db.close()

    return {
        "message": "Seat changed successfully",
        "updated_booking": {
            "booking_id": booking.id,
            "new_seat_number": booking.seat_number
        }
    }


@app.get("/bookseat/{booking_id}")
def confirm_booking(booking_id: int):

    db: Session = SessionLocal()

    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    db.close()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    return {
        "message": "Booking confirmed",
        "booking_details": {
            "booking_id": booking.id,
            "bus_id": booking.bus_id,
            "passenger": booking.passenger_name,
            "seat_number": booking.seat_number
        }
    }