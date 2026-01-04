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
@patch("routes.product_routes.product_repo.get_all")
def test_get_all_products_empty(mock_get_all,mock_cache, mock_jwt_decode, client):
    mock_jwt_decode.return_value = {
        "sub": "1",
        "is_admin": True
    }
    mock_cache.check_key.return_value=False
    mock_get_all.return_value = []
    response = client.get("/products/products", headers={
            "Authorization": "Bearer fake_token"
        })
    assert response.status_code == 404
    data = response.get_json()
    assert "data" in data
    assert data["message"] == "No products found"
    assert data["data"] == []
    


@patch("services.jwt_manager.jwt_manager.decode")
@patch("routes.product_routes.product_repo.get_all")
def test_get_all_products_success(mock_get_all, mock_jwt_decode, client):
    mock_jwt_decode.return_value = {
        "sub": "1",
        "is_admin": True
    }
    fake_product = MagicMock()
    fake_product.to_dict.return_value = {
        "id": 1,
        "sku": "DOG-001",
        "name": "Dog Food",
        "price": 10.0,
        "description": "Food for dogs",
        "quantity": 5
    }
    mock_get_all.return_value = [fake_product]
    response = client.get("/products/products", headers={
            "Authorization": "Bearer fake_token"
        })
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["name"] == "Dog Food"


@patch("services.jwt_manager.jwt_manager.decode")
@patch("routes.product_routes.product_repo.get_by_id")
def test_get_product_by_id_empty(mock_get_by_id, mock_jwt_decode, client):
    mock_jwt_decode.return_value = {
        "sub": "1",
        "is_admin": True
    }
    mock_get_by_id.return_value = None
    response = client.get(
        "/products/products/1",
        headers={
            "Authorization": "Bearer fake_token"
        }
    )
    assert response.status_code == 404
    data = response.get_json()
    assert data["message"] == "No product found"


@patch("services.jwt_manager.jwt_manager.decode")
@patch("routes.product_routes.product_repo.create")
def test_create_product_missing_fields(mock_create, mock_jwt_decode, client):
    mock_jwt_decode.return_value = {
        "sub": "1",
        "is_admin": True
    }


    response = client.post(
        "/products/products",
        json={
            "sku":"PRE-76908",
            "name":"Dry dog food"
        },
        headers={
            "Authorization": "Bearer fake_token"
        }
    )
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
    mock_create.assert_not_called()


@patch("services.jwt_manager.jwt_manager.decode")
@patch("routes.product_routes.product_repo.create")
def test_create_product_success(mock_create, mock_jwt_decode, client):
    mock_jwt_decode.return_value = {
        "sub": "1",
        "is_admin": True
    }


    response = client.post(
        "/products/products",
        json={
            "sku":"PRE-76908",
            "name":"Dry dog food",
            "price":3600,
            "description":"Nutritios formula",
            "quantity":7
                
        },
        headers={
            "Authorization": "Bearer fake_token"
        }
    )
    assert response.status_code == 201
    data = response.get_json()
    assert "message" in data
    assert data["message"] == "Product created succesfully"


@patch("services.jwt_manager.jwt_manager.decode")
@patch("routes.product_routes.product_repo.update")
def test_update_product_success(mock_update, mock_jwt_decode, client):
    mock_jwt_decode.return_value = {"sub": "1", "is_admin": True}
    fake_product = MagicMock()
    fake_product.id = 1
    fake_product.name = "Updated Dog Food"
    mock_update.return_value = fake_product
    update_data = {
        "name": "Updated Dog Food",
        "price": 45.0
    }
    product_id = "1"
    response = client.put(
        f"/products/products/{product_id}",
        json=update_data,
        headers={"Authorization": "Bearer fake_token"}
    )
    
    assert response.status_code == 200
    assert f"Product with ID {product_id} was updated successfully" in response.get_json()["message"]

@patch("services.jwt_manager.jwt_manager.decode")
@patch("routes.product_routes.product_repo.delete")
def test_delete_product_success(mock_delete, mock_jwt_decode, client):
    mock_jwt_decode.return_value = {"sub": "1", "is_admin": True}
    fake_product = MagicMock()
    fake_product.id = 1
    fake_product.name = "Updated Dog Food"
    mock_delete.return_value = fake_product
    product_id = "1"
    response = client.delete(
        f"/products/products/{product_id}",
        headers={"Authorization": "Bearer fake_token"}
    )
    assert response.status_code == 200
    assert f"Product with ID {product_id} was deleted successfully" in response.get_json()["message"]
