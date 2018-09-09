class User:
    user = []
    '''
    this class creates  new instance of user data
    '''
    def __init__(self, username, password):
        '''
        init method to define objects
        Args: 
            username: to ask user a username
            password: to either generate or ask user for a password
        '''
        self.username = username
        self.password = password
        
    
    def new_user(self):
        '''
           Method that appends a user
        '''
        User.user.append(self)

    def save_user(self):
        '''
           Method that saves a new user
        '''
        User.user.append(self)

    def delete_user(self):
        '''
           Method that deletes a user
        '''
        User.user.remove(self)