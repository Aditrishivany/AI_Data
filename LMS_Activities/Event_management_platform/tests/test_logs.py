def test_logs_endpoints(client):
    event_log = client.post("/logs/events", json={"actor": "system", "action": "event_created", "details": {"id": 1}})
    assert event_log.status_code == 201

    activity_log = client.post(
        "/logs/activities",
        json={"actor": "alice@example.com", "action": "participant_created", "details": {"id": 5}},
    )
    assert activity_log.status_code == 201

    feedback = client.post(
        "/logs/feedback",
        json={"participant_email": "alice@example.com", "event_id": 1, "comment": "Great event"},
    )
    assert feedback.status_code == 201

    get_event_logs = client.get("/logs/events")
    assert get_event_logs.status_code == 200
    assert isinstance(get_event_logs.json(), list)

    update_log = client.put("/logs/events/1", json={"action": "updated"})
    assert update_log.status_code == 200

    delete_log = client.delete("/logs/events/1")
    assert delete_log.status_code == 204
