from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from typing import List
from db import db_rankclub
from schemas import Rankclub

router = APIRouter(
    prefix='/rankclub',
    tags=['rankclub']
)

# Read rankclub
@router.get('/', response_model=List[Rankclub])
def get_rankclub(db: Session = Depends(get_db)):
  return db_rankclub.get_rankclub(db)