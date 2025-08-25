import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.booking import Booking
from app.db.schemas.booking import BookingCreate, BookingResponse
from app.utils.auth import get_current_user

router = APIRouter()

@router.post("/bookings", response_model=BookingResponse)
def create_booking(
    booking: BookingCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    
    new_booking = Booking(
        user_id=user_id,
        flight_id=booking.flight_id,
        status="CONFIRMED",
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking
