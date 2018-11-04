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
