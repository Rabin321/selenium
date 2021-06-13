import unittest
# we can import selenium if we want to deal with some websites.


def setUpModule():  # will be executed before executing all the class or any methods present in the test class.
    print("SetUpModule")

def tearDownModule():    # will be execute after executing all the calss or any methods present in the test class.
    print("TearDownModule")

class AppTesting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Opening Application")  # setUpClass will execute only one time before executing all the test methods.

    @classmethod      #decorator
    def setUp(self):
        print("Login")       # Setup up method will execute each time before executing  all the test methods..
    @classmethod
    def tearDown(self):
        print("Logout")      #  tearDown method will execute each time after executing  all the test methods..







    def test_search(self):
        print("Search")

    def test_advancedsearch(self):
        print("Advanced Search")

    def test_recharge(self):
        print("Rechharge")

    def test_plan(self):
        print("Plan")

    @classmethod
    def tearDownClass(cls):  # tearDownCass  wil execute only one time after executing all the test methods.
        print("Close Application")


if __name__ == '__main__':
    unittest.main()
