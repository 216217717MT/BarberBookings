

import pytest
from fastapi.testclient import TestClient
from main import app
from domain.user import User

client = TestClient(app)

@pytest.fixture
def new_user():
    return User(id="2564", name="tshepang", email="tmolefe11@agmail.com")

def test_create_user(new_user):
    response = client.post("/users", json=new_user.dict())
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == new_user.id
    assert data["name"] == new_user.name

def test_get_user(new_user):
    client.post("/users", json=new_user.dict())  # Ensure the user exists
    response = client.get(f"/users/{new_user.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == new_user.id
    assert data["name"] == new_user.name

def test_update_user(new_user):
    client.post("/users", json=new_user.dict())  # Ensure the user exists
    updated_user = new_user.copy(update={"name": "Bob"})
    response = client.put(f"/users/{new_user.id}", json=updated_user.dict())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Bob"

def test_delete_user(new_user):
    client.post("/users", json=new_user.dict())  # Ensure the user exists
    response = client.delete(f"/users/{new_user.id}")
    assert response.status_code == 200
    response = client.get(f"/users/{new_user.id}")
    assert response.status_code == 404
