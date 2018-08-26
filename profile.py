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

    # def save_profile(self):