
from typing import Optional, List
from domain.user import User
from repositories.user_repository import UserRepository
from fastapi import HTTPException

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user: User) -> User:
        existing = self.user_repository.find_by_id(user.id)
        if existing:
            raise HTTPException(status_code=400, detail=f"User with ID {user.id} already exists.")
        self.user_repository.save(user)
        return user

    def get_user(self, user_id: str) -> Optional[User]:
        user = self.user_repository.find_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def update_user(self, user_id: str, updated_user: User) -> User:
        if not self.user_repository.find_by_id(user_id):
            raise HTTPException(status_code=404, detail="User not found")
        self.user_repository.save(updated_user)
        return updated_user

    def delete_user(self, user_id: str) -> None:
        if not self.user_repository.find_by_id(user_id):
            raise HTTPException(status_code=404, detail="User not found")
        self.user_repository.delete_by_id(user_id)

    def list_users(self) -> List[User]:
        return self.user_repository.find_all()