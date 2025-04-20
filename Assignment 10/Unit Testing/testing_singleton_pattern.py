import unittest
import DatabaseConnection # from src.singleton 

class TestSingletonPattern(unittest.TestCase):
    def test_singleton(self):
        db1 = DatabaseConnection()
        db2 = DatabaseConnection()

        self.assertIs(db1, db2)                         #  both instances must be  the same
        self.assertEqual(db1.connect(), db2.connect())  # they return the same connection string

