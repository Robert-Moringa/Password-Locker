#!/usr/bin/env python3.8
from Crendetials import Credentials
from User import user

def create_account(acc_name, user_name, password):
    '''
    Function to creates new account
    '''
    new_account= Credentials(acc_name, user_name, password)
    return new_account

def save_credential (Credentials):
    '''
    Function to delete a credentials
    '''
    Credentials.save_credential()

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Credentials.display_accounts()


def del_account(Credentials):
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
        print("Hello. Welcome back to Password Locker!")
        print('\n')
        print('Let us create a login username and a password')
        print('\n')
        print('Enter username')
        login_username =  input()
        print('Enter password')
        login_password = input()

        print('To login in, Enter your username')
        input_username = input()
        if (input_username == login_username):
            print('Enter your password')
            input_password = input()
            if (input_password == login_password):
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

                        print('Enter the name of an account you wish to delete.')
                        del_name= input()
                        if (del_name == display_accounts()):
                            del_name.delete_account()

                        else:
                            Print('If you entered an account name, it seems you mis spelt it. KIndly input a new name of an account to delete.')

                    else:
                        print('\n')
                        print("You dont seem to have any accounts saved yet")
                        print('\n')
            else:
                print('Wrong Password')

        else:
            print('Wrong Username')


if __name__ == '__main__':

    main()