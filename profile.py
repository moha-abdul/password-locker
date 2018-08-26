import pyperclip

class Profile:
    profile = []
    '''
    this class creates  new instance of user data
    '''
    def __init__(self, account, password):
        self.account = account
        self.password = password

    def new_profile(self):
        Profile.profile.append(self)

    def save_profile(self):
        Profile.profile.append(self)

    # def save_profile(self):
    def delete_profile(self):
        Profile.profile.remove(self)

    @classmethod
    def find_profile_by_account(cls, account):
        for profile in cls.profile:
            if profile.account == account:
                return profile