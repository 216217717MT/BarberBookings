
from fastapi import APIRouter
from typing import List
from domain.appointment import Appointment
from services.appointment_service import AppointmentService
from repositories.inmemory.inmemory_appointment_repository import InMemoryAppointmentRepository

appointment_router = APIRouter(prefix="/api/appointments", tags=["Appointments"])
appointment_service = AppointmentService(appointment_repository=InMemoryAppointmentRepository())

@appointment_router.post("/", response_model=Appointment)
def create_appointment(appointment: Appointment):
    return appointment_service.create_appointment(appointment)

@appointment_router.get("/{appointment_id}", response_model=Appointment)
def get_appointment(appointment_id: str):
    return appointment_service.get_appointment(appointment_id)

@appointment_router.put("/{appointment_id}", response_model=Appointment)
def update_appointment(appointment_id: str, appointment: Appointment):
    return appointment_service.update_appointment(appointment_id, appointment)

@appointment_router.delete("/{appointment_id}")
def delete_appointment(appointment_id: str):
    appointment_service.delete_appointment(appointment_id)
    return {"message": f"Appointment {appointment_id} deleted"}

@appointment_router.get("/", response_model=List[Appointment])
def list_appointments():
    return appointment_service.list_appointments()