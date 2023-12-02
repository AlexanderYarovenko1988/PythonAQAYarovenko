import requests
import json
import logging

BASE_URL = "https://reqres.in/api"

# Настроим базовый логгер
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ReqresUser:
    def __init__(self, id, email, first_name, last_name, avatar):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar

def get_users(page=1):
    params = {"page": page}
    response = requests.get(f"{BASE_URL}/users", params=params)
    logger.info(f"GET {BASE_URL}/users - Status Code: {response.status_code}")
    return response


def get_user(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    logger.info(f"GET {BASE_URL}/users/{user_id} - Status Code: {response.status_code}")
    return response

def get_list_resource():
    response = requests.get(f"{BASE_URL}/unknown")
    logger.info(f"GET {BASE_URL}/unknown - Status Code: {response.status_code}")
    return response

def get_single_resource(resource_id):
    response = requests.get(f"{BASE_URL}/unknown/{resource_id}")
    logger.info(f"GET {BASE_URL}/unknown/{resource_id} - Status Code: {response.status_code}")
    return response

def create_user(user_data):
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    logger.info(f"POST {BASE_URL}/users - Status Code: {response.status_code}")
    return response

def update_user(user_id, user_data):
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=user_data)
    logger.info(f"PUT {BASE_URL}/users/{user_id} - Status Code: {response.status_code}")
    return response

def update_user_patch(user_id, data):
    endpoint = f"{BASE_URL}/users/{user_id}"
    response = requests.patch(endpoint, json=data)
    logger.info(f"PATCH {endpoint} - Status Code: {response.status_code}")
    return response

def delete_user(user_id):
    url = f"{BASE_URL}/users/{user_id}"
    response = requests.delete(url)
    logger.info(f"DELETE {url} - Status Code: {response.status_code}")
    return response
