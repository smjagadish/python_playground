import sys
import unittest
from math import factorial

from excercises import basic_class
class myFirstTest(unittest.TestCase):

    def testEquality(self):
        lst = list()
        self.assertIsNotNone(lst,"test failed ! list is None")

    #@unittest.skip('temporary pause on this test only') - unconditional skip
    @unittest.skipIf(sys.version_info[0]<=3,
                     'this test will not run with python version 3 and above')
    def testEqualityFailure(self):
        llst = None
        self.assertIsNotNone(llst, "test fail ! list is  None")


    def testFactorial(self):
        num = 4
        self.assertEqual(factorial(num),24,'test failed ! factorial function does not work')

    def testBasicClass(self):
        obj = basic_class.basic()
        self.assertIsInstance(obj,basic_class.basic,'test failed ! instance type is incorrect')
        self.assertNotEqual(obj.basic_var,78,'test failed ! the class variable has unexpected value')



if __name__ == '__main__':
    unittest.main()