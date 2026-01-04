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


@patch("routes.invoice_routes.invoice_repo.get_all")
@patch("services.jwt_manager.jwt_manager.decode")
def test_get_all_invoices_admin_success(mock_jwt, mock_get_all, client):
    mock_jwt.return_value = {"sub": "1", "is_admin": True}
    fake_invoice = MagicMock()
    fake_invoice.to_dict.return_value = {"id": 1, "invoice_number": "INV-001"}
    mock_get_all.return_value = [fake_invoice]

    response = client.get("/invoices/invoices", headers={"Authorization": "Bearer token"})
    
    assert response.status_code == 200
    assert len(response.get_json()) == 1


@patch("routes.invoice_routes.invoice_repo.get_by_id")
@patch("services.jwt_manager.jwt_manager.decode")
def test_get_invoice_by_id_success(mock_jwt, mock_get_by_id, client):
    mock_jwt.return_value = {
        "sub": "5", 
        "is_admin": False}
    
    fake_invoice = MagicMock()
    fake_invoice.user_id = 5
    fake_invoice.to_dict.return_value = {"id": 1, "user_id": 5}
    mock_get_by_id.return_value = fake_invoice

    response = client.get("/invoices/invoices/1", headers={"Authorization": "Bearer token"})
    
    assert response.status_code == 200
    assert response.get_json()["Shopping Cart"]["user_id"] == 5



@patch("routes.invoice_routes.shopping_cart_repo.get_by_id")
@patch("routes.invoice_routes.shopping_cart_product_repo.get_by_shopping_cart_id")
@patch("routes.invoice_routes.product_repo.get_by_id")
@patch("routes.invoice_routes.invoice_repo.create")
@patch("routes.invoice_routes.product_repo.update")
@patch("routes.invoice_routes.shopping_cart_repo.update")
@patch("routes.invoice_routes.cache_manager")
@patch("services.jwt_manager.jwt_manager.decode")
def test_create_invoice_success(mock_jwt, mock_cache, mock_cart_upd, mock_prod_upd, mock_inv_create, mock_get_prod, mock_get_cp, mock_get_cart, client):
    
    mock_jwt.return_value = {
        "sub": "1",
        "is_admin": True
    }
    
    fake_cart = MagicMock()
    fake_cart.id = 10
    fake_cart.status = "completed"
    fake_cart.user_id = 5
    mock_get_cart.return_value = fake_cart

    fake_cp = MagicMock()
    fake_cp.product_id = 100
    fake_cp.quantity = 2
    fake_cp.subtotal = 50.0
    mock_get_cp.return_value = [fake_cp]

    fake_prod = MagicMock()
    fake_prod.id = 100
    fake_prod.quantity = 10
    mock_get_prod.return_value = fake_prod

    fake_inv = MagicMock()
    fake_inv.to_dict.return_value = {"id": 1, "total_amount": 50.0}
    mock_inv_create.return_value = fake_inv

    payload = {
        "invoice_number": "INV-123",
        "user_id": 5,
        "shopping_cart_id": 10,
        "created_at": "2025-01-01",
        "billing_address": "Street 123",
        "payment_method": "Credit Card",
        "payment_status": "paid"
    }

    response = client.post("/invoices/invoices", json=payload, headers={"Authorization": "Bearer token"})

    assert response.status_code == 201
    assert response.get_json()["message"] == "Invoice created successfully"
    assert mock_prod_upd.called
    mock_cart_upd.assert_called_with(id=10, status="invoiced")


@patch("routes.invoice_routes.shopping_cart_repo.get_by_id")
@patch("services.jwt_manager.jwt_manager.decode")
def test_create_invoice_cart_not_found(mock_jwt, mock_get_cart, client):
    mock_jwt.return_value = {"sub": "1", "is_admin": True}
    mock_get_cart.return_value = None

    payload = {
        "invoice_number": "INV-123", "user_id": 5, "shopping_cart_id": 999,
        "created_at": "2025-01-01", "billing_address": "X", "payment_method": "Y", "payment_status": "Z"
    }
    
    response = client.post("/invoices/invoices", json=payload, headers={"Authorization": "Bearer token"})
    
    assert response.status_code == 404
    assert response.get_json()["error"] == "Shopping cart not found"


@patch("routes.invoice_routes.shopping_cart_repo.get_by_id")
@patch("routes.invoice_routes.shopping_cart_product_repo.get_by_shopping_cart_id")
@patch("routes.invoice_routes.product_repo.get_by_id")
@patch("services.jwt_manager.jwt_manager.decode")
def test_create_invoice_stock_error(mock_jwt, mock_get_prod, mock_get_cp, mock_get_cart, client):
    mock_jwt.return_value = {"sub": "1", "is_admin": True}
    
    fake_cart = MagicMock()
    fake_cart.status = "completed"
    mock_get_cart.return_value = fake_cart

    fake_cp = MagicMock()
    fake_cp.product_id = 100
    fake_cp.quantity = 50
    mock_get_cp.return_value = [fake_cp]

    fake_prod = MagicMock()
    fake_prod.quantity = 10 
    mock_get_prod.return_value = fake_prod

    payload = {
        "invoice_number": "INV-123", "user_id": 5, "shopping_cart_id": 10,
        "created_at": "2025-01-01", "billing_address": "X", "payment_method": "Y", "payment_status": "Z"
    }

    response = client.post("/invoices/invoices", json=payload, headers={"Authorization": "Bearer token"})
    
    assert response.status_code == 400
    assert "Not enough stock" in response.get_json()["error"]