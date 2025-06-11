from unittest import TestCase
from class_playground.student import student


class Teststudent(TestCase):
    def test_getfull_name(self):
        obj = student('abc', 'def', 100)
        self.assertEqual(obj.getfullName(), 'abc def')


class Teststudent1(TestCase):
    def test_lname(self):
        self.fail()


class Teststudent2(TestCase):
    def test_fname(self):
        self.fail()
