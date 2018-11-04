import pyperclip



class User:
    """
    Class that generates new instances of user
    """
    user_list=[]

    def __init__(self, first_name, last_name, email, password):
        '''
        __init__ method that define properties held in our objects.
        '''

        self.first_name= first_name
        self.last_name= last_name
        self.email= email
        self.password= password

    def save_user(self):
        '''
        function to save new created instance of users
        '''
        User.user_list.append(self)

class Credential:
    '''
    Class that creates instances of user credentials 
    '''
    credential_list = []

    def __init__(self, site_name, account_name, password):
        '''
        __init__ method that define properties held in this object
        '''
        self.site_name = site_name
        self.account_name = account_name
        self.password = password
        
  