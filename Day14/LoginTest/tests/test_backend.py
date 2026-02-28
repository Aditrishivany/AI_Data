import pytest
from LoginTest.models import User
from LoginTest.app import app, db


@pytest.fixture
def add_user():
    user = User(username="admin", password="1234")
    db.session.add(user)
    db.session.commit()


def test_login_success_backend(client, add_user):
    response = client.post("/login", data={
        "username": "admin",
        "password": "1234"
    })
    assert response.status_code == 200


def test_login_failure_backend(client):
    response = client.post("/login", data={
        "username": "admin",
        "password": "wrong"
    })
    assert response.status_code == 401
