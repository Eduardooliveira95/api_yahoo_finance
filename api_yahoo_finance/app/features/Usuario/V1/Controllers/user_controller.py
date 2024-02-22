from fastapi import APIRouter, HTTPException
from typing import List
from app.features.Usuario.V1.Services.UserService import UserService
from app.features.Usuario.V1.Models.DTO.User import UserCreate, UserUpdate

router = APIRouter()
user_service = UserService()

@router.get("/users/", response_model=List[UserUpdate])
async def read_users(skip: int = 0, limit: int = 10):
    return user_service.get_users(skip=skip, limit=limit)

@router.get("/users/{user_id}", response_model=UserUpdate)
async def read_user(user_id: int):
    user = user_service.get_user(user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
