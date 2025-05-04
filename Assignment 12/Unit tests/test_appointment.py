
import pytest
from fastapi.testclient import TestClient
from main import app
from domain.appointment import Appointment

client = TestClient(app)

@pytest.fixture
def new_appointment():
    return Appointment(id="456", date="2025-05-05", barber_id="123", user_id="789")

def test_create_appointment(new_appointment):
    response = client.post("/appointments", json=new_appointment.dict())
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == new_appointment.id
    assert data["date"] == new_appointment.date

def test_get_appointment(new_appointment):
    client.post("/appointments", json=new_appointment.dict())  # Ensure the appointment exists
    response = client.get(f"/appointments/{new_appointment.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == new_appointment.id
    assert data["date"] == new_appointment.date

def test_update_appointment(new_appointment):
    client.post("/appointments", json=new_appointment.dict())  # Ensure the appointment exists
    updated_appointment = new_appointment.copy(update={"date": "2025-05-06"})
    response = client.put(f"/appointments/{new_appointment.id}", json=updated_appointment.dict())
    assert response.status_code == 200
    data = response.json()
    assert data["date"] == "2025-05-06"

def test_delete_appointment(new_appointment):
    client.post("/appointments", json=new_appointment.dict())  # Ensure the appointment exists
    response = client.delete(f"/appointments/{new_appointment.id}")
    assert response.status_code == 200
    response = client.get(f"/appointments/{new_appointment.id}")
    assert response.status_code == 404
