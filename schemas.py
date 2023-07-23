from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional



class UserBase(BaseModel):
    username: str
    password: str
    fullname: str  
    email: str
    telNumber: Optional[str]=None  
    birthday: str
    gender: str
    address: Optional[str]=None
    province: Optional[str]=None
    district: Optional[str]=None
    ward: Optional[str]=None
    org_id: Optional[str]=None
    child_org_id: Optional[str]=None
    size_id: str
    link_fb: Optional[str]=None  

class User_Change_Password(BaseModel):
    old_password: str
    new_password: str

# Tạo một Pydantic model để định nghĩa cấu trúc của request body
class RefreshTokenRequest(BaseModel):
    refresh_Token: str

    

