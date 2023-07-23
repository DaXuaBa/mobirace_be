from sqlalchemy.orm.session import Session
from sqlalchemy import text
from schemas import UserBase, User_Change_Password
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
        user = get_user_by_username(request.username,db)
        email = db.query(User).filter(User.EMAIL == request.email).first()
        if user or email:
            if user:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='username đã tồn tại')
            else:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='email đã tồn tại')
        
        cursor.execute(text("CALL register_user(:username, :password, :fullname, :email, :telNumber, :birthday, :gender, :address, :province, :district, :ward, :org_id, :child_org_id, :size, :link_fb)"),
                         **user.dict())
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
def change_password(user: User_Change_Password, db: Session, current_user: User):
    try:
        authenticate_user(current_user,user.old_password)
        current_user.PASSWORD = Hash.bcrypt(user.new_password)
        
        db.commit()
        response = {
            "status": 200,
            "detail": "Đổi mật khẩu thành công"
        }
        return response
    except :
        db.rollback()
        raise HTTPException(status_code=401, detail="Wrong password")


def authenticate_user(user: User, password: str):
    if not Hash.verify(user.PASSWORD, password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wrong password",
        )
    
def get_user_by_username(username: str, db: Session): 
  try:
    user = db.query(User).filter(User.USER_NAME == username).first()
    if not user:
        return None
    return user
  except:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Execution fail.')
  


    

