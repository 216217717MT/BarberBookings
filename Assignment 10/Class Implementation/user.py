class User:
    def __init__(self, user_id: str, name: str, email: str, phone: str, password: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password  

    def update_profile(self, name: str = None, email: str = None, phone: str = None):
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone

    def change_password(self, new_password: str):
        self.password = new_password                
    def __str__(self):
        return f"User({self.name}, {self.email}, {self.phone})"
