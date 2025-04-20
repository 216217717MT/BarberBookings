import User
import Barber
import Admin

class UserFactory:
    @staticmethod
    def create_user(user_type: str, user_id: str, name: str, email: str, password: str):
        if user_type.lower() == "client":
            return User(user_id, name, email, password)
        elif user_type.lower() == "barber":
            return Barber(user_id, name, email, password, [])
        elif user_type.lower() == "admin":
            return Admin(user_id, name, email, password)
        else:
            raise ValueError(f"Unknown user type: {user_type}")
