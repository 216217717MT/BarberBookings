
from typing import Optional, Dict, List
from repositories.barber_repository import BarberRepository
from domain.barber import Barber

class InMemoryBarberRepository(BarberRepository):
    def __init__(self):
        self._storage: Dict[str, Barber] = {}

    def save(self, barber: Barber) -> None:
        self._storage[barber.id] = barber

    def find_by_id(self, barber_id: str) -> Optional[Barber]:
        return self._storage.get(barber_id)

    def find_all(self) -> List[Barber]:
        return list(self._storage.values())

    def update(self, barber: Barber) -> None:
        if barber.id in self._storage:
            self._storage[barber.id] = barber

    def delete(self, barber_id: str) -> None:
        if barber_id in self._storage:
            del self._storage[barber_id]
