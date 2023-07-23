from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import User
from fastapi import HTTPException, status, Query
from utils.hash import Hash

#create user
def create_user(request: UserBase, db: Session):
    try:
        connection = db.connection().connection
        cursor = connection.cursor()
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Cannot connect to database.')
    try:
        user = db.query(User).filter(User.USER_NAME == request.username).first()
        email = db.query(User).filter(User.EMAIL == request.email).first()
        if user:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
            detail=f'username đã tồn tại')
        elif email:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
            detail=f'email đã tồn tại')
        new_user = User(
            USER_NAME = request.username,
            PASSWORD = Hash.bcrypt(request.password),
            FULL_NAME = request.fullname,
            EMAIL = request.email,        
            EL_NUM = request.tel_number,
            DATE_OF_BIRTH = '2002-07-19',
            GENDER = request.gender,
            SIZE_ID = int(request.size_id),
            LINK_FB = request.link_fb
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        response = {
            "status": 200,
            "detail": "Thao tác thành công!"
        }
        return response
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Execution fail.')
    finally:
        cursor.close()
        connection.close()

def get_user_by_username(username: str, db: Session): 
  try:
    user = db.query(User).filter(User.USER_NAME == username).first()
    if not user:
        return None
    return user
  except:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Execution fail.')
  


    

