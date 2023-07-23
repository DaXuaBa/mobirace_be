from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from typing import List
from db import db_homepage
from schemas import Homepage

router = APIRouter(
    prefix='/homepage',
    tags=['homepage']
)

# Read homepage
@router.get('/', response_model=List[Homepage])
def get_homepage(db: Session = Depends(get_db)):
  return db_homepage.get_homepage(db)