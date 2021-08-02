#!/usr/bin/env python3.8
from Crendetials import Credentials
from User import user

def create_account(acc_name, user_name, password):
    '''
    Function to creates new account
    '''
    new_account= Credentials(acc_name, user_name, password)
    return new_account

def save_credential (Crendetials):
    '''
    Function to delete a credentials
    '''
    Credentials.save_credential()

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Credentials.display_accounts()


def del_account(Credential):
    '''
    Function to delete an account
    '''
    Credentials.delete_account()

def main():
    print("Hello Welcome to your password locker site. What is your name?")
    name = input()

    print(f"Hello {name}. what would you like to do?")
    print('\n')

while True:
        print("Hello. Welcome back to your")



        print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, ex -exit the account list ")

        short_code:any = input().lower()

        if short_code == "ca":
            print("New Account")
            print("-"*10)

            print ("Account name ...")
            acc_name = input()

            print("Username ...")
            user_name = input()

            print("Password ...")
            password = input()

            save_credential(create_account(acc_name, user_name, password)) # create and save new account.
            print('\n')
            print(f"New {acc_name} Account Created")
            print('\n')

        if short_code == "da":

            if display_accounts:
                print("Here is a list of all your accounts")
                print('\n')

                for account in display_accounts():
                    print(f"{account.acc_name} {account.user_name} .....{account.password}")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have any contacts saved yet")
                print('\n')


if __name__ == '__main__':

    main()