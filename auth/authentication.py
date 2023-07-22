from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import models
from auth.hash import Hash
from auth import oauth2
from jose import jwt
from jose.exceptions import JWTError

router = APIRouter(
  tags=['authentication']
)

@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
  user = db.query(models.DbUser).filter(models.DbUser.username == request.username).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
  if not Hash.verify(user.password, request.password):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")

  access_token = oauth2.create_access_token(data={'sub': user.username})
  refresh_token = oauth2.create_refresh_token(data={'sub': user.username})

  return {
    'access_token': access_token,
    'refresh_token': refresh_token,
    'user_id': user.id,
    'username': user.username
  }

@router.post('/new_token')
def get_new_token(token: str , db: Session = Depends(get_db)):
  try: 
    payload = jwt.decode(token, oauth2.SECRET_KEY_REFRESH, algorithms=[oauth2.ALGORITHM])
    username: str = payload.get("sub")
    user = db.query(models.DbUser).filter(models.DbUser.username == username).first()
    if not user:
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid refresh token")

    access_token = oauth2.create_access_token(data={'sub': user.username})
    refresh_token = oauth2.create_refresh_token(data={'sub': user.username})

    return {
      'access_token': access_token,
      'refresh_token': refresh_token,
      'user_id': user.id,
      'username': user.username
    }
  except JWTError:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail=f'Refresh token has expired or invalid')
  
  


 