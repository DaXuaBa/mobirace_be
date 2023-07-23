from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from typing import List
from db import db_rankuser
from schemas import Rankuser

router = APIRouter(
    prefix='/rankuser',
    tags=['rankuser']
)

# Read rankuser
@router.get('/', response_model=List[Rankuser])
def get_rankuser(db: Session = Depends(get_db)):
  return db_rankuser.get_rankuser(db)