# unittesting framwork

import unittest
class Test(unittest.TestCase):
    def test_firstTest(self):
        print("First unit testcase")

# won't run without this.
if __name__=="__main__":
    unittest.main()