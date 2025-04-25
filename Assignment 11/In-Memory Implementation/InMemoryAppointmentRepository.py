from typing import Optional, Dict, List
from repositories.appointment_repository import AppointmentRepository
from domain.appointment import Appointment

class InMemoryAppointmentRepository(AppointmentRepository):
    def __init__(self):
        self._storage: Dict[str, Appointment] = {} # HashMap storage

    def save(self, appointment: Appointment) -> None:
        self._storage[appointment.id] = appointment

    def find_by_id(self, appointment_id: str) -> Optional[Appointment]:
        return self._storage.get(appointment_id)

    def find_all(self) -> List[Appointment]:
        return list(self._storage.values())

    def update(self, appointment: Appointment) -> None:
        if appointment.id in self._storage:
            self._storage[appointment.id] = appointment

    def delete(self, appointment_id: str) -> None:
        if appointment_id in self._storage:
            del self._storage[appointment_id]
