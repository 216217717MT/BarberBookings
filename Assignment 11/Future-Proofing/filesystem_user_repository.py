
import json
import os
from typing import Optional
from repositories.user_repository import UserRepository
from src.user import User

class FileSystemUserRepository(UserRepository):
    def __init__(self, file_path: str = "users.json"):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump({}, f)

    def _load_all(self):
        with open(self.file_path, 'r') as f:
            data = json.load(f)
            return {k: User(**v) for k, v in data.items()}

    def _save_all(self, users: dict):
        with open(self.file_path, 'w') as f:
            json.dump({k: v.__dict__ for k, v in users.items()}, f)

    def save(self, user: User) -> None:
        users = self._load_all()
        users[user.user_id] = user
        self._save_all(users)

    def find_by_id(self, user_id: str) -> Optional[User]:
        users = self._load_all()
        return users.get(user_id)

    def delete(self, user_id: str) -> None:
        users = self._load_all()
        if user_id in users:
            del users[user_id]
            self._save_all(users)

    def update(self, user: User) -> None:
        self.save(user)                    # Overwrites the existing user

    def find_all(self) -> list[User]:
        users = self._load_all()
        return list(users.values())
