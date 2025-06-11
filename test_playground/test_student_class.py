import unittest
from class_playground.student import student

class test_student_cls(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.std1 = student('john','wark',300)  # this is a class level object. excercise caution in not using instance level access to make changes
        cls.std2 = student('mark','walters',400) # this is a class level object. excercise caution in not using instance level access to make changes

    @classmethod
    def tearDownClass(cls):
        pass

    def test_fname(self):
        self.assertEqual(self.std1.fname,'john','testcase to set fname failed') # okay since the class level instantiated std1 is available. as long as we dont do any changes, this is fine and there is no promotion to instance level
        self.assertEqual(self.std2.fname,'mark','testcase to set fname failed') # okay since the class level instantiated std1 is available. as long as we dont do any changes, this is fine and there is no promotion to instance level


if __name__ == '__main__':
    #suite = unittest.TestSuite([test_student_cls()]) #used when the class has a runTest method that has the TC. rarely used
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_student_cls)
    #suite = unittest.makeSuite(test_student_cls,'test') #deprecated in favor of the above way of invoking
    unittest.TextTestRunner.run(suite)
