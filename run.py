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


def main():
    print("Hello Welcome to your password locker site. What is your name?")
    name = input()

    print(f"Hello {name}. what would you like to do?")
    print('\n')

while True:
        print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

        short_code:any = input().lower()

        if short_code == "cc":
            print("New Account")
            print("-"*10)

            print ("Account name ...")
            acc_name = input()

            print("Username ...")
            user_name = input()

            print("Password ...")
            password = input()

            save_credantial(create_account(acc_name, user_name, password)) # create and save new account.
            print('\n')
            print(f"New {acc_name} Account Created")
            print('\n')

if __name__ == '__main__':

    main()