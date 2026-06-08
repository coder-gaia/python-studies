from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_task_invalid_user():

    response = client.post(
        "/users/123/tasks",
        json={
            "title": "Task inválida"
        }
    )

    assert response.status_code == 404
    
def test_create_task_invalid_user():

    response = client.post(
        "/users/123/tasks",
        json={
            "title": "Task inválida"
        }
    )

    assert response.status_code == 404
    
def test_get_user_tasks():

    create_user = client.post(
        "/users",
        json={
            "name": "Maria",
            "email": "maria@email.com"
        }
    )

    user = create_user.json()

    client.post(
        f"/users/{user['id']}/tasks",
        json={
            "title": "Task 1"
        }
    )

    response = client.get(
        f"/users/{user['id']}/tasks"
    )

    assert response.status_code == 200

    tasks = response.json()

    assert len(tasks) >= 1

def test_update_task():

    create_user = client.post(
        "/users",
        json={
            "name": "Carlos",
            "email": "carlos@email.com"
        }
    )

    user = create_user.json()

    create_task = client.post(
        f"/users/{user['id']}/tasks",
        json={
            "title": "Task antiga"
        }
    )

    task = create_task.json()

    response = client.put(
        f"/tasks/{task['id']}",
        json={
            "title": "Task atualizada"
        }
    )

    assert response.status_code == 200

    assert response.json()["title"] == "Task atualizada"
    
def test_complete_task():

    create_user = client.post(
        "/users",
        json={
            "name": "Julia",
            "email": "julia@email.com"
        }
    )

    user = create_user.json()

    create_task = client.post(
        f"/users/{user['id']}/tasks",
        json={
            "title": "Finalizar projeto"
        }
    )

    task = create_task.json()

    response = client.patch(
        f"/tasks/{task['id']}/complete"
    )

    assert response.status_code == 200

    assert response.json()["completed"] is True
    
def test_delete_task():

    create_user = client.post(
        "/users",
        json={
            "name": "Lucas",
            "email": "lucas@email.com"
        }
    )

    user = create_user.json()

    create_task = client.post(
        f"/users/{user['id']}/tasks",
        json={
            "title": "Excluir task"
        }
    )

    task = create_task.json()

    response = client.delete(
        f"/tasks/{task['id']}"
    )

    assert response.status_code == 200

    assert response.json() == {
        "message": "Task deleted"
    }