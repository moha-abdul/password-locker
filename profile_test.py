import unittest # Importing the unittest module

from profile import Profile #Importing the profile class

class TestProfile(unittest.TestCase):
    '''
    class  called TestProfile, that inherits from unittest TestCase
    '''
    def setUp(self):
        '''
        create profile object
        '''
        self.new_profile = Profile("youtube", "1234mister")

    def tearDown(self):
        '''
        create empty object list that runs before every test
        '''
        Profile.profile = []

    def test_init(self):
        '''
          test to confirm if profile class object has been instantiated correctly
        '''
        self.assertEqual(self.new_profile.account, "youtube")
        self.assertEqual(self.new_profile.password, "1234mister")
        

    def test_save_profile(self):
        '''
        create test to save profile object
        '''
        self.new_profile.save_profile()
        self.assertEqual(len(Profile.profile),1)

    def test_delete_profile(self):
        '''
        create test to delete profile object
        '''
        self.new_profile.save_profile()
        test_profile = Profile("Test_Account", "meed") # new test profile
        test_profile.save_profile()
        self.new_profile.delete_profile()
        self.assertEqual(len(Profile.profile),1)

    def test_find_profile_by_account(self):
        '''
        create test to find profile by account
        '''
        self.new_profile.save_profile()
        test_profile = Profile("Test", "userpass") # new test profile
        test_profile.save_profile()
        found_profile = Profile.find_profile_by_account("Test")

        self.assertEqual(found_profile.account, test_profile.account)

    def test_display_profiles(self):
        '''
        create test to display all profiles
        '''
        return Profile.display_profiles(self)


if __name__ == '__main__':
    unittest.main()
