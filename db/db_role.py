from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import User
from fastapi import HTTPException, status, Query
from utils.hash import Hash
from db.models import User, UserRole, Function, RoleFunction,Role



def get_role_by_userID(user: User, db: Session): 
    try:
        user_role = db.query(UserRole).join(User, UserRole.USER_ID == User.USER_ID).filter(User.USER_ID == user.USER_ID).first()
        return user_role
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Execution fail.')

  


    

