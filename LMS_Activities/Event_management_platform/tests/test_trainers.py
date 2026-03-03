def test_trainer_assignment_and_sessions(client):
    trainer = client.post(
        "/trainers",
        json={"full_name": "Trainer One", "email": "trainer@example.com", "expertise": "Python"},
    )
    assert trainer.status_code == 201
    trainer_id = trainer.json()["id"]

    event = client.post("/events", json={"title": "FastAPI Masterclass", "description": "API", "capacity": 30})
    assert event.status_code == 201
    event_id = event.json()["id"]

    assign = client.post(f"/trainers/{trainer_id}/assign/{event_id}")
    assert assign.status_code == 200
    assert assign.json()["trainer_id"] == trainer_id

    sessions = client.get(f"/trainers/{trainer_id}/sessions")
    assert sessions.status_code == 200
    assert len(sessions.json()) == 1
    assert sessions.json()[0]["id"] == event_id

