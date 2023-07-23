from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from typing import List
from db import db_slogan
from schemas import Slogan

router = APIRouter(
    prefix='/slogan',
    tags=['slogan']
)

# Read all slogan
@router.get('/', response_model=List[Slogan])
def get_slogan(db: Session = Depends(get_db)):
  return db_slogan.get_slogan(db)