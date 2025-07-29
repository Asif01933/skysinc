from sqlalchemy import Column, Integer, String, Float, DateTime
from app.db.base import Base

class Flight(Base):
    __tablename__ = "flights"
    
    id = Column(Integer, primary_key=True, index=True)
    origin = Column(String, index=True)
    destination = Column(String, index=True)
    departure_time = Column(DateTime)
    price = Column(Float)
    seats_available = Column(Integer)