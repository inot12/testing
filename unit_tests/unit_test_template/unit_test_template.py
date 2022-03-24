#! /home/inot/.pyenv/shims/python3
"""
Created on Nov 2, 2020

@author: inot
"""

import unittest

import mdl

# from module import class  # import the class you are about to test
# from module import function  # import the function you are about to test


class ClassNameFunctionNameGoodInput(unittest.TestCase):
    """Test for good input of class ClassName or function FunctionName."""

    def setUp(self):
        """Create an instance of the class for use in all test methods.

        Only used for classes. Not required for testing functions.
        The setUp method runs BEFORE EVERY SINGLE TEST.
        Example:
        self.instance_name = Class(*args)
        """
        # instance initialization comes here
        # self.instance_name = Class(*args)

    def tearDown(self):
        """Destroy all instances of tested files for a clean state.

        tearDown method runs AFTER EVERY SINGLE TEST.
        """
        # pass

    @classmethod  # we work with the class and not the instance of the class
    def setUpClass(cls):
        """RUNS BEFORE ANYTHING IN THE TEST.

        Use for costly operations that you want to do only once.
        This does not run before every single test individually,
        but before all tests, and it does it only once.
        """
        # pass

    @classmethod
    def tearDownClass(cls):
        """RUNS AFTER ANYTHING IN THE TEST."""
        # pass

    def test_case1(self):
        """f should return known results for known values."""
        self.assertEqual(f(known_value), known_result)

    # def test_case2(self):
    #     """f should return known results for known values."""
    #     self.assertAlmostEqual(f(known_value), known_result, delta=1e-5)


class ClassNameFunctionNameBadInput(unittest.TestCase):
    """Test for bad input of class ClassName or function FunctionName."""

    def setUp(self):
        """Create an instance of the class for use in all test methods.

        Only used for classes. Not required for testing functions.
        The setUp method runs BEFORE EVERY SINGLE TEST.
        Example:
        self.instance_name = Class(*args)
        """
        # instance initialization comes here
        # self.instance_name = Class(*args)

    def tearDown(self):
        """Destroy all instances of tested files for a clean state.

        tearDown method runs AFTER EVERY SINGLE TEST.
        """
        # pass

    # def test_case1(self):
    #     """f should fail if condition.
    #
    #     We test excetpions by assertRaises. assertRaises takes 3 arguments:
    #     1. The error that should be raised.
    #     2. The function or method that should raise it.
    #     3. All the arguments of mdl.f that result in the exception.
    #
    #     Example:
    #     We test divide(a,b) which divides two numbers for zero division error
    #     self.assertRaises(ValueError, mdl.divide, 5, 0)
    #     """
    #     self.assertRaises(ErrorType, mdl.f, *args)

    # def test_case2(self):
    #     """Alternative with context manager.
    #
    #     Use if you have more exceptions of the same type.
    #     """
    #     with self.assertRaises(ValueError):
    #         calc.divide(10, 0)
    #         calc.divide(10, '1')


def main():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()
