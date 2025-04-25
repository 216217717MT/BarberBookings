
from .interface Repository import Repository
from domain.service import Service

class ServiceRepository(Repository[Service, str]):
    pass
