import unittest
import pyperclip
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Mister", "Moham", "moha")

    def tearDown(self):
        User.user = []

    def test_init(self):
        self.assertEqual(self.new_user.first_name, "Mister")
        self.assertEqual(self.new_user.last_name, "Moham")
        self.assertEqual(self.new_user.username, "moha")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user),1)

    # def test_find_user_by_username(self):
    #     self.new_user.save_user()
    #     test_user = User("Test", "Mohah", "usertest") # new test user
    #     test_user.save_user()
        
    #     found_user = User.find_user_by_username("usertest")

    #     self.assertEqual(found_user.username, test_user.username)

    # def test_user_exists(self):
    #     self.new_user.save_user()
    #     test_user = User("Test", "User", "moood") # new test user
    #     test_user.save_user()

    #     user_exists = User.user_exists("moood")

    #     self.assertTrue(user_exists)

    # def test_copy_password(self):
    #     self.new_user.save_user()
    #     self.new_user.password = password_found
    #     pyperclip.copy(password_found)
    #     # User.copy_password("0718")

        # self.assertEqual(self.new_user.password, pyperclip.paste())

if __name__ == '__main__':
    unittest.main()