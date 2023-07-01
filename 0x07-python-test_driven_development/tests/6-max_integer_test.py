#!/usr/bin/python3
""" Unittest for max_integer([..]) """


max_integer = __import__("6-max_integer").max_integer
import unittest

class TestMaxInteger(unittest.TestCase):
    """ Test max_integer function """

    def testEmptyList(self):
        # Test emty list
        self.assertEqual(max_integer(), None)

    def testOrderedList(self):
        # Test ordered list
        self.assertEqual(max_integer([0, 1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 1, 2, 3, 0]), 4)

    def tesUnorderedList(self):
        # Test unordered list
        self.assertEqual(max_integer([2, 1, 4, 0, 3]), 4)

    def testListWithNegativeNumbers(self):
        # Test list with negative numbers:
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([0, -1, -2, -3, -4]), 0)
        self.assertEqual(max_integer([-1, -3, -2, -4, 0]), 0)
        self.assertEqual(max_integer([-1, 4, -3, 2]), 4)

    def testListWithFloats(self):
        # Test list with floats
        self.assertEqual(max_integer([2.3, 5.4, 6.0, -7, -100.5]), 6.0)
        self.assertEqual(max_integer([2.3, 5.4, 6.0, 7.25, 100.55]), 100.55)
        self.assertEqual(max_integer([100.55, 100.56, 7.5, 6.5]), 100.56)
        self.assertEqual(max_integer([-2.3, -5.4, -6.0, -7, -100.5]), -2.3)

    def testListWithOneNumber(self):
        # Test list with on number
        self.assertEqual(max_integer([10]), 10)

    def testString(self):
        # Test a string
        self.assertEqual(max_integer("abcdef"), "f")
        self.assertEqual(max_integer("fedcba"), "f")
        self.assertEqual(max_integer("aA"), "a")
        self.assertEqual(max_integer("a"), "a")

    def testEmptyString(self):
        # Test empty string
        self.assertEqual(max_integer(""), None)
        self.assertEqual(max_integer([""]), "")
