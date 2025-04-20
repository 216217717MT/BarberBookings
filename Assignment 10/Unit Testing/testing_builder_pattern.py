import unittest
import PizzaBuilder       # from builder
import Pizza               # from pizza 

class TestPizzaBuilder(unittest.TestCase):
    def test_pizza_builder(self):
        builder = PizzaBuilder()
        pizza = builder.add_cheese("Cheddar").add_toppings(["Mushrooms", "Bacon"]).add_size("Medium").build()
        
        self.assertEqual(pizza.cheese, "Cheddar")
        self.assertIn("Mushrooms", pizza.toppings)
        self.assertEqual(pizza.size, "Medium")