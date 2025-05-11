class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def greet(self):
        return f"Hello, {self.name}! Your email is {self.email}."

# Creating an instance of the User class
user1 = User("Soso", "soso@example.com")

# Calling a method from the class
print(user1.greet())
