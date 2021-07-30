#!/usr/bin/env python3.8
from Crendetials import Credentials

def create_account( acc_name, user_name, password):
    '''
    Function to creates new account
    '''
    new_account= Credentials(acc_name, user_name, password)
    return new_account

def save_credantial (contact):
    '''
    Function to delete a contacts
    '''
    Credentials.save_credantial()