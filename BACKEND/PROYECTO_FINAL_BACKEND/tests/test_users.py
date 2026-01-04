import pytest
from unittest.mock import patch, MagicMock
from main import app

@pytest.fixture
def client():
    app.config["TESTING"]= True
    with app.test_client() as client:
        yield client


def test_login_invalid_credentials(client):
    response = client.post(
        "/users/login",
        json={
            "username": "fake_user",
            "password": "wrong_password"
        }
    )
    assert response.status_code == 401
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "Invalid credentials"


@patch("repositories.user_repository.UserRepository.get_by_username")
@patch("services.password_manager.PasswordManager.verify_password")
def test_login_success(mock_verify_password, mock_get_user, client):
    fake_user=MagicMock()
    fake_user.id=1
    fake_user.password="hashed_password"
    fake_user.is_admin=True
    mock_get_user.return_value=fake_user
    mock_verify_password.return_value=True
    response = client.post(
        "/users/login",
        json={
            "username": "admin",
            "password": "correct_password"
        }
    )
    assert response.status_code == 200
    data = response.get_json()
    assert "access_token" in data
    assert "refresh_token" in data


def test_refresh_token_missing_header(client):
    response = client.post("/users/refresh-token")
    assert response.status_code == 401
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "Refresh token requerido"


@patch("services.jwt_manager.jwt_manager.decode")
def test_refresh_token_invalid_type(mock_decode, client):
    mock_decode.return_value={
        "type":"access"
    }
    response = client.post(
        "/users/refresh-token",
        headers={
            "Authorization": "Bearer fake_refresh_token"
        }
    )
    assert response.status_code == 403
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "Invalid token"