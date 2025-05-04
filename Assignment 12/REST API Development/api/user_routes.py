
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from domain.user import User
from services.user_service import UserService
from repositories.inmemory.inmemory_user_repository import InMemoryUserRepository

user_router = APIRouter(prefix="/api/users", tags=["Users"])
user_service = UserService(user_repository=InMemoryUserRepository())

@user_router.post("/", response_model=User)
def create_user(user: User):
    return user_service.create_user(user)

@user_router.get("/{user_id}", response_model=User)
def get_user(user_id: str):
    return user_service.get_user(user_id)

@user_router.put("/{user_id}", response_model=User)
def update_user(user_id: str, user: User):
    return user_service.update_user(user_id, user)

@user_router.delete("/{user_id}")
def delete_user(user_id: str):
    user_service.delete_user(user_id)
    return {"message": f"User {user_id} deleted"}

@user_router.get("/", response_model=List[User])
def list_users():
    return user_service.list_users()