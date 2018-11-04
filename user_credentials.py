import pyperclip
import string
import random


class User:
    """
    Class that generates new instances of user
    """
    user_list = []

    def __init__(self, first_name, last_name, email, password):
        '''
        __init__ method that define properties held in our objects.
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
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

    def __init__(self, site_name, account_name, password):
        '''
        __init__ method that define properties held in this object
        '''
        self.site_name = site_name
        self.account_name = account_name
        self.password = password

    def save_credentials(self):
            '''
	        Function to save a newly created user instance
	        '''
            Credential.credential_list.append(self)

    def generate_password(self, size =8,char=string.ascii_uppercase+ ascii_lowercase + string.digits): 
        '''
        Function to generate a password
        '''  
        gen_pass=''.join(random.choice(char) for _ in range(size))
        self.password = gen_pass
        return self.password

    @classmethod
    def display_credentials(cls):
        '''
        class method to display the list of credentials saved
        '''
        return cls.credential_list

    @classmethod
    def find_by_site_name(cls, site_name):
        '''
        Method to input site name and output matching information from site name
        '''
        for credential in cls.credential_list:
            if credential.site_name == site_name:
                return Credential

    @classmethod
    def copy_credential(cls,site_name):
        '''
        Class method that copies account info adjacent to site entered 
        '''
        find_credential = cls.find_by_site_name(site_name)
        pyperclip.copy(f'Site Name: {find_credential.site_name} - UserName: {find_credential.site_name} - Password: {find_credential.password}')

    