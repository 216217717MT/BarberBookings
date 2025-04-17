# Creational Pattern Implementation AND Unit Testing (for each creational pattern)

**all six creational patterns with clear use cases**

**1. Simple Factory Pattern**

from src.user import User
from src.barber import Barber
from src.admin import Admin

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

**Testing Simple Factory Pattern**:

import unittest
from creational_patterns.simple_factory import VehicleFactory

class TestSimpleFactoryPattern(unittest.TestCase):
    def test_vehicle_factory(self):
        car = VehicleFactory.create_vehicle('Car')
        self.assertEqual(car.drive(), "Driving a car")

        bike = VehicleFactory.create_vehicle('Bike')
        self.assertEqual(bike.ride(), "Riding a bike")

        truck = VehicleFactory.create_vehicle('Truck')
        self.assertEqual(truck.load(), "Loading a truck")



**2. Factory Method Pattern**

from src.payment_processor import PaymentProcessor
from src.credit_card_processor import CreditCardProcessor
from src.paypal_processor import PayPalProcessor

class PaymentProcessorFactory:
    @staticmethod
    def get_payment_processor(payment_method: str) -> PaymentProcessor:
        if payment_method.lower() == "creditcard":
            return CreditCardProcessor()
        elif payment_method.lower() == "paypal":
            return PayPalProcessor()
        else:
            raise ValueError(f"Unknown payment method: {payment_method}")

**Testing Factory Method**

import unittest
from src.payment_processor_factory import PaymentProcessorFactory
from src.credit_card_processor import CreditCardProcessor
from src.paypal_processor import PayPalProcessor

class TestPaymentProcessorFactory(unittest.TestCase):
    def test_get_creditcard_processor(self):
        processor = PaymentProcessorFactory.get_payment_processor("creditcard")
        self.assertIsInstance(processor, CreditCardProcessor)

    def test_get_paypal_processor(self):
        processor = PaymentProcessorFactory.get_payment_processor("paypal")
        self.assertIsInstance(processor, PayPalProcessor)

    def test_invalid_payment_method(self):
        with self.assertRaises(ValueError):
            PaymentProcessorFactory.get_payment_processor("bitcoin")


**3. Abstract Factory Pattern**

 
from src.windows_button import WindowsButton
from src.macos_button import MacOSButton
from src.button import Button

class GUIFactory:
    @staticmethod
    def create_button(os_type: str) -> Button:
        if os_type.lower() == "windows":
            return WindowsButton()
        elif os_type.lower() == "macos":
            return MacOSButton()
        else:
            raise ValueError(f"Unknown OS type: {os_type}")


**Testing Abstract Factory**:

import unittest
from src.abstract_factory import GUIFactory
from src.windows_button import WindowsButton
from src.macos_button import MacOSButton

class TestGUIFactory(unittest.TestCase):
    def test_create_windows_button(self):
        button = GUIFactory.create_button("windows")
        self.assertIsInstance(button, WindowsButton)

    def test_create_macos_button(self):
        button = GUIFactory.create_button("macos")
        self.assertIsInstance(button, MacOSButton)

    def test_invalid_os_type(self):
        with self.assertRaises(ValueError):
            GUIFactory.create_button("linux")

**4. Builder Pattern**

from src.pizza import Pizza

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

**src/pizza.py**

class Pizza:
    def __init__(self):
        self.cheese = None
        self.toppings = []
        self.size = None

    def __repr__(self):
        return f"Pizza(Size: {self.size}, Cheese: {self.cheese}, Toppings: {', '.join(self.toppings)})"

**Testing Builder Pattern**

import unittest
from src.builder import PizzaBuilder
from src.pizza import Pizza

class TestPizzaBuilder(unittest.TestCase):
    def test_pizza_builder(self):
        builder = PizzaBuilder()
        pizza = builder.add_cheese("Cheddar").add_toppings(["Mushrooms", "Bacon"]).add_size("Medium").build()
        
        self.assertEqual(pizza.cheese, "Cheddar")
        self.assertIn("Mushrooms", pizza.toppings)
        self.assertEqual(pizza.size, "Medium")


**5. Prototype Pattern**

import copy

class Shape:
    def clone(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def clone(self):
        return copy.deepcopy(self)

    def __repr__(self):
        return f"Circle(Radius: {self.radius})"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def clone(self):
        return copy.deepcopy(self)

    def __repr__(self):
        return f"Rectangle(Width: {self.width}, Height: {self.height})"


**Testing Prototype Pattern**

import unittest
from src.prototype import Circle

class TestPrototypePattern(unittest.TestCase):
    def test_shape_prototype(self):
        circle1 = Circle(5)
        circle2 = circle1.clone()
        
        self.assertEqual(circle1.radius, circle2.radius)
        self.assertIsNot(circle1, circle2)  # Ensure they are different instances

**6. Singleton Pattern**

class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

    def connect(self):
        return "Connecting to the database..."

    def disconnect(self):
        return "Disconnecting from the database..."

**Testing Singleton Pattern**

import unittest
from src.singleton import DatabaseConnection

class TestSingletonPattern(unittest.TestCase):
    def test_singleton(self):
        db1 = DatabaseConnection()
        db2 = DatabaseConnection()

        self.assertIs(db1, db2)  # Ensure both instances are the same
        self.assertEqual(db1.connect(), db2.connect())  # Ensure they return the same connection string

