from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

class MosqueModel(Base):
    __tablename__ = "mosques"

    id = Column(Integer, primary_key=True, index=True)

    image = Column(String, nullable=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=True)

    lat = Column(Float, nullable=False)
    long = Column(Float, nullable=False)

    phone_no = Column(String, nullable=True)
    website = Column(String, nullable=True)