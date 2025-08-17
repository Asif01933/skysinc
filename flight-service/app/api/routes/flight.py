from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.schemas.flight import FlightCreate, FlightResponse
from app.db.models.flight import Flight
from app.db.session import get_db
from typing import List
from datetime import datetime
router = APIRouter()

@router.post("/flights", response_model=FlightResponse)
def create_flight(flight: FlightCreate, db: Session = Depends(get_db)):
    db_flight = Flight(**flight.dict())
    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)
    return db_flight


@router.get("/flights/search", response_model=List[FlightResponse])
def search_flights(
    from_: str = Query(..., alias="from"),
    to: str = Query(...),
    db: Session = Depends(get_db)
):
    flights = db.query(Flight).filter(
        Flight.origin.ilike(f"%{from_}%"),
        Flight.destination.ilike(f"%{to}%")

    ).all()
    if not flights:
        raise HTTPException(status_code=404, detail="No flights available")
    return flights



@router.get("/flights/all", response_model=List[FlightResponse])
def search_flights(
    db: Session = Depends(get_db)
):
    flights = db.query(Flight).all()
    return flights