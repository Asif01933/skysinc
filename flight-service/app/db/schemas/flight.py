from pydantic import BaseModel
from datetime import datetime

class FlightBase(BaseModel):
    origin:str 
    destination:str
    departure_time:datetime
    price:float
    seats_available:int


class FlightCreate(FlightBase):
    pass

class FlightResponse(FlightBase):
    id:int
    
    
    class Config:
        orm_mode = True