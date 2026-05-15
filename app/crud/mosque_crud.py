from sqlalchemy.orm import Session
from app.models.mosque_model import MosqueModel
from app.schemas.mosque_schema import MosqueCreateSchema


def create_mosque(db: Session,body: MosqueCreateSchema):
    mosque = MosqueModel(**body.dict())
    db.add(mosque)
    db.commit()
    db.refresh(mosque)
    return mosque


def get_all_mosques(db: Session):
    return db.query(MosqueModel).all()