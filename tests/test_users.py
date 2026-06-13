from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():

    response = client.post(
        "/users",
        json={
            "name": "Victor",
            "email": "victor@email.com"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Victor"
    assert data["email"] == "victor@email.com"
    
def test_get_invalid_user():

    response = client.get(
        "/users/123"
    )

    assert response.status_code == 404
    
def test_get_user():
    
    create = client.post(
        "/users",
        json={
            "name": "Maria",
            "email": "maria@email.com"
        }
    )

    user = create.json()

    response = client.get(
        f"/users/{user['id']}"
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Maria"
    
def test_update_user():

    create = client.post(
        "/users",
        json={
            "name": "Pedro",
            "email": "pedro@email.com"
        }
    )

    user = create.json()

    response = client.put(
        f"/users/{user['id']}",
        json={
            "name": "Pedro Atualizado",
            "email": "novo@email.com"
        }
    )

    print("\nSTATUS:", response.status_code)
    print("BODY:", response.json())

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Pedro Atualizado"
    assert data["email"] == "novo@email.com"
    
def test_delete_user():

    create = client.post(
        "/users",
        json={
            "name": "João",
            "email": "joao@email.com"
        }
    )

    user = create.json()

    response = client.delete(
        f"/users/{user['id']}"
    )

    assert response.status_code == 200

    assert response.json() == {
        "message": "User deleted"
    }