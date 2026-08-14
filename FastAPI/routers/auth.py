from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

class LoginRequest(BaseModel):
    email: str
    password: str
    
class LoginResponse(BaseModel):
    message: str
    email: str
    token: str

@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest):
    if data.email == "admin@gmail.com" and data.passsword == "1234":
        return {
            "message": "Login successful",
            "email": data.email,
            "token": "fake-token-123"
        }
    raise HTTPException(
        status_code=401,
        detail="Invalid email or password"
    )