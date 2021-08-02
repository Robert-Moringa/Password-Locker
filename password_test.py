# from _typeshed import Self
import unittest
from Crendetials import Credentials # Importing the Credentials class

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the Credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Credentials("Twitter","@Robert_Maina20","0701316729") # create credantials object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.acc_name, "Twitter")
        self.assertEqual(self.new_account.user_name, "@Robert_Maina20")
        self.assertEqual(self.new_account.password, "0701316729")


    def test_display_all_accounts(self):
        '''
        method that returns a list of all accounts saved
        '''

        self.assertEqual(Credentials.display_accounts(), Credentials.accounts_list)


    def test_save_all_accounts(self):
        '''
        method that saves a new account
        '''
        self.new_account.save_credential()
        test_account = Credentials("Twitter","@Robert_Maina20","0701316729") #new account
        test_account.save_credential()
        self.assertEqual(len(Credentials.accounts_list), 3)


    def test_delete_account(self):
        '''
        test_delete_account to test if we can remove an account from our our account list
        '''
        self.new_account.save_credential()
        test_account = Credentials("Twitter","@Robert_Maina20","0701316729")
        test_account.save_credential()

        self.new_account.delete_account()
        self.assertEqual(len(Credentials.accounts_list), 1)


if __name__ == '__main__':
    unittest.main()