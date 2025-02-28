from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    email: EmailStr
    password: str | None = None

class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True 