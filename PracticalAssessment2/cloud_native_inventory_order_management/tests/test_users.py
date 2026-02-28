import src.api.users as users_api


async def fake_log_activity(action: str, entity: str, details: str):
    return None


def test_create_and_list_users(client, monkeypatch):
    monkeypatch.setattr(users_api, "log_activity", fake_log_activity)

    payload = {
        "name": "Test User",
        "email": "test_user@example.com",
        "is_active": True,
    }
    create_response = client.post("/api/users/", json=payload)
    assert create_response.status_code == 201
    assert create_response.json()["email"] == payload["email"]

    list_response = client.get("/api/users/")
    assert list_response.status_code == 200
    assert len(list_response.json()) >= 1
