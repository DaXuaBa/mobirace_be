from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from typing import List
from db import db_community
from schemas import Community

router = APIRouter(
    prefix='/community',
    tags=['community']
)

# Read community
@router.get('/', response_model=List[Community])
def get_community(db: Session = Depends(get_db)):
  return db_community.get_community(db)