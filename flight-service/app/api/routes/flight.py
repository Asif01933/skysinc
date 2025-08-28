from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.schemas.flight import FlightCreate, FlightResponse
from app.db.models.flight import Flight
from app.db.session import get_db
from typing import List
from datetime import datetime
from app.core.redis import redis_client
from app.core.deps import get_current_user
import json
router = APIRouter()

@router.post("/flights", response_model=FlightResponse)
def create_flight(flight: FlightCreate, db: Session = Depends(get_db)):
    db_flight = Flight(**flight.dict())
    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)
    return db_flight


@router.get("/flights/search", response_model=List[FlightResponse])
async def search_flights(
    from_: str = Query(..., alias="from"),
    to: str = Query(...),
    db: Session = Depends(get_db)
):
    cache_key = f"flights:{from_}:{to}"

   
    cached = await redis_client.get(cache_key)
    if cached:
        return json.loads(cached)

   
    flights = db.query(Flight).filter(
        Flight.origin.ilike(f"%{from_}%"),
        Flight.destination.ilike(f"%{to}%")
    ).all()

    if not flights:
        raise HTTPException(status_code=404, detail="No flights available")

    flights_data = [
        {
            "id": f.id,
            "origin": f.origin,
            "destination": f.destination,
            "price": f.price,
            "departure_time": f.departure_time.isoformat() if f.departure_time else None,
            "seats_available": f.seats_available
        }
        for f in flights
    ]

    
    await redis_client.setex(cache_key, 600, json.dumps(flights_data))

    return flights_data




@router.get("/flights/all", response_model=List[FlightResponse])
def search_flights(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    flights = db.query(Flight).all()
    return flights