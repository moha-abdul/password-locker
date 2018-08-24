import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Mister", "Moham", "moha", "12345")

    def test_init(self):
        self.assertEqual(self.new_user.first_name, "Mister")
        self.assertEqual(self.new_user.last_name, "Moham")
        self.assertEqual(self.new_user.username, "moha")
        self.assertEqual(self.new_user.password, "12345")

if __name__ == '__main__':
    unittest.main()