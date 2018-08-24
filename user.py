
class User:
    user = []
    '''
    this class creates  new instance of user data
    '''
    def __init__(self, first_name, last_name, username, password):
        '''
        init method to define objects
        Args: 
            username: to ask user a username
            password: to either generate or ask user for a password
        '''
        self.first_name =first_name
        self.last_name = last_name
        self.username = username
        self.password = password
    
    def new_user(self):
        User.user.append(self)

    def save_user(self):
        User.user.append(self)

    