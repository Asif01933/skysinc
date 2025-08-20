from sqlalchemy import Column, Integer, String, DateTime, func
from app.db.base import Base

class Booking(Base):
    __tablename__ = 'bookings'
    
    id = Column(Integer, primary_key = True, index=True)
    user_id = Column(Integer, nullable = False)
    flight_id = Column(Integer, nullable=False)
    status = Column(String, default='pending')
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())