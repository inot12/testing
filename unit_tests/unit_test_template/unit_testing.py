#! /home/toni/.pyenv/shims/python3
"""
Created on May 1, 2020

@author:toni
"""

import unittest

# from module import class_  # import the class you are about to test
# from module import function  # import the function you are about to test


class Test_ClassName_FunctionName(unittest.TestCase):
    """Tests for the class ClassName or function FunctionName."""

    def setUp(self):
        """Create an instance of the class for use in all test methods.
        Only used for classes. Not required for testing functions."""
        # self.c = Class()  # instance initialization comes here

    def test_case1(self):  # test method names begin with 'test'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)

    def test_case2(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)


def main():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()
