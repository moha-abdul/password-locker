import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Mister", "Moham", "moha", "12345")

    def tearDown(self):
        User.user = []

    def test_init(self):
        self.assertEqual(self.new_user.first_name, "Mister")
        self.assertEqual(self.new_user.last_name, "Moham")
        self.assertEqual(self.new_user.username, "moha")
        self.assertEqual(self.new_user.password, "12345")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user),1)

    def test_delete_user(self):
        self.new_user.save_user()
        test_user = User("Test", "meed", "useeer", "23456") # new test user
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user),1)

    def test_find_user_by_username(self):
        self.new_user.save_user()
        test_user = User("Test", "Mohah", "usertest", "12457") # new test user
        test_user.save_user()
        
        found_user = User.find_user_by_username("usertest")

        self.assertEqual(found_user.username, test_user.username)

    def test_user_exists(self):
        self.new_user.save_user()
        test_user = User("Test", "User", "moood", "0711223344") # new test user
        test_user.save_user()

        user_exists = User.user_exists("moood")

        self.assertTrue(user_exists)

if __name__ == '__main__':
    unittest.main()