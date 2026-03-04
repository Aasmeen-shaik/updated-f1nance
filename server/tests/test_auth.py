from fastapi import status

def test_register_user(client):
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "password": "testpassword123",
            "full_name": "Test User",
            "username": "testuser"
        }
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_login_user(client):
    # First register
    client.post(
        "/api/v1/auth/register",
        json={
            "email": "login@example.com",
            "password": "loginpassword123",
            "full_name": "Login User",
            "username": "loginuser"
        }
    )
    
    # Then login
    # OAuth2PasswordRequestForm uses 'username' field for email/username
    response = client.post(
        "/api/v1/auth/login",
        data={
            "username": "login@example.com",
            "password": "loginpassword123"
        }
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
