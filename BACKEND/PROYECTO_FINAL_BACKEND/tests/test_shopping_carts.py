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


@patch("services.jwt_manager.jwt_manager.decode")
@patch("routes.product_routes.cache_manager")
@patch("routes.shopping_cart_routes.shopping_cart_repo.get_all")
def test_get_all_shopping_carts_empty(mock_get_all,mock_cache, mock_jwt_decode, client):
    mock_jwt_decode.return_value = {
        "sub": "1",
        "is_admin": True
    }
    mock_cache.check_key.return_value=False
    mock_get_all.return_value = []
    response = client.get("/shopping_carts/shopping_carts", headers={
            "Authorization": "Bearer fake_token"
        })
    assert response.status_code == 404
    data = response.get_json()
    assert "data" in data
    assert data["message"] == "No carts found"
    assert data["data"] == []
    


@patch("services.jwt_manager.jwt_manager.decode")
@patch("routes.shopping_cart_routes.shopping_cart_repo.get_all")
def test_get_all_shopping_carts_success(mock_get_all, mock_jwt_decode, client):
    mock_jwt_decode.return_value = {
        "sub": "1",
        "is_admin": True
    }
    fake_shopping_cart = MagicMock()
    fake_shopping_cart.to_dict.return_value = {
        "id": 1,
        "user_id": 5,
        "status": "cancelled",
        "created_at": "2025-12-01 00:00:00"
    }
    mock_get_all.return_value = [fake_shopping_cart]
    response = client.get("/shopping_carts/shopping_carts", headers={
            "Authorization": "Bearer fake_token"
        })
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["user_id"] == 5


@patch("services.jwt_manager.jwt_manager.decode")
@patch("routes.shopping_cart_routes.shopping_cart_repo.get_by_id")
def test_get_shopping_cart_by_id_empty(mock_get_by_id, mock_jwt_decode, client):
    mock_jwt_decode.return_value = {
        "sub": "1",
        "is_admin": True
    }
    mock_get_by_id.return_value = None
    response = client.get(
        "/shopping_carts/shopping_carts/1",
        headers={
            "Authorization": "Bearer fake_token"
        }
    )
    assert response.status_code == 404
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "Cart not found"


@patch("services.jwt_manager.jwt_manager.decode")
@patch("routes.shopping_cart_routes.shopping_cart_repo.create")
def test_create_shopping_cart_missing_fields(mock_create, mock_jwt_decode, client):
    mock_jwt_decode.return_value = {
        "sub": "1",
        "is_admin": True
    }


    response = client.post(
        "/shopping_carts/shopping_carts",
        json={
            "user_id":5,
            "status":"empty"
        },
        headers={
            "Authorization": "Bearer fake_token"
        }
    )
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
    mock_create.assert_not_called()

@patch("routes.shopping_cart_routes.user_repo.get_by_id")
@patch("services.jwt_manager.jwt_manager.decode")
@patch("routes.shopping_cart_routes.shopping_cart_repo.create")
def test_create_shopping_cart_success(mock_create, mock_jwt_decode,mock_user_repo, client):
    mock_jwt_decode.return_value = {
        "sub": "5",
        "is_admin": True
    }
    fake_user=MagicMock()
    fake_user.id=5
    mock_user_repo.return_value=fake_user
    fake_cart = MagicMock()
    
    fake_cart.to_dict.return_value = {
        "id": 1,
        "user_id": 5,
        "status": "empty",
        "created_at": "2025-12-01 00:00:00"
    }
    mock_create.return_value = fake_cart
    response = client.post(
        "/shopping_carts/shopping_carts",
        json={
            "user_id":5,
            "status":"empty",
            "created_at":"2025-12-01 00:00:00"
                
        },
        headers={
            "Authorization": "Bearer fake_token"
        }
    )
    assert response.status_code == 201
    data = response.get_json()
    assert "message" in data
    assert data["message"] == "Shopping cart created successfully"


@patch("routes.shopping_cart_routes.shopping_cart_repo.get_by_id")
@patch("services.jwt_manager.jwt_manager.decode")
@patch("routes.shopping_cart_routes.shopping_cart_repo.update")
def test_update_shopping_cart_success(mock_update, mock_jwt_decode,mock_get_by_id, client):
    mock_jwt_decode.return_value = {"sub": "1", "is_admin": True}
    shopping_cart_id = "1"
    fake_cart = MagicMock()
    fake_cart.user_id = 5
    fake_cart.status = "empty"
    fake_cart.created_at = "2025-12-01 00:00:00"
    mock_get_by_id.return_value = fake_cart

    fake_cart_updated = MagicMock()
    fake_cart_updated.to_dict.return_value = {
        "id": 1,
        "user_id": 5,
        "status": "cancelled",
        "created_at": "2025-12-01 00:00:00"
    }
    mock_update.return_value = fake_cart_updated

    update_data = {
        "status": "cancelled",
        "created_at": "2025-12-01 00:00:00"
    }
    shopping_cart_id = "1"
    response = client.put(
        f"/shopping_carts/shopping_carts/{shopping_cart_id}",
        json=update_data,
        headers={"Authorization": "Bearer fake_token"}
    )
    
    assert response.status_code == 200
    assert f"Shopping cart with ID {shopping_cart_id} updated successfully" in response.get_json()["message"]


@patch("services.jwt_manager.jwt_manager.decode")
@patch("routes.shopping_cart_routes.shopping_cart_repo.delete")
def test_delete_shopping_cart_success(mock_delete, mock_jwt_decode, client):
    mock_jwt_decode.return_value = {"sub": "1", "is_admin": True}
    fake_shopping_cart = MagicMock()
    fake_shopping_cart.id = 1
    mock_delete.return_value = fake_shopping_cart
    shopping_cart_id = "1"
    response = client.delete(
        f"/shopping_carts/shopping_carts/{shopping_cart_id}",
        headers={"Authorization": "Bearer fake_token"}
    )
    assert response.status_code == 200
    assert f"Shopping cart with ID {shopping_cart_id} was deleted successfully" in response.get_json()["message"]





@patch("routes.shopping_cart_routes.shopping_cart_repo.get_by_id")
@patch("routes.shopping_cart_routes.shopping_cart_product_repo.get_by_shopping_cart_id")
@patch("services.jwt_manager.jwt_manager.decode")
def test_get_all_cart_products_empty(mock_jwt_decode, mock_get_products, mock_get_cart, client):
    mock_jwt_decode.return_value = {
        "sub": "1",
        "is_admin": True
    }
    fake_cart = MagicMock()
    fake_cart.user_id = 1
    mock_get_cart.return_value = fake_cart

    mock_get_products.return_value = []

    response = client.get(
        "/shopping_carts/shopping_carts/1/products",
        headers={
            "Authorization": "Bearer fake_token"
        }
    )

    assert response.status_code == 404
    data = response.get_json()
    assert data["data"] == []
    assert data["message"] == "No products found"


@patch("routes.shopping_cart_routes.shopping_cart_repo.get_by_id")
@patch("routes.shopping_cart_routes.product_repo.get_by_id")
@patch("routes.shopping_cart_routes.shopping_cart_product_repo.get_product_in_cart")
@patch("routes.shopping_cart_routes.shopping_cart_product_repo.create")
@patch("services.jwt_manager.jwt_manager.decode")
def test_add_product_to_cart_success(mock_jwt, mock_create_item, mock_get_existing, mock_get_product, mock_get_cart, client):
    mock_jwt.return_value = {
        "sub": "5", 
        "is_admin": False
    }

    fake_cart = MagicMock()
    fake_cart.user_id = 5
    mock_get_cart.return_value = fake_cart


    fake_product = MagicMock()
    fake_product.id = 10
    fake_product.quantity = 100 
    mock_get_product.return_value = fake_product

    mock_get_existing.return_value = None

    fake_item = MagicMock()
    fake_item.to_dict.return_value = {
        "shopping_cart_id": 1,
        "product_id": 10,
        "quantity": 2
    }
    mock_create_item.return_value = fake_item

    response = client.post(
        "/shopping_carts/shopping_carts/1/products",
        json={
            "product_id": 10,
            "quantity": 2
        },
        headers={"Authorization": "Bearer fake_token"}
    )

    assert response.status_code == 201
    data = response.get_json()
    assert data["product_id"] == 10
    assert data["quantity"] == 2


@patch("routes.shopping_cart_routes.shopping_cart_repo.get_by_id")
@patch("routes.shopping_cart_routes.shopping_cart_product_repo.get_product_in_cart")
@patch("routes.shopping_cart_routes.product_repo.get_by_id")
@patch("routes.shopping_cart_routes.shopping_cart_product_repo.update_quantity")
@patch("services.jwt_manager.jwt_manager.decode")
def test_update_product_quantity_success(mock_jwt, mock_update_qty, mock_get_product, mock_get_in_cart, mock_get_cart, client):
    mock_jwt.return_value = {
        "sub": "5", 
        "is_admin": False
    }

    fake_cart = MagicMock()
    fake_cart.user_id = 5
    mock_get_cart.return_value = fake_cart

    fake_cart_product = MagicMock()
    fake_cart_product.id = 100
    fake_cart_product.quantity = 2
    mock_get_in_cart.return_value = fake_cart_product

    fake_product = MagicMock()
    fake_product.quantity = 5
    mock_get_product.return_value = fake_product

    fake_updated_item = MagicMock()
    fake_updated_item.to_dict.return_value = {
        "id": 100,
        "shopping_cart_id": 1,
        "product_id": 10,
        "quantity": 5
    }
    mock_update_qty.return_value = fake_updated_item

    response = client.patch(
        "/shopping_carts/shopping_carts/1/products/10",
        json={"quantity": 5},
        headers={"Authorization": "Bearer fake_token"}
    )

    assert response.status_code == 200
    data = response.get_json()
    assert "updated in cart 1" in data["message"]
    assert data["shopping_cart_product"]["quantity"] == 5


@patch("routes.shopping_cart_routes.shopping_cart_repo.get_by_id")
@patch("routes.shopping_cart_routes.shopping_cart_product_repo.get_product_in_cart")
@patch("routes.shopping_cart_routes.shopping_cart_product_repo.delete")
@patch("services.jwt_manager.jwt_manager.decode")
def test_remove_product_from_cart_success(mock_jwt, mock_delete, mock_get_in_cart, mock_get_cart, client):
    mock_jwt.return_value = {
        "sub": "1", 
        "is_admin": True
    }

    fake_cart = MagicMock()
    fake_cart.user_id = 5 
    mock_get_cart.return_value = fake_cart

    fake_item = MagicMock()
    fake_item.id = 500
    mock_get_in_cart.return_value = fake_item

    mock_delete.return_value = True

    cart_id = 1
    product_id = 10
    response = client.delete(
        f"/shopping_carts/shopping_carts/{cart_id}/products/{product_id}",
        headers={"Authorization": "Bearer fake_token"}
    )

    assert response.status_code == 200
    data = response.get_json()
    assert f"Product with ID {product_id} was removed from cart {cart_id}" == data["message"]