#! /usr/bin/env python3
import pyperclip
from user_credentials import User , Credential

def create_user(fname,lname,email,password):
    '''
    Function to create a new user 
    '''
    new_user = User(fname,lname,email,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    User.save_user(user) 

def generate_password():
    '''
	Function to generate a password automatically
	'''
    User.generate_password()


def main():
        print('Hello! Welcome to password locker.')
        while True:
            print ('Use these codes to navigate: ca-Create an Account, li-Log In, ex-Exit')
            print("-"*60)
            short_code = input('Enter a choice: ').lower().strip()
            if short_code == 'ex':
                print('Goodbye')
                break

            elif short_code == 'ca':
                print('To create a new account')
                print("-"*60)
                first_name = input('Enter your first name: ')
                last_name = input('Enter your last name: ')
                password = input('Enter your password: ')
                save_user(create_user(first_name,last_name,password))
                print("-"*60)
                print(f'New Account Created for: {first_name} {last_name} using password: {password}')
                print("-"*60)

if __name__ == '__main__':
    main()

			
		
	
		
		
		
		
