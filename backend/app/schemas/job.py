from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class JobBase(BaseModel):
    company: str
    title: str
    status: Optional[str] = None
    date_applied: Optional[datetime] = None
    
    
class JobCreate(JobBase):
    pass

class JobUpdate(JobBase):
    pass

class JobOut(JobBase):
    id: int

    class Config:
        orm_mode = True