import lesson.hw_lesson_29.infrastructure_api_reqres as infra
import logging
import sys
import pytest

# Настроим базовый логгер для тестов
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture
def created_user():
    # Создаем пользователя
    response_create = infra.create_user({
        "name": "John Doe",
        "job": "Developer"
    })
    assert response_create.status_code == 201
    created_user_id = response_create.json()["id"]
    yield created_user_id  # Этот блок выполняется после завершения тестов
    # Удаляем созданного пользователя после завершения теста
    response_delete = infra.delete_user(user_id=created_user_id)
    logger.info(f"Fixture: Deleting created user - Status Code: {response_delete.status_code}")

def test_get_users_page_positive():
    response = infra.get_users(page=2)
    logger.info(f"test_get_users_page_positive - Status Code: {response.status_code}")

    assert response.status_code == 200
    data = response.json()
    assert data["page"] == 2
    assert data["per_page"] == 6
    assert data["total"] == 12
    assert data["total_pages"] == 2
    assert len(data["data"]) == 6

def test_get_users_page_negative():
    response = infra.get_users(page=1000)
    logger.info(f"test_get_users_page_negative - Status Code: {response.status_code}")

    assert response.status_code == 200
    data = response.json()
    assert not data["data"]

def test_get_user_positive():
    response = infra.get_user(user_id=2)
    logger.info(f"test_get_user_positive - Status Code: {response.status_code}")

    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    user_data = data["data"]
    assert user_data["id"] == 2
    assert user_data["email"] == "janet.weaver@reqres.in"
    assert user_data["first_name"] == "Janet"
    assert user_data["last_name"] == "Weaver"
    assert user_data["avatar"] == "https://reqres.in/img/faces/2-image.jpg"

def test_get_nonexistent_user_negative():
    response = infra.get_user(user_id=23)
    logger.info(f"test_get_nonexistent_user_negative - Status Code: {response.status_code}")

    assert response.status_code == 404
    assert not response.json()

def test_get_nonexistent_user_negative_alternative():
    response = infra.get_user(user_id=23)
    logger.info(f"test_get_nonexistent_user_negative_alternative - Status Code: {response.status_code}")

    assert response.status_code == 404
    data = response.json()
    assert "data" not in data

def test_get_list_resource_positive():
    response = infra.get_list_resource()
    logger.info(f"test_get_list_resource_positive - Status Code: {response.status_code}")

    assert response.status_code == 200
    data = response.json()
    assert "page" in data
    assert "per_page" in data
    assert "total" in data
    assert "total_pages" in data
    assert "data" in data
    assert len(data["data"]) == 6

def test_get_list_resource_negative():
    response = infra.get_list_resource()
    logger.info(f"test_get_list_resource_negative - Status Code: {response.status_code}")

    assert response.status_code != 404

def test_get_single_resource_positive():
    response = infra.get_single_resource(resource_id=2)
    logger.info(f"test_get_single_resource_positive - Status Code: {response.status_code}")

    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    resource_data = data["data"]
    assert resource_data["id"] == 2
    assert resource_data["name"] == "fuchsia rose"
    assert resource_data["year"] == 2001
    assert resource_data["color"] == "#C74375"
    assert resource_data["pantone_value"] == "17-2031"

def test_get_nonexistent_single_resource_negative():
    response = infra.get_single_resource(resource_id=23)
    logger.info(f"test_get_nonexistent_single_resource_negative - Status Code: {response.status_code}")

    assert response.status_code == 404
    assert not response.json()

def test_get_nonexistent_single_resource_negative_alternative():
    response = infra.get_single_resource(resource_id=23)
    logger.info(f"test_get_nonexistent_single_resource_negative_alternative - Status Code: {response.status_code}")

    assert response.status_code == 404
    data = response.json()
    assert "data" not in data

def test_create_user_positive():
    user_data = {
        "name": "morpheus",
        "job": "leader"
    }
    response = infra.create_user(user_data)
    logger.info(f"test_create_user_positive - Status Code: {response.status_code}")

    assert response.status_code == 201
    created_user_data = response.json()
    assert "id" in created_user_data
    assert created_user_data["name"] == user_data["name"]
    assert created_user_data["job"] == user_data["job"]

def test_update_user_positive():
    user_data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = infra.update_user(2, user_data)
    logger.info(f"test_update_user_positive - Status Code: {response.status_code}")

    assert response.status_code == 200
    updated_user_data = response.json()
    assert "updatedAt" in updated_user_data
    assert updated_user_data["name"] == user_data["name"]
    assert updated_user_data["job"] == user_data["job"]

def test_update_user_invalid_id_negative():
    user_data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = infra.update_user(-1, user_data)
    logger.info(f"test_update_user_invalid_id_negative - Status Code: {response.status_code}")

    if response.status_code != 200:
        error_data = response.json()
        assert "error" in error_data
        assert "user not found" in str(error_data).lower()

def test_delete_created_user(created_user):
    response_delete = infra.delete_user(user_id=created_user)
    logger.info(f"test_delete_created_user - Status Code: {response_delete.status_code}")
    assert response_delete.status_code == 204
