from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import User
from fastapi import HTTPException, status, Query
from utils.hash import Hash
from db.models import User, UserRole, Function, RoleFunction,Role



def get_func_by_roleID(user_role: UserRole, db: Session): 
    try:
        func = db.query(Function).join(RoleFunction, Function.FUNC_ID == RoleFunction.FUNC_ID).join(Role, RoleFunction.ROLE_ID == Role.ROLE_ID).filter(Role.ROLE_ID == user_role.ROLE_ID).all()
        return func
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Execution fail.')

  


    

