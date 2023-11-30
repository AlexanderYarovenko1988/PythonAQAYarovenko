import requests
import json

url = "https://api.restful-api.dev/objects"


class Phone:
    def __init__(self, id, name, data):
        self.id = id
        self.name = name
        self.data = data


def get_an_object(object_id):
    return requests.get(f"{url}/{object_id}")


def get_objects():
    response = requests.get(url)
    if response.status_code == 200:
        objects = response.json()
        return [Phone(**item) for item in objects]
    return None


def get_object(object_id):
    response = requests.get(f"{url}/{object_id}")
    if response.status_code == 200:
        return response.json()
    return None


def post_an_object(new_object):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(new_object), headers=headers)
    return response


def put_an_object(object_id, updated_object):
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f"{url}/{object_id}", data=json.dumps(updated_object), headers=headers)
    return response


def patch_an_object(object_id, updated_info):
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f"{url}/{object_id}", data=json.dumps(updated_info), headers=headers)
    return response


def delete_an_object(object_id):
    response = requests.delete(f"{url}/{object_id}")
    return response


