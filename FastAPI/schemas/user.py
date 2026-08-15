from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    age: int = Field(..., ge=18, le=100)

class UserResponse(BaseModel):
    id: int 
    name: str
    email: EmailStr
    age: int
