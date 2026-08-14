from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

class User(BaseModel):
    name: str
    email: str
    age: int
    
users = []

@router.get("/")
def get_users():
    return {
        "users": users
    }

@router.get("/{user_id}")
def get_user(user_id: int):
    if user_id >= len(users):
        raise HTTPException(
            status_code=404,
            detail="User not founde"
        )
    return users[user_id]

@router.post("/")
def create_user(user: User):
    users.append(user.model_dump())

    return {
        "message": "User created successfully",
        "user": user
    }

@router.put("/{user_id}")
def update_user(user_id: int, user: User):
    if user_id >= len(users):
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    user[user_id] = user.model_dump()
    
    return {
        "message": "User updated successfully",
        "user": user
    }
    
@router.delete("/{user_id}")
def delete_user(user_id: int):
    if user_id >= len(users):
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    deleted_user = users.pop(user_id)

    return {
        "message": "User deleted successfully",
        "user": deleted_user
    }