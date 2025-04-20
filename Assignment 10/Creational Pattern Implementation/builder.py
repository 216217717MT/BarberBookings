import Pizza # from pizza 

class PizzaBuilder:
    def __init__(self):
        self._pizza = Pizza()

    def add_cheese(self, cheese_type: str):
        self._pizza.cheese = cheese_type
        return self

    def add_toppings(self, toppings: list):
        self._pizza.toppings.extend(toppings)
        return self

    def add_size(self, size: str):
        self._pizza.size = size
        return self

    def build(self) -> Pizza:
        return self._pizza
