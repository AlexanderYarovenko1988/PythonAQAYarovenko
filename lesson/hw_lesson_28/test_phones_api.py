import lesson.hw_lesson_28.infrasstructure_api_phone as infra

def test_get_objects():
    objects = infra.get_objects()
    assert len(objects) == 13


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


def test_get_single_object():
    created_object = infra.create_an_object({"name": "Test Object", "data": {"color": "Red"}})
    object_id = created_object["id"]
    response = infra.get_an_object(object_id)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    data = response.json()
    assert data["id"] == str(object_id), "Object ID doesn't match"
    assert data["name"] == "Test Object", "Object name doesn't match"
    assert data["data"]["color"] == "Red", "Object color doesn't match"


def test_get_nonexistent_object_1():
    created_object = infra.create_an_object({"name": "Nonexistent Object", "data": {"color": "Blue"}})
    object_id = str(created_object["id"])
    response = infra.get_an_object(object_id + "1")
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"


def test_patch_object_with_invalid_data():
    created_object = infra.create_an_object({"name": "Test Object", "data": {"color": "Red"}})
    object_id = created_object["id"]

    invalid_data = {"invalid_key": "Invalid Value"}
    response = infra.patch_an_object(object_id, invalid_data)
    print(response.text)

    assert response.status_code == 404, f"Очікувався статусний код 404, але отримано {response.status_code}"
    assert "No valid field(s) to update have been passed" in response.text, "Повідомлення про помилку не збігається"

    unchanged_object = infra.get_object(object_id)
    assert unchanged_object is not None, "Не вдалося отримати незмінений об'єкт"

    assert unchanged_object["name"] == "Test Object", "Поле Name було неправильно змінено"
    assert unchanged_object["data"]["color"] == "Red", "Поле Color було неправильно змінено"





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
    created_object = infra.create_an_object({"name": "Test Object", "data": {"color": "Red"}})
    object_id = created_object["id"]

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

    response = infra.put_an_object(object_id, updated_object)
    assert response.status_code == 200, f"PUT request failed with status code {response.status_code}"
    modified_object = infra.get_object(object_id)
    assert modified_object is not None, "Failed to retrieve the modified object"

    assert modified_object["name"] == updated_object["name"], "Name field was not updated"
    assert modified_object["data"] == updated_object["data"], "Data field was not updated"




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
    created_object = infra.create_an_object({"name": "Test Object", "data": {"color": "Red"}})
    object_id = created_object["id"]
    invalid_data = {"invalid_key": "Invalid Value"}
    response = infra.put_an_object(object_id, invalid_data)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"


def test_put_object_with_missing_name():
    created_object = infra.create_an_object({"name": "Test Object", "data": {"color": "Red"}})
    object_id = created_object["id"]
    object_without_name = {
        "data": {
            "year": 2021,
            "price": 1299.99,
            "CPU model": "AMD Ryzen 9",
            "Hard disk size": "512 GB SSD"
        }
    }

    response = infra.put_an_object(object_id, object_without_name)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"


def test_put_object_with_missing_data():
    created_object = infra.create_an_object({"name": "Test Object", "data": {"color": "Red"}})
    object_id = created_object["id"]

    object_without_data = {
        "name": "Dell XPS 13"
    }

    response = infra.put_an_object(object_id, object_without_data)
    assert response.status_code == 200, f"PUT request failed with status code {response.status_code}"

    modified_object = infra.get_object(object_id)
    assert modified_object is not None, "Failed to retrieve the modified object"

    assert modified_object["name"] == object_without_data["name"], "Name field was not updated"
    assert "data" in modified_object, "Data field was not retained"



def test_put_object_with_empty_data():
    object_with_empty_data = {
        "name": "HP Spectre x360",
        "data": {}
    }

    response = infra.put_an_object(7, object_with_empty_data)
    assert response.status_code == 200

    modified_object = response.json()
    assert modified_object["name"] == object_with_empty_data["name"]
    assert modified_object["data"] == object_with_empty_data["data"]
    assert "id" in modified_object
    assert "updatedAt" in modified_object


def test_patch_object_name():
    # Створюємо об'єкт для тестування
    created_object = infra.create_an_object({"name": "Test Object", "data": {"color": "Red"}})
    object_id = created_object["id"]

    # Запит на патч об'єкта тільки для поля "name"
    updated_name = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }

    response = infra.patch_an_object(object_id, updated_name)

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    modified_object = response.json()
    assert modified_object["id"] == object_id
    assert modified_object["name"] == updated_name["name"]
    assert "data" in modified_object
    assert "updatedAt" in modified_object

    assert modified_object["data"]["color"] == "Red", "Other fields were incorrectly modified"


def test_patch_object_data():
    created_object = infra.create_an_object({"name": "Test Object", "data": {"color": "Red"}})
    object_id = created_object["id"]

    updated_data = {
        "data": {
            "year": 2020,
            "price": 1999.99,
            "CPU model": "Intel Core i7",
            "Hard disk size": "2 TB"
        }
    }

    response = infra.patch_an_object(object_id, updated_data)

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    modified_object = response.json()
    assert modified_object["id"] == object_id
    assert "name" in modified_object
    assert modified_object["data"] == updated_data["data"]
    assert "updatedAt" in modified_object

    assert modified_object["name"] == "Test Object", "Name field was incorrectly modified"


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
    assert response.status_code == 200

    modified_object = response.json()
    assert modified_object["id"] == "7"
    assert modified_object["name"] == updated_info["name"]
    assert modified_object["data"] == updated_info["data"]
    assert "updatedAt" in modified_object


def test_delete_object():

    created_object = infra.create_an_object({"name": "Test Object", "data": {"color": "Red"}})
    object_id = created_object["id"]

    response_deleted_object = infra.delete_an_object(object_id)

    assert response_deleted_object.status_code == 200, f"Expected status code 200, but got {response_deleted_object.status_code}"
    deleted_object = infra.get_object(object_id)
    assert deleted_object is None, "Object was not deleted"



def test_delete_nonexistent_object():
    # Спроба видалити об'єкт, якого не існує (ID = 'ff8081818c01d7ae018c299e89c827fa')
    response = infra.delete_an_object('ff8081818c01d7ae018c299e89c827fa')
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"



def test_delete_object_with_invalid_id():
    response = infra.delete_an_object('-1')
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"


def test_delete_object_with_missing_id():
    response = infra.delete_an_object(None)
    assert response.status_code == 404
