import unittest  # importing the unit test
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
        self.new_user = User("Ibrahim", "Hassib", "ihassib@gmail.com", "McGee")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name, "Ibrahim")
        self.assertEqual(self.new_user.last_name, "Hassib")
        self.assertEqual(self.new_user.email, "ihassib@gmail.com")
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

    def setUp(self):
        '''
        Set up method to run before each test cases.  
        '''
        self.new_account = Credential("Twitter", "Hiasco", "McGee")

    def test_init_(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.site_name, 'Twitter')
        self.assertEqual(self.new_account.account_name, 'Hiasco')
        self.assertEqual(self.new_account.password, 'McGee')
   
    def test_save_credentials(self):
        '''
        test_save_credentials to see if the new account information is saved into the appropriate list
        '''
        self.new_account.save_credentials()
        self.facebook = Credential('Facebook', 'Loso', 'psd001')
        self.facebook.save_credentials()
        self.assertEqual(len(Credential.credential_list), 2)

    def tearDown(self):
        '''
        Function to clear the credentials list after each test
        '''
        Credential.credential_list = []      

    def test_display_credentials(self):
        '''
        test_display_credentials to see if the new information can be displayed
        '''
        self.new_credential.save_credentials()
        self.facebook = Credential('Facebook','Loso','psd001')
        self.facebook.save_credentials()

        self.assertListEqual(Credential.display_credentials(),Credential.credential_list)

    def test_find_by_site_name(self):
        '''
        test to find account info
        '''
        self.new_credential.save_credentials()
        facebook = Credential('Facebook','Loso','psd001')
        facebook.save_credentials()
        credential_exists = Credential.find_by_site_name('Twitter')

        self.assertEqual(credential_exists,facebook)


    def test_copy_credential(self):
        '''
        Test to check if the copy a credential method copies the correct account info
        '''
        self.new_account.save_credentials()
        Credential.copy_credential(self.new_account.site_name)
        self.assertEqual(str(f"Site Name: {self.new_credential.site_name} - UserName: {self.new_credential.site_name} - Password: {self.new_credential.password}"),pyperclip.paste())

if __name__ == '__main__':
    unittest.main(verbosity=2)
