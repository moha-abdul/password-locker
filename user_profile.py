class User_profile:
    user_info = []
    '''
    this class collects user data
    '''
    def __init__(self, first_name, last_name, phone_number, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.age = age
        self.gender = gender