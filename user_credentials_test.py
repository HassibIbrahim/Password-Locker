import unittest #importing the unit test
import pyperclip
from user_credentials import User, Credential 


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
        self.new_user= User("Ibrahim","Hassib","ihassib@gmail.com","McGee")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Ibrahim")
        self.assertEqual(self.new_user.last_name,"Hassib")
        self.assertEqual(self.new_user.email,"ihassib@gmail.com")
        self.assertEqual(self.new_user.password,"McGee")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user list
        '''

        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

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
        self.new_account = Credential("Twitter","Hiasco","McGee")




if __name__ == '__main__':
    unittest.main(verbosity=2)