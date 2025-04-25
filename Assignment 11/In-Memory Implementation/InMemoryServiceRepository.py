
from typing import Optional, Dict, List
from repositories.service_repository import ServiceRepository
from domain.service import Service

class InMemoryServiceRepository(ServiceRepository):
    def __init__(self):
        self._storage: Dict[str, Service] = {}

    def save(self, service: Service) -> None:
        self._storage[service.id] = service

    def find_by_id(self, service_id: str) -> Optional[Service]:
        return self._storage.get(service_id)

    def find_all(self) -> List[Service]:
        return list(self._storage.values())

    def update(self, service: Service) -> None:
        if service.id in self._storage:
            self._storage[service.id] = service

    def delete(self, service_id: str) -> None:
        if service_id in self._storage:
            del self._storage[service_id]
