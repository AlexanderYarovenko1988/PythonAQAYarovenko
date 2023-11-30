import lesson.hw_lesson_28.infrasstructure_api_phone as infra


def test_get_objects():
    objects = infra.get_objects()
    assert len(objects) == 13


def test_get_single_object():
    response = infra.get_an_object(5)
    assert response.status_code == 200
    phone = infra.Phone(**response.json())
    assert phone.id == "5"
    assert phone.name == "Samsung Galaxy Z Fold2"
    assert phone.data["price"] == 689.99
    assert phone.data["color"] == "Brown"


def test_get_single_object_by_id():
    response = infra.get_object(1)
    assert response["id"] == "1"
    assert response["name"] == "Google Pixel 6 Pro"
    assert response["data"]["color"] == "Cloudy White"


def test_get_object_with_null_data():
    response = infra.get_object(2)
    assert response["id"] == "2"
    assert response["name"] == "Apple iPhone 12 Mini, 256GB, Blue"
    assert response["data"] is None


def test_get_object_with_invalid_id():
    response = infra.get_object(-1)
    assert response is None


def test_get_multiple_objects():
    response = infra.get_an_object([3, 5, 10])
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3

    # Перевірка першого об'єкта
    assert data[0]["id"] == "3"
    assert data[0]["name"] == "Apple iPhone 12 Pro Max"
    assert data[0]["data"]["color"] == "Cloudy White"
    assert data[0]["data"]["capacity GB"] == 512

    # Перевірка другого об'єкта
    assert data[1]["id"] == "5"
    assert data[1]["name"] == "Samsung Galaxy Z Fold2"
    assert data[1]["data"]["price"] == 689.99
    assert data[1]["data"]["color"] == "Brown"

    # Перевірка третього об'єкта
    assert data[2]["id"] == "10"
    assert data[2]["name"] == "Apple iPad Mini 5th Gen"
    assert data[2]["data"]["Capacity"] == "64 GB"
    assert data[2]["data"]["Screen size"] == 7.9


def test_get_nonexistent_object_1():
    response = infra.get_an_object(999)
    assert response.status_code == 404


def test_get_objects_with_invalid_ids_1():
    response = infra.get_an_object([1, 'abc', 7])
    assert response.status_code == 400


def test_get_specific_object():
    response = infra.get_an_object(7)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "7"
    assert data["name"] == "Apple MacBook Pro 16"
    assert data["data"]["year"] == 2019
    assert data["data"]["price"] == 1849.99
    assert data["data"]["CPU model"] == "Intel Core i9"
    assert data["data"]["Hard disk size"] == "1 TB"


def test_post_object():
    new_object = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }

    response = infra.post_an_object(new_object)
    assert response.status_code == 200

    created_object = response.json()
    assert created_object["name"] == new_object["name"]
    assert created_object["data"] == new_object["data"]
    assert "id" in created_object
    assert "createdAt" in created_object


def test_post_object_with_invalid_data():
    invalid_object = {
        "invalid_key": "Invalid Value"
    }

    response = infra.post_an_object(invalid_object)
    assert response.status_code == 200


def test_post_object_with_missing_name():
    object_without_name = {
        "data": {
            "year": 2021,
            "price": 1299.99,
            "CPU model": "AMD Ryzen 9",
            "Hard disk size": "512 GB SSD"
        }
    }

    response = infra.post_an_object(object_without_name)
    assert response.status_code == 200


def test_post_object_with_missing_data():
    object_without_data = {
        "name": "Dell XPS 13"
    }

    response = infra.post_an_object(object_without_data)
    assert response.status_code == 200


def test_post_object_with_empty_data():
    object_with_empty_data = {
        "name": "HP Spectre x360",
        "data": {}
    }

    response = infra.post_an_object(object_with_empty_data)
    assert response.status_code == 200

    created_object = response.json()
    assert created_object["name"] == object_with_empty_data["name"]
    assert created_object["data"] == object_with_empty_data["data"]
    assert "id" in created_object
    assert "createdAt" in created_object

