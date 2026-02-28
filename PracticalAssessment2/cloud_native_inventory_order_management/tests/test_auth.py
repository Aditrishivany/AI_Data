import src.api.auth as auth_api


async def fake_log_activity(action: str, entity: str, details: str):
    return None


def test_register_and_login(client, monkeypatch):
    monkeypatch.setattr(auth_api, "log_activity", fake_log_activity)

    register_payload = {
        "name": "Auth User",
        "email": "auth_user@example.com",
        "password": "secret123",
    }
    register_response = client.post("/api/auth/register", json=register_payload)
    assert register_response.status_code == 201
    assert register_response.json()["email"] == register_payload["email"]

    login_payload = {
        "email": "auth_user@example.com",
        "password": "secret123",
    }
    login_response = client.post("/api/auth/login", json=login_payload)
    assert login_response.status_code == 200
    assert login_response.json()["message"] == "Login successful"
