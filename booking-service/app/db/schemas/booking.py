from pydantic import BaseModel
from datetime import datetime

class BookingCreate(BaseModel):
    flight_id: int


class BookingResponse(BaseModel):
    id:int
    user_id: int
    flight_id: int
    status: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True