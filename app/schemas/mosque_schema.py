from pydantic import BaseModel
from typing import Optional

class MosqueCreateSchema(BaseModel):
    image: Optional[str] = None
    name: str
    type: Optional[str] = None
    lat: float
    long: float
    phone_no: Optional[str] = None
    website: Optional[str] = None


class MosqueResponseSchema(BaseModel):
    id: int
    image: Optional[str]
    name: str
    type: Optional[str]
    lat: float
    long: float
    phone_no: Optional[str]
    website: Optional[str]

class Config:
        from_attributes = True