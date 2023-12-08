# users_repositories.py

from lesson.hw_lesson_31.session_handler import session
from lesson.hw_lesson_31.models.users import Users
import requests


class UsersRepository:
    def __init__(self):
        self.__session = session

    def add_one_row(self, user):
        self.__session.add(user)
        self.__session.commit()

    def get_all(self):
        return self.__session.query(Users).all()

    def get_user_by_id(self, user_id):
        return self.__session.query(Users).filter_by(id=user_id).first()

    def get_user_by_first_name(self, user_name):
        return self.__session.query(Users).filter_by(name=user_name).all()

    def add_user_from_api(self):
        # Пример добавления данных из API-запроса
        url = "https://api.restful-api.dev/objects"
        data = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }

        response = requests.post(url, json=data)

        if response.status_code == 200:
            result_data = response.json()
            user_to_add = Users(
                id=result_data['id'],
                name=result_data['name'],
                createdAt=result_data['createdAt'],
            )
            self.add_one_row(user_to_add)

            print("Данные успешно добавлены в базу данных.")
        else:
            print(f"Ошибка при выполнении запроса: {response.status_code}")

        response = requests.post(url, json=data)

        if response.status_code == 200:
            result_data = response.json()
            user_to_add = Users(
                id=result_data['id'],
                name=result_data['name'],
                createdAt=result_data['createdAt'],
            )
            self.add_one_row(user_to_add)

            print("Данные успешно добавлены в базу данных.")
        else:
            print(f"Ошибка при выполнении запроса: {response.status_code}")


users_repository = UsersRepository()
users_repository.add_user_from_api()
all_users = users_repository.get_all()
for user in all_users:
    print(user)

print(f"Пользователь по ID: {users_repository.get_user_by_id('ff8081818c01d7ae018c49d896834ceb')}")
