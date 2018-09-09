import unittest # Importing the unittest module

from user import User # Importing the user class

class TestUser(unittest.TestCase):
    '''
    class  called TestUser, that inherits from unittest TestCase
    '''
    def setUp(self):
        '''
        create user object
        '''
        self.new_user = User("Mister","moha123")

    def tearDown(self):
        '''
        create empty object list that runs before every test
        '''
        User.user = []

    def test_init(self):
        '''
        test to confirm if user class object has been instantiated correctly
        '''
        self.assertEqual(self.new_user.username, "Mister")
        self.assertEqual(self.new_user.password, "moha123")

    def test_save_user(self):
        '''
        create test to save user object
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user),1)


if __name__ == '__main__':
    unittest.main()