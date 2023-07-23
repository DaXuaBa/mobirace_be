from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional



class UserBase(BaseModel):
    username: str
    password: str
    fullname: str  # Sử dụng snake_case thay vì camelCase
    email: str
    tel_number: str  # Sử dụng snake_case thay vì camelCase
    birthday: str
    gender: str
    address: str
    province: str
    district: str
    ward: str
    org_id: str
    child_org_id: str  # Sử dụng snake_case thay vì camelCase
    size_id: str
    link_fb: str  # Sử dụng snake_case thay vì camelCase

# Tạo một Pydantic model để định nghĩa cấu trúc của request body
class RefreshTokenRequest(BaseModel):
    refresh_Token: str
    

