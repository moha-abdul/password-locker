import pyperclip
import random

class Profile:
    profile = []
    '''
    this class creates  new instance of user data
    '''
    def __init__(self, account, password, pass_length):
        self.account = account
        self.password = password
        self.pass_length = pass_length

    def new_profile(self):
        Profile.profile.append(self)

    def save_profile(self):
        Profile.profile.append(self)

    def delete_profile(self):
        Profile.profile.remove(self)

    @classmethod
    def find_profile_by_account(cls, account):
        for profile in cls.profile:
            if profile.account == account:
                return profile
    
    @classmethod
    def display_profiles(cls, profile):
        return cls.profile
    
    @classmethod
    def profile_exists(cls, account):
        for profile in cls.profile:
            if profile.account == account:
                return True

        return False
    
    @classmethod
    def password_generate(cls, pass_length):
        string = "abcdefghigjkmnopqrstuvwxyz1234567890-_=+{}\|"';>./,`!@#$^&*()`'
        password = "".join(random.sample(string, int(pass_length)))
        account_passsword = password
        return account_passsword