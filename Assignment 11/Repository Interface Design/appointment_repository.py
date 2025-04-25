
from .interface Repository import Repository
from domain.appointment import Appointment

class AppointmentRepository(Repository[Appointment, str]):
    pass