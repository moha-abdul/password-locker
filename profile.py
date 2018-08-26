import pyperclip

class Profile:
    profile = []
    '''
    this class creates  new instance of user data
    '''
    def __init__(self, profile, password):
        self.profile = profile
        self.password = password

    def new_profile(self):
        Profile.profile.append(self)