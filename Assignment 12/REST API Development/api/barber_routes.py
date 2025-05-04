
from fastapi import APIRouter
from typing import List
from domain.barber import Barber
from services.barber_service import BarberService
from repositories.inmemory.inmemory_barber_repository import InMemoryBarberRepository

barber_router = APIRouter(prefix="/api/barbers", tags=["Barbers"])
barber_service = BarberService(barber_repository=InMemoryBarberRepository())

@barber_router.post("/", response_model=Barber)
def create_barber(barber: Barber):
    return barber_service.create_barber(barber)

@barber_router.get("/{barber_id}", response_model=Barber)
def get_barber(barber_id: str):
    return barber_service.get_barber(barber_id)

@barber_router.put("/{barber_id}", response_model=Barber)
def update_barber(barber_id: str, barber: Barber):
    return barber_service.update_barber(barber_id, barber)

@barber_router.delete("/{barber_id}")
def delete_barber(barber_id: str):
    barber_service.delete_barber(barber_id)
    return {"message": f"Barber {barber_id} deleted"}

@barber_router.get("/", response_model=List[Barber])
def list_barbers():
    return barber_service.list_barbers()
