
import pytest
from fastapi.testclient import TestClient
from domain.barber import Barber

def test_barber_crud():
    # Create
    response = client.post("/api/barbers", json={
        "id": "b10",
        "name": "Barber John",
        "specialty": "Fades"
    })
    assert response.status_code == 200

    # Read
    response = client.get("/api/barbers/b10")
    assert response.status_code == 200
    assert response.json()["specialty"] == "Fades"

    # Update
    response = client.put("/api/barbers/b10", json={
        "id": "b10",
        "name": "John Barber",
        "specialty": "Beards"
    })
    assert response.status_code == 200
    assert response.json()["specialty"] == "Beards"

    # Delete
    response = client.delete("/api/barbers/b10")
    assert response.status_code == 200

    # Confirm Deletion
    response = client.get("/api/barbers/b10")
    assert response.status_code == 404
