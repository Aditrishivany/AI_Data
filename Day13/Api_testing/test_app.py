import pytest
import app as app_module
from app import app

# -----------------------
# Fixture Setup
# -----------------------

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        # Reset global state before each test
        app_module.tasks.clear()
        app_module.current_id = 1
        yield client

# -----------------------
# Functional Tests
# -----------------------

def test_create_task(client):
    response = client.post(
        "/api/tasks",
        json={"title": "Learn pytest"}
    )
    assert response.status_code == 201
    assert response.get_json()["title"] == "Learn pytest"


def test_get_all_tasks(client):
    client.post("/api/tasks", json={"title": "Task 1"})
    response = client.get("/api/tasks")

    assert response.status_code == 200
    assert len(response.get_json()) == 1

def test_update_task(client):
    client.post("/api/tasks", json={"title": "Task 1"})

    response = client.put(
        "/api/tasks/1",
        json={"completed": True}
    )

    assert response.status_code == 200
    assert response.get_json()["completed"] is True


def test_delete_task(client):
    client.post("/api/tasks", json={"title": "Task 1"})

    response = client.delete("/api/tasks/1")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Task deleted"}


# -----------------------
# Negative Tests
# -----------------------

def test_create_without_title(client):
    response = client.post(
        "/api/tasks",
        json={"description": "No title"}
    )
    assert response.status_code == 400


def test_get_non_existing_task(client):
    response = client.get("/api/tasks/999")
    assert response.status_code == 404


def test_update_non_existing_task(client):
    response = client.put(
        "/api/tasks/999",
        json={"title": "Updated"}
    )
    assert response.status_code == 404


def test_invalid_data_type(client):
    response = client.post(
        "/api/tasks",
        json={"title": "Test", "completed": "yes"}
    )
    assert response.status_code == 400
