import unittest
from lesson.hw_lesson_31.models.users import Users
from lesson.hw_lesson_31.repositories.users_repositories import UsersRepository

class TestUsersRepository(unittest.TestCase):

    def test_add_user_from_api_success(self):
        users_repository = UsersRepository()
        users_repository.add_user_from_api()
        all_users = users_repository.get_all()
        self.assertTrue(len(all_users) > 0)

    def test_user_with_specific_id_in_database(self):
        users_repository = UsersRepository()
        all_users = users_repository.get_all()
        user_with_id_exists = any(user.id == 'ff8081818c01d7ae018c49d896834ceb' for user in all_users)
        self.assertTrue(user_with_id_exists)



if __name__ == '__main__':
    unittest.main()
