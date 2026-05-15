from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.mosque_schema import MosqueCreateSchema, MosqueResponseSchema
from app.crud import mosque_crud

mosque_router = APIRouter(prefix="/mosques", tags=["Mosques"])

@mosque_router.post("/create",response_model=MosqueResponseSchema,status_code=status.HTTP_201_CREATED)
def add_mosque(body:MosqueCreateSchema,db:Session = Depends(get_db)):
    return mosque_crud.create_mosque(db, body)


@mosque_router.get("/all", response_model=list[MosqueResponseSchema])
def all_mosques(db: Session = Depends(get_db)):
    return mosque_crud.get_all_mosques(db)