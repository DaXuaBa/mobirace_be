from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional



class UserBase(BaseModel):
    username: str
    password: str
    fullname: str
    email: str
    telNumber: str
    birthday:str
    gender:str
    address: str
    province:str
    district:str
    ward:str
    org_id:str
    child_org_id:str
    size:str
    link_fb:str
    

