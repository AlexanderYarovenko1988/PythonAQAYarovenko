from lesson.hw_lesson_30.session_handler import session
from lesson.hw_lesson_30.models.users import Users

class UsersRepository:
    def __init__(self):
        self.__session = session

    def add_one_row(self, user):
        self.__session.add(user)
        self.__session.commit()

    def get_all(self):
        list_of_users = []
        for user in self.__session.query(Users).all():
            list_of_users.append(user)
        return list_of_users

    def get_user_by_id(self, user_id):
        return self.__session.get(Users, {'id': user_id})



users_repository = UsersRepository()
# user_to_add = Users(id='cccc', first_name='Alejandro', last_name='Vallejo', email='alejandro@gmail.com')
# users_repository.add_one_row(user_to_add)
all_users = users_repository.get_all()
for user in all_users:
    print(user)

print(f"the user we`re looking for is {users_repository.get_user_by_id('AAAAA')}")