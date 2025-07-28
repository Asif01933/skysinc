def test_register_user(client):
    response = client.post("/auth/register", json={
        "username": "asif",
        "email": "asif@example.com",
        "password": "securepass"
    })
    assert response.status_code == 201
    assert response.json()["message"] == "User created successfully"

def test_login_user(client):
    response = client.post("/auth/login", data={
        "username": "asif",
        "password": "securepass"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
