class user:
    """
    Class that allows user to create a login password.
    """
    login_name= ''
    login_password=''

    def __init__(self, login_name, login_password):
        '''
        method that defines variables to be used
        '''

        self.login_name = login_name
        self.login_password= login_password

    