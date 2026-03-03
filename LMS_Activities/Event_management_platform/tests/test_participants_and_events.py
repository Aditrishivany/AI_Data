def test_participant_crud_and_event_registration(client):
    participant_payload = {"full_name": "Alice Doe", "email": "alice@example.com", "phone": "12345"}
    create_participant = client.post("/participants", json=participant_payload)
    assert create_participant.status_code == 201
    participant_id = create_participant.json()["id"]

    create_event = client.post("/events", json={"title": "Data Bootcamp", "description": "SQL + Mongo", "capacity": 1})
    assert create_event.status_code == 201
    event_id = create_event.json()["id"]

    register = client.post(f"/participants/{participant_id}/register/{event_id}")
    assert register.status_code == 201
    assert register.json()["participant_id"] == participant_id

    # Capacity is 1 so a second participant should fail.
    second_participant = client.post(
        "/participants",
        json={"full_name": "Bob Doe", "email": "bob@example.com", "phone": "99999"},
    )
    assert second_participant.status_code == 201
    second_id = second_participant.json()["id"]
    second_register = client.post(f"/participants/{second_id}/register/{event_id}")
    assert second_register.status_code == 400
    assert second_register.json()["detail"] == "Event capacity reached"

    update_participant = client.put(f"/participants/{participant_id}", json={"full_name": "Alice Updated"})
    assert update_participant.status_code == 200
    assert update_participant.json()["full_name"] == "Alice Updated"

