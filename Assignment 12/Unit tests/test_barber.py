
import pytest
from fastapi.testclient import TestClient
from main import app
from domain.barber import Barber

client = TestClient(app)

@pytest.fixture
def new_barber():
    return Barber(id="123", name="Tshepang Molefe", age=30, specialization="Haircut")

def test_create_barber(new_barber):
    response = client.post("/barbers", json=new_barber.dict())
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == new_barber.id
    assert data["name"] == new_barber.name

def test_get_barber(new_barber):
    client.post("/barbers", json=new_barber.dict())  # Ensure the barber exists
    response = client.get(f"/barbers/{new_barber.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == new_barber.id
    assert data["name"] == new_barber.name

def test_update_barber(new_barber):
    client.post("/barbers", json=new_barber.dict())  # Ensure the barber exists
    updated_barber = new_barber.copy(update={"name": "Amo Ntwa"})
    response = client.put(f"/barbers/{new_barber.id}", json=updated_barber.dict())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Amo Ntwa"

def test_delete_barber(new_barber):
    client.post("/barbers", json=new_barber.dict())  # Ensure the barber exists
    response = client.delete(f"/barbers/{new_barber.id}")
    assert response.status_code == 200
    response = client.get(f"/barbers/{new_barber.id}")
    assert response.status_code == 404
