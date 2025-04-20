class Pizza:
    def __init__(self):
        self.cheese = None
        self.toppings = []
        self.size = None

    def __repr__(self):
        return f"Pizza(Size: {self.size}, Cheese: {self.cheese}, Toppings: {', '.join(self.toppings)})"
