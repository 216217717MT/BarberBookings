
from repositories.inmemory.inmemory_user_repository import InMemoryUserRepository
from repositories.inmemory.inmemory_barber_repository import InMemoryBarberRepository
from repositories.inmemory.inmemory_appointment_repository import InMemoryAppointmentRepository
from repositories.inmemory.inmemory_service_repository import InMemoryServiceRepository

class RepositoryFactory:
    @staticmethod
    def get_user_repository(storage_type="MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryUserRepository()
        # Future: elif storage_type == "DATABASE": return DatabaseUserRepository()
        else:
            raise ValueError("Invalid storage type")

    @staticmethod
    def get_barber_repository(storage_type="MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryBarberRepository()
        else:
            raise ValueError("Invalid storage type")

    @staticmethod
    def get_appointment_repository(storage_type="MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryAppointmentRepository()
        else:
            raise ValueError("Invalid storage type")

    @staticmethod
    def get_service_repository(storage_type="MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryServiceRepository()
        else:
            raise ValueError("Invalid storage type")
