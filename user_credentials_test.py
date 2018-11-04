import unittest  
import pyperclip
from user_credentials import User
from user_credentials import Credential



class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase :TestCase class that helps in creating test cases 
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.  
        '''
        self.new_user = User("Ibrahim", "Hassib", "McGee")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name, "Ibrahim")
        self.assertEqual(self.new_user.last_name, "Hassib")
        self.assertEqual(self.new_user.password, "McGee")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user list
        '''

        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


class TestCredentials(unittest.TestCase):
    '''
    Test class that identifies test cases for the credentials class behaviours.

    Args:
        unittest.TestCase :TestCase class that helps in creating test cases 
    '''

    def test_check_user(self):
        '''
        Function to test whether the login in function check_user works as expected
        '''
        self.new_user = User('Ibrahim','Hassib','McGee')
        self.new_user.save_user()
        user2 = User('Loso','Wii','psd001')
        user2.save_user()

        for user in User.user_list:
            if user.first_name == user2.first_name and user.password == user2.password:
                current_user = user.first_name
        return current_user

        self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))

    def setUp(self):
        '''
        Set up method to run before each test cases.  
        '''
        self.new_account = Credential("Twitter", "Hiasco","Gwala", "McGee")

    def test_init_(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.site_name, 'Twitter')
        self.assertEqual(self.new_account.account_name, 'twitter')
        self.assertEqual(self.new_account.account_name,'Gwala')
        self.assertEqual(self.new_account.password, 'McGee')
   
    def test_save_credentials(self):
        '''
        test_save_credentials to see if the new account information is saved into the appropriate list
        '''
        self.new_account.save_credentials()
        self.facebook = Credential('Facebook', 'Loso', 'Gwala', 'psd001')
        self.facebook.save_credentials()
        self.assertEqual(len(Credential.credential_list), 2)

    def tearDown(self):
        '''
        Function to clear the credentials list after each test
        '''
        Credential.credential_list = []
        User.user_list = []      

    def test_display_credentials(self):
        '''
        test_display_credentials to see if the new information can be displayed
        '''
        self.new_account.save_credentials()
        facebook = Credential('Facebook','Loso','Gwala','psd001')
        facebook.save_credentials()
        google = Credential('bob','google','nutty','psd047')
        google.save_credentials()
        self.assertListEqual(len(Credential.display_credentials(facebook.user_name)),2)

    def test_find_by_site_name(self):
        '''
        test to find account info
        '''
        self.new_account.save_credentials()
        facebook = Credential('Facebook','Loso','Gwala','psd001')
        facebook.save_credentials()
        credential_exists = Credential.find_by_site_name('Twitter')

        self.assertEqual(credential_exists,facebook)


    def test_copy_credential(self):
        '''
        Test to check if the copy a credential method copies the correct account info
        '''
        self.new_account.save_credentials()
        facebook = Credential('Facebook','Loso','Gwala','psd001') 
        facebook.save_credentials()
        find_credential = None
        for credential in Credential.user_credentials_list:
            find_credential =Credential.find_by_site_name(credential.site_name)
            return pyperclip.copy(find_credential.password)
        Credential.copy_credential(self.new_account.site_name)
        self.assertEqual('McGee',pyperclip.paste())
        print(pyperclip.paste())

if __name__ == '__main__':
    unittest.main(verbosity=2)
