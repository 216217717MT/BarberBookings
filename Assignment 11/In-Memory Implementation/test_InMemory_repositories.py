
import unittest
from repositories.inmemory.inmemory_user_repository import InMemoryUserRepository
from repositories.inmemory.inmemory_barber_repository import InMemoryBarberRepository
from repositories.inmemory.inmemory_service_repository import InMemoryServiceRepository
from repositories.inmemory.inmemory_appointment_repository import InMemoryAppointmentRepository
from entities.user import User
from entities.barber import Barber
from entities.service import Service
from entities.appointment import Appointment

class TestInMemoryRepositories(unittest.TestCase):

    def test_user_repository_crud(self):
        repo = InMemoryUserRepository()
        user = User(user_id="u1", name="Tshepang Molefe", email="tmolefe111@gmail.com")
        repo.save(user)
        self.assertEqual(repo.find_by_id("u1"), user)
        
        user.name = "Tshepang Molefe"
        repo.update("u1", user)
        self.assertEqual(repo.find_by_id("u1").name, "Tshepang Molefe")

        repo.delete("u1")
        self.assertIsNone(repo.find_by_id("u1"))

    def test_barber_repository_crud(self):
        repo = InMemoryBarberRepository()
        barber = Barber(barber_id="b1", name="Zakaria", specialization="Fade")
        repo.save(barber)
        self.assertEqual(repo.find_by_id("b1"), barber)

        barber.name = "Zakaria"
        repo.update("b1", barber)
        self.assertEqual(repo.find_by_id("b1").name, "Zakaria")

        repo.delete("b1")
        self.assertIsNone(repo.find_by_id("b1"))

    def test_service_repository_crud(self):
        repo = InMemoryServiceRepository()
        service = Service(service_id="s1", name="Haircut", duration=30, price=15.0)
        repo.save(service)
        self.assertEqual(repo.find_by_id("s1"), service)

        service.price = 18.0
        repo.update("s1", service)
        self.assertEqual(repo.find_by_id("s1").price, 18.0)

        repo.delete("s1")
        self.assertIsNone(repo.find_by_id("s1"))

    def test_appointment_repository_crud(self):
        repo = InMemoryAppointmentRepository()
        appointment = Appointment(appointment_id="a1", user_id="u1", barber_id="b1", service_id="s1", scheduled_time="2025-05-01 10:00")
        repo.save(appointment)
        self.assertEqual(repo.find_by_id("a1"), appointment)

        appointment.scheduled_time = "2025-05-01 11:00"
        repo.update("a1", appointment)
        self.assertEqual(repo.find_by_id("a1").scheduled_time, "2025-05-01 11:00")

        repo.delete("a1")
        self.assertIsNone(repo.find_by_id("a1"))

if __name__ == '__main__':
    unittest.main()
