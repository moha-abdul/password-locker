import unittest
import pyperclip
from profile import Profile

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_profile = Profile("Mister", "Moham")