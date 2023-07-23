from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from typing import List
from db import db_statistic
from schemas import Rankuser

router = APIRouter(
    prefix='/statistic',
    tags=['statistic']
)

# Read rankuser
@router.get('/')
def count_users(db: Session = Depends(get_db)):
  return {'member' : db_statistic.count_users(db),
          'total distance' : db_statistic.total_distance(db),
          'total club' : db_statistic.total_club(db),
          'total race' : db_statistic.total_race(db)}



