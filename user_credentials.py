class User_credentials:
    user_credentials = []
    '''
    this class creates  new instance of user data
    '''
    def __init__(self, username, password, account_type):
        '''
        init method to define objects
        Args: 
            username: to ask user a username
            password: to either generate or ask user for a password
            account_type: type of account like twitter, facebook
        '''
        self.username = username
        self.password = password
        self.account_type = account_type