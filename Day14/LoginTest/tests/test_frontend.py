def test_login_page_renders(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Login Page" in response.data
    assert b'name="username"' in response.data
    assert b'name="password"' in response.data
