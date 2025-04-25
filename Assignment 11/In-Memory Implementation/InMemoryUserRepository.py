
from typing import Optional, Dict, List
from repositories.user_repository import UserRepository
from domain.user import User

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._storage: Dict[str, User] = {}

    def save(self, user: User) -> None:
        self._storage[user.id] = user

    def find_by_id(self, user_id: str) -> Optional[User]:
        return self._storage.get(user_id)

    def find_all(self) -> List[User]:
        return list(self._storage.values())

    def update(self, user: User) -> None:
        if user.id in self._storage:
            self._storage[user.id] = user

    def delete(self, user_id: str) -> None:
        if user_id in self._storage:
            del self._storage[user_id]
