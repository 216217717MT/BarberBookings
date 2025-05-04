import pytest
from fastapi.testclient import TestClient
from domain.barber import Barber


def test_user_crud():
    # Create
    response = client.post("/api/users", json={
        "id": "u10",
        "name": "Jane Doe",
        "email": "jane@example.com"
    })
    assert response.status_code == 200

    # Read
    response = client.get("/api/users/u10")
    assert response.status_code == 200
    assert response.json()["email"] == "jane@example.com"

    # Update
    response = client.put("/api/users/u10", json={
        "id": "u10",
        "name": "Jane Updated",
        "email": "jane_updated@example.com"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Updated"

    # Delete
    response = client.delete("/api/users/u10")
    assert response.status_code == 200

    # Confirm Deletion
    response = client.get("/api/users/u10")
    assert response.status_code == 404