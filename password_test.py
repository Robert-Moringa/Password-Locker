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

if __name__ == '__main__':
    unittest.main()