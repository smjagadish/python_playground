import unittest
from class_playground.student import student
class testStudent(unittest.TestCase):

    def setUp(self): # test level fixture . done for each tc
        self.std1 = student('john','wark',200)
        self.std2 = student('mark','walters',400)

    def tearDown(self): # test level fixture . done for each tc
        pass

    @classmethod
    def setUpClass(cls): #class level fixture . done once for the class
        print('class fixture for setup invoked')

    @classmethod
    def tearDownClass(cls): #class level fixture. done once for the class
        print('class fixture for teardown invoked')

    def test_fname(self):
        self.assertEqual(self.std1.fname,'john','test to set fname failed')
        self.assertEqual(self.std2.fname,'mark','test to set fname failed')

    def test_fullname(self):
        self.assertEqual(self.std1.getfullName(),'john wark','test to set fullname failed')
        self.assertEqual(self.std2.getfullName(),'mark walters','test to set fullname failed')


if __name__ == '__main__':
    unittest.main()