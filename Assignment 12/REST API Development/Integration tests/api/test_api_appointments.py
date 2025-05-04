
import pytest
from fastapi.testclient import TestClient
from domain.appointment import appointment


def test_appointment_crud():
    # Create
    response = client.post("/api/appointments", json={
        "id": "a10",
        "user_id": "u1",
        "barber_id": "b1",
        "time": "2025-05-03T10:00:00"
    })
    assert response.status_code == 200

    # Read
    response = client.get("/api/appointments/a10")
    assert response.status_code == 200
    assert response.json()["user_id"] == "u1"

    # Update
    response = client.put("/api/appointments/a10", json={
        "id": "a10",
        "user_id": "u1",
        "barber_id": "b1",
        "time": "2025-05-04T11:00:00"
    })
    assert response.status_code == 200
    assert response.json()["time"] == "2025-05-04T11:00:00"

    # Delete
    response = client.delete("/api/appointments/a10")
    assert response.status_code == 200

    # Confirm Deletion
    response = client.get("/api/appointments/a10")
    assert response.status_code == 404
