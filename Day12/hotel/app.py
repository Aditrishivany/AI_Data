from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import engine, SessionLocal, Base
from models import Hotel, HotelBooking

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/addhotel")
def add_hotel(hotel: dict):

    if "name" not in hotel or "location" not in hotel:
        raise HTTPException(status_code=400, detail="Hotel name and location required")

    db: Session = SessionLocal()

    new_hotel = Hotel(
        name=hotel["name"],
        location=hotel["location"]
    )

    db.add(new_hotel)
    db.commit()
    db.refresh(new_hotel)
    db.close()

    return {
        "message": "Hotel added successfully",
        "hotel": {
            "id": new_hotel.id,
            "name": new_hotel.name,
            "location": new_hotel.location
        }
    }


@app.get("/hotels")
def get_all_hotels():

    db: Session = SessionLocal()
    hotels = db.query(Hotel).all()
    db.close()

    return {
        "available_hotels": [
            {"id": h.id, "name": h.name, "location": h.location}
            for h in hotels
        ]
    }


@app.post("/bookroom")
def book_room(data: dict):

    required = ["hotel_id", "guest_name", "room_number"]
    for field in required:
        if field not in data:
            raise HTTPException(status_code=400, detail=f"{field} is required")

    db: Session = SessionLocal()

    hotel = db.query(Hotel).filter(Hotel.id == data["hotel_id"]).first()
    if not hotel:
        db.close()
        raise HTTPException(status_code=404, detail="Hotel not found")

    room_taken = db.query(HotelBooking).filter(
        HotelBooking.hotel_id == data["hotel_id"],
        HotelBooking.room_number == data["room_number"]
    ).first()

    if room_taken:
        db.close()
        raise HTTPException(status_code=400, detail="Room already booked")

    booking = HotelBooking(
        hotel_id=data["hotel_id"],
        guest_name=data["guest_name"],
        room_number=data["room_number"]
    )

    db.add(booking)
    db.commit()
    db.refresh(booking)
    db.close()

    return {
        "message": "Room booked successfully",
        "booking": {
            "booking_id": booking.id,
            "hotel_id": booking.hotel_id,
            "guest": booking.guest_name,
            "room_number": booking.room_number
        }
    }


@app.put("/bookroom/{booking_id}")
def change_room(booking_id: int, data: dict):

    if "new_room_number" not in data:
        raise HTTPException(status_code=400, detail="new_room_number required")

    db: Session = SessionLocal()

    booking = db.query(HotelBooking).filter(
        HotelBooking.id == booking_id
    ).first()

    if not booking:
        db.close()
        raise HTTPException(status_code=404, detail="Booking not found")

    room_taken = db.query(HotelBooking).filter(
        HotelBooking.hotel_id == booking.hotel_id,
        HotelBooking.room_number == data["new_room_number"]
    ).first()

    if room_taken:
        db.close()
        raise HTTPException(status_code=400, detail="Room already taken")

    booking.room_number = data["new_room_number"]
    db.commit()
    db.refresh(booking)
    db.close()

    return {
        "message": "Room changed successfully",
        "new_room_number": booking.room_number
    }


@app.get("/bookroom/{booking_id}")
def confirm_booking(booking_id: int):

    db: Session = SessionLocal()

    booking = db.query(HotelBooking).filter(
        HotelBooking.id == booking_id
    ).first()
    db.close()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    return {
        "message": "Booking confirmed",
        "booking_details": {
            "booking_id": booking.id,
            "hotel_id": booking.hotel_id,
            "guest": booking.guest_name,
            "room_number": booking.room_number
        }
    }