
from .interface Repository import Repository
from domain.barber import Barber

class BarberRepository(Repository[Barber, str]):
    pass