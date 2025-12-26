import pytest
from unittest.mock import patch, MagicMock
from main import app
from cache_utils.manager import cache_manager


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def clean_cache_before_test():
    cache_manager.clear_all()
    yield


@patch("routes.returns_routes.returns_repo.get_all")
@patch("services.jwt_manager.jwt_manager.decode")
def test_get_all_returns_admin_success(mock_jwt, mock_get_all, client):
    mock_jwt.return_value = {
        "sub": "1", 
        "is_admin": True
    }
    fake_return = MagicMock()
    fake_return.to_dict.return_value = {"id": 1, "reason": "Defective"}
    mock_get_all.return_value = [fake_return]

    response = client.get("/returns/returns", headers={"Authorization": "Bearer token"})
    
    assert response.status_code == 200
    assert len(response.get_json()) == 1


@patch("routes.returns_routes.returns_repo.get_by_id")
@patch("routes.returns_routes.invoice_repo.get_by_id")
@patch("services.jwt_manager.jwt_manager.decode")
def test_get_return_by_id_success(mock_jwt, mock_get_invoice, mock_get_return, client):
    mock_jwt.return_value = {"sub": "5", "is_admin": False}
    
    fake_return = MagicMock()
    fake_return.user_id = 5
    fake_return.to_dict.return_value = {"id": 1, "user_id": 5}
    mock_get_return.return_value = fake_return

    response = client.get("/returns/returns/1", headers={"Authorization": "Bearer token"})
    
    assert response.status_code == 200
    assert response.get_json()["Return"]["user_id"] == 5


@patch("routes.returns_routes.invoice_repo.get_by_id")
@patch("routes.returns_routes.product_repo.get_by_id")
@patch("routes.returns_routes.product_repo.update_quantity")
@patch("routes.returns_routes.returns_repo.create")
@patch("routes.returns_routes.cache_manager")
@patch("services.jwt_manager.jwt_manager.decode")
def test_create_return_success_processed(mock_jwt, mock_cache, mock_create, mock_prod_upd, mock_get_prod, mock_get_inv, client):
    mock_jwt.return_value = {"sub": "5", "is_admin": False}
    
    fake_inv = MagicMock()
    fake_inv.user_id = 5
    mock_get_inv.return_value = fake_inv

    fake_prod = MagicMock()
    fake_prod.id = 100
    fake_prod.quantity = 10
    mock_get_prod.return_value = fake_prod

    fake_ret = MagicMock()
    fake_ret.to_dict.return_value = {"id": 1, "processed": True}
    mock_create.return_value = fake_ret

    payload = {
        "invoice_id": 1,
        "product_id": 100,
        "quantity_returned": 2,
        "return_date": "2025-01-01",
        "reason": "Wrong item",
        "processed": True
    }

    response = client.post("/returns/returns", json=payload, headers={"Authorization": "Bearer token"})

    assert response.status_code == 201
    assert mock_prod_upd.called
    assert response.get_json()["message"] == "Return created successfully"


@patch("routes.returns_routes.returns_repo.get_by_id")
@patch("routes.returns_routes.invoice_repo.get_by_id")
@patch("routes.returns_routes.product_repo.get_by_id")
@patch("routes.returns_routes.product_repo.update_quantity")
@patch("routes.returns_routes.returns_repo.update")
@patch("routes.returns_routes.cache_manager")
@patch("services.jwt_manager.jwt_manager.decode")
def test_update_return_to_processed(mock_jwt, mock_cache, mock_upd_ret, mock_upd_prod, mock_get_prod, mock_get_inv, mock_get_ret, client):
    mock_jwt.return_value = {"sub": "1", "is_admin": True}
    
    fake_ret = MagicMock()
    fake_ret.processed = False
    fake_ret.product_id = 100
    fake_ret.quantity_returned = 5
    fake_ret.invoice_id = 1
    mock_get_ret.return_value = fake_ret

    fake_inv = MagicMock()
    fake_inv.user_id = 5
    mock_get_inv.return_value = fake_inv

    fake_prod = MagicMock()
    fake_prod.id = 100
    fake_prod.quantity = 10
    mock_get_prod.return_value = fake_prod

    fake_updated = MagicMock()
    fake_updated.to_dict.return_value = {"id": 1, "processed": True}
    mock_upd_ret.return_value = fake_updated

    response = client.put("/returns/returns/1", json={"processed": True}, headers={"Authorization": "Bearer token"})

    assert response.status_code == 200
    assert mock_upd_prod.called
    assert response.get_json()["return"]["processed"] is True


def test_create_return_invalid_quantity(client):
    payload = {
        "invoice_id": 1, "product_id": 100, "quantity_returned": 0,
        "return_date": "2025-01-01", "reason": "X", "processed": False
    }

    with patch("services.jwt_manager.jwt_manager.decode") as mock_jwt:
        mock_jwt.return_value = {"sub": "1", "is_admin": True}
        response = client.post("/returns/returns", json=payload, headers={"Authorization": "Bearer token"})
        assert response.status_code == 400
        assert "greater than 0" in response.get_json()["error"]