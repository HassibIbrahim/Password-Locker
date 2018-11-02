import unittest #importing the unit test
import pyperclip
from user_credentials import User 


class TestUserCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

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


if __name__ == '__main__':
    unittest.main()