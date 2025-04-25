

from .interface Repository import Repository
from typing import Optional
from domain.user import User  

class UserRepository(Repository[User, str]):
    pass