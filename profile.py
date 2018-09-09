# import random

class Profile:
    profile = []
    '''
    this class creates  new instance of user data
    '''
    def __init__(self, account, password):
        self.account = account
        self.password = password

    def new_profile(self):
        '''
           Method that creates a profile
        '''
        Profile.profile.append(self)

    def save_profile(self):
        '''
           Method that saves a profile
        '''
        Profile.profile.append(self)

    def delete_profile(self):
        '''
           Method that deletes a profile
        '''
        Profile.profile.remove(self)

    @classmethod
    def find_profile_by_account(cls, account):
        '''
           Method that finds a profile by account name
        '''
        for profile in cls.profile:
            if profile.account == account:
                return profile
    
    @classmethod
    def display_profiles(cls, profile):
        '''
           Method that displays all profiles
        '''
        return cls.profile
    
    @classmethod
    def profile_exists(cls, account):
        '''
           Method that checks if a profile exists
        '''
        for profile in cls.profile:
            if profile.account == account:
                return True

        return False