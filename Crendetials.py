class Credentials:
    """
    Class that generates new instances of credentials.
    """

    accounts_list = [] # Empty accounts list
    # Init method up here

    def __init__(self, acc_name, user_name, password):

      # docstring removed for simplicity

        self.acc_name = acc_name
        self.user_name = user_name
        self.password = password

    @classmethod
    def display_accounts(cls):
        '''
        method that returns the accounts_list
        '''
        return cls.accounts_list

    @classmethod
    def save_credential(self):

        '''
        save_credential method saves account objects into accounts_list
        '''

        Credentials.accounts_list.append(self)

    @classmethod
    def delete_account(self):
        '''
        delete account method deletes a saved account from the account list
        '''
        Credentials.accounts_list.remove(self)
