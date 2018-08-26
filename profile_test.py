import unittest
import pyperclip
from profile import Profile

class TestProfile(unittest.TestCase):
    def setUp(self):
        self.new_profile = Profile("Mister", "mohamed", "7")

    def tearDown(self):
        Profile.profile = []

    def test_init(self):
        self.assertEqual(self.new_profile.account, "twitter")
        self.assertEqual(self.new_profile.password, "1234mister")
        self.assertEqual(self.new_profile.pass_length, "10")
        

    def test_save_profile(self):
        self.new_profile.save_profile()
        self.assertEqual(len(Profile.profile),1)

    def test_delete_profile(self):
        self.new_profile.save_profile()
        test_profile = Profile("Test", "meed", "10") # new test profile
        test_profile.save_profile()
        self.new_profile.delete_profile()
        self.assertEqual(len(Profile.profile),1)

    def test_find_profile_by_account(self):
        self.new_profile.save_profile()
        test_profile = Profile("Test", "usertest", "10") # new test profile
        test_profile.save_profile()
        found_profile = Profile.find_profile_by_account("usertest")

        self.assertEqual(found_profile.account, test_profile.account)

    def test_display_profiles(self):
        return Profile.display_profiles(self)

    def test_password_generate(self):
        """
        This will  test if the password generator works.
        """
        self.new_profile.save_profile()
        random_password = self.new_profile.password_generate("17")
        self.assertNotEqual(random_password, self.new_profile.password)
