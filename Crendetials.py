class Credentials:
    """
    Class that generates new instances of credentials.
    """

    accounts_list = [] # Empty credential list
    # Init method up here
    def save_credantial(self):

        '''
        save_credential method saves account objects into accounts_list
        '''

        Credentials.accounts_list.append(self)

    def __init__(self, acc_name, user_name, password):

      # docstring removed for simplicity

        self.acc_name = acc_name
        self.user_name = user_name
        self.password = password