def test_put_object():
    updated_object = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }

    response = infra.put_an_object(7, updated_object)
    assert response.status_code == 405

    if response.status_code == 200:
        modified_object = response.json()
        assert modified_object["name"] == updated_object["name"]
        assert modified_object["data"] == updated_object["data"]
        assert "id" in modified_object
        assert "updatedAt" in modified_object
    else:
        print(f"PUT request failed with status code {response.status_code}")


def test_put_object_with_invalid_id():
    updated_object = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }

    response = infra.put_an_object(-1, updated_object)
    assert response.status_code == 404

def test_put_object_with_invalid_data():
    invalid_object = {
        "invalid_key": "Invalid Value"
    }

    response = infra.put_an_object(7, invalid_object)
    assert response.status_code == 405

def test_put_object_with_missing_name():
    object_without_name = {
        "data": {
            "year": 2021,
            "price": 1299.99,
            "CPU model": "AMD Ryzen 9",
            "Hard disk size": "512 GB SSD"
        }
    }

    response = infra.put_an_object(7, object_without_name)
    assert response.status_code == 405

def test_put_object_with_missing_data():
    object_without_data = {
        "name": "Dell XPS 13"
    }

    response = infra.put_an_object(7, object_without_data)
    assert response.status_code == 405

def test_put_object_with_empty_data():
    object_with_empty_data = {
        "name": "HP Spectre x360",
        "data": {}
    }

    response = infra.put_an_object(7, object_with_empty_data)
    assert response.status_code == 405

    modified_object = response.json()
    assert modified_object["name"] == object_with_empty_data["name"]
    assert modified_object["data"] == object_with_empty_data["data"]
    assert "id" in modified_object
    assert "updatedAt" in modified_object

def test_patch_object_name():
    updated_name = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }

    response = infra.patch_an_object(7, updated_name)
    assert response.status_code == 405

    modified_object = response.json()
    assert modified_object["id"] == "7"
    assert modified_object["name"] == updated_name["name"]
    assert "data" in modified_object
    assert "updatedAt" in modified_object


def test_patch_object_data():
    updated_data = {
        "data": {
            "year": 2020,
            "price": 1999.99,
            "CPU model": "Intel Core i7",
            "Hard disk size": "2 TB"
        }
    }

    response = infra.patch_an_object(7, updated_data)
    assert response.status_code == 405

    modified_object = response.json()
    assert modified_object["id"] == "7"
    assert "name" in modified_object
    assert modified_object["data"] == updated_data["data"]
    assert "updatedAt" in modified_object


def test_patch_object_name_and_data():
    updated_info = {
        "name": "Apple MacBook Pro 16 (Updated Name)",
        "data": {
            "year": 2020,
            "price": 1999.99,
            "CPU model": "Intel Core i7",
            "Hard disk size": "2 TB"
        }
    }

    response = infra.patch_an_object(7, updated_info)
    assert response.status_code == 405

    modified_object = response.json()
    assert modified_object["id"] == "7"
    assert modified_object["name"] == updated_info["name"]
    assert modified_object["data"] == updated_info["data"]
    assert "updatedAt" in modified_object


def test_patch_object_with_invalid_data():
    invalid_info = {
        "invalid_key": "Invalid Value"
    }

    response = infra.patch_an_object(7, invalid_info)
    assert response.status_code == 405


def test_delete_object():
    response = infra.delete_an_object(6)
    assert response.status_code == 200

    deleted_message = response.json()
    assert deleted_message["message"] == "Object with id = 6, has been deleted."


def test_delete_nonexistent_object():
    response = infra.delete_an_object(999)
    assert response.status_code == 404


def test_delete_object_with_invalid_id():
    response = infra.delete_an_object(-1)
    assert response.status_code == 404


def test_delete_object_with_missing_id():
    response = infra.delete_an_object(None)
    assert response.status_code == 404