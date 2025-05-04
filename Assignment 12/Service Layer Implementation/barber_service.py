
from typing import Optional, List
from domain.barber import Barber
from repositories.barber_repository import BarberRepository
from fastapi import HTTPException

class BarberService:
    def __init__(self, barber_repository: BarberRepository):
        self.barber_repository = barber_repository

    def create_barber(self, barber: Barber) -> Barber:
        existing = self.barber_repository.find_by_id(barber.id)
        if existing:
            raise HTTPException(status_code=400, detail=f"Barber with ID {barber.id} already exists.")
        self.barber_repository.save(barber)
        return barber

    def get_barber(self, barber_id: str) -> Optional[Barber]:
        barber = self.barber_repository.find_by_id(barber_id)
        if not barber:
            raise HTTPException(status_code=404, detail="Barber not found")
        return barber

    def update_barber(self, barber_id: str, updated_barber: Barber) -> Barber:
        if not self.barber_repository.find_by_id(barber_id):
            raise HTTPException(status_code=404, detail="Barber not found")
        self.barber_repository.save(updated_barber)
        return updated_barber

    def delete_barber(self, barber_id: str) -> None:
        if not self.barber_repository.find_by_id(barber_id):
            raise HTTPException(status_code=404, detail="Barber not found")
        self.barber_repository.delete_by_id(barber_id)

    def list_barbers(self) -> List[Barber]:
        return self.barber_repository.find_all()