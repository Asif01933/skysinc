import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.db.models.flight import Flight
from app.db import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

def seed_data():
    db: Session = SessionLocal()
    flights_data = [
        Flight(
            origin="DAC",
            destination="FCO",
            departure_time=datetime.utcnow() + timedelta(days=1),
            price=75.5,
            seats_available=40
        ),
        Flight(
            origin="DAC",
            destination="DXB",
            departure_time=datetime.utcnow() + timedelta(days=2),
            price=65.0,
            seats_available=35
        ),
        Flight(
            origin="DAC",
            destination="CXB",
            departure_time=datetime.utcnow() + timedelta(days=3),
            price=95.0,
            seats_available=25
        ),
    ]
    db.add_all(flights_data)
    db.commit()
    db.close()
    print("✅ Mock flight data inserted.")

if __name__ == "__main__":
    seed_data()