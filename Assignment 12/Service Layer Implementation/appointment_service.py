
from typing import Optional, List
from domain.appointment import Appointment
from repositories.appointment_repository import AppointmentRepository
from fastapi import HTTPException

class AppointmentService:
    def __init__(self, appointment_repository: AppointmentRepository):
        self.appointment_repository = appointment_repository

    def create_appointment(self, appointment: Appointment) -> Appointment:
        existing = self.appointment_repository.find_by_id(appointment.id)
        if existing:
            raise HTTPException(status_code=400, detail=f"Appointment with ID {appointment.id} already exists.")
        self.appointment_repository.save(appointment)
        return appointment

    def get_appointment(self, appointment_id: str) -> Optional[Appointment]:
        appointment = self.appointment_repository.find_by_id(appointment_id)
        if not appointment:
            raise HTTPException(status_code=404, detail="Appointment not found")
        return appointment

    def update_appointment(self, appointment_id: str, updated_appointment: Appointment) -> Appointment:
        if not self.appointment_repository.find_by_id(appointment_id):
            raise HTTPException(status_code=404, detail="Appointment not found")
        self.appointment_repository.save(updated_appointment)
        return updated_appointment

    def delete_appointment(self, appointment_id: str) -> None:
        if not self.appointment_repository.find_by_id(appointment_id):
            raise HTTPException(status_code=404, detail="Appointment not found")
        self.appointment_repository.delete_by_id(appointment_id)

    def list_appointments(self) -> List[Appointment]:
        return self.appointment_repository.find_all()