import pyperclip

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

    def delete_user(self):
        User.user.remove(self)

    @classmethod
    def find_user_by_username(cls, username):
        for user in cls.user:
            if user.username == username:
                return user

    @classmethod
    def user_exists(cls, username):
        for user in cls.user:
            if user.username == username:
                return True

        return False

    @classmethod
    def display_users(cls):
        return cls.user

    # @classmethod
    # def copy_password(cls, password):
    #     password_found = User.copy_password(password)
    #     pyperclip.copy(password_found.password)