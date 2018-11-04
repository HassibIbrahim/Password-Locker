import pyperclip
import string
import random

global users_list
class User:
    """
    Class that generates new instances of user
    """
    user_list = []

    def __init__(self, first_name, last_name, password):
        '''
        __init__ method that define properties held in our objects.
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.password = password

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
    user_credentials_list = []


    @classmethod
    def check_user(cls,first_name,password):
        '''
        Method to confirm matching data in user_list
        '''
        current_user = ''
        for user in User.user_list:
            if (user.first_name == first_name and user.password == password):
                current_user = user.first_name
                return current_user
              


    def __init__(self,user_name, site_name, account_name, password):
        '''
        __init__ method that define properties held in this object
        '''
        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password

    def save_credentials(self):
            '''
	        Function to save a new user instance
	        '''
            Credential.credential_list.append(self)

    def generate_password(self,size =8,char=string.ascii_uppercase+ string.ascii_lowercase + string.digits): 
        '''
        Function to generate a password
        '''  
        gen_pass=''.join(random.choice(char) for _ in range(size))
        return gen_pass

    @classmethod
    def display_credentials(cls,user_name):
        '''
        class method to display the list of credentials saved
        '''
        user_credentials_list = []
        for credential in cls.credential_list:
            if credential.user_name == user_name:
                user_credentials_list.append(credential)
        return user_credentials_list

    @classmethod
    def find_by_site_name(cls, site_name):
        '''
        Method to input site name and output matching information from site name
        '''
        for credential in cls.credential_list:
            if credential.site_name == site_name:
                return credential

    @classmethod
    def copy_credential(cls,site_name):
        '''
        Class method that copies account info adjacent to site entered 
        '''
        find_credential = Credential.find_by_site_name(site_name)
        return pyperclip.copy(find_credential.password)
    