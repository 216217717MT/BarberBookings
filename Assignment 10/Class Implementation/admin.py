
import User   # from user 
import Barber # from barber

class Admin(User):                          # Inherits from User
    def __init__(self, user_id: str, name: str, email: str, password: str):
        super().__init__(user_id, name, email, password)
        self._managed_users = []
        self._managed_barbers = []

    def add_user(self, user: User):
        self._managed_users.append(user)

    def remove_user(self, user_id: str):
        self._managed_users = [u for u in self._managed_users if u.user_id != user_id]

    def add_barber(self, barber: Barber):
        self._managed_barbers.append(barber)

    def remove_barber(self, barber_id: str):
        self._managed_barbers = [b for b in self._managed_barbers if b.user_id != barber_id]

    def list_all_users(self):
        return [user.get_profile() for user in self._managed_users]

    def list_all_barbers(self):
        return [barber.get_profile() for barber in self._managed_barbers]
