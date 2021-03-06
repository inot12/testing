#! /home/toni/.pyenv/shims/python3
"""
Created on May 8, 2020

@author:toni
"""

import unittest

import roman1


class KnownValues(unittest.TestCase):
    """Test for known values."""
    known_values = ((1, 'I'),
                    (2, 'II'),
                    (3, 'III'),
                    (4, 'IV'),
                    (5, 'V'),
                    (6, 'VI'),
                    (7, 'VII'),
                    (8, 'VIII'),
                    (9, 'IX'),
                    (10, 'X'),
                    (50, 'L'),
                    (100, 'C'),
                    (500, 'D'),
                    (1000, 'M'),
                    (31, 'XXXI'),
                    (148, 'CXLVIII'),
                    (294, 'CCXCIV'),
                    (312, 'CCCXII'),
                    (421, 'CDXXI'),
                    (528, 'DXXVIII'),
                    (621, 'DCXXI'),
                    (782, 'DCCLXXXII'),
                    (870, 'DCCCLXX'),
                    (941, 'CMXLI'),
                    (1043, 'MXLIII'),
                    (1110, 'MCX'),
                    (1226, 'MCCXXVI'),
                    (1301, 'MCCCI'),
                    (1485, 'MCDLXXXV'),
                    (1509, 'MDIX'),
                    (1607, 'MDCVII'),
                    (1754, 'MDCCLIV'),
                    (1832, 'MDCCCXXXII'),
                    (1993, 'MCMXCIII'),
                    (2074, 'MMLXXIV'),
                    (2152, 'MMCLII'),
                    (2212, 'MMCCXII'),
                    (2343, 'MMCCCXLIII'),
                    (2499, 'MMCDXCIX'),
                    (2574, 'MMDLXXIV'),
                    (2646, 'MMDCXLVI'),
                    (2723, 'MMDCCXXIII'),
                    (2892, 'MMDCCCXCII'),
                    (2975, 'MMCMLXXV'),
                    (3051, 'MMMLI'),
                    (3185, 'MMMCLXXXV'),
                    (3250, 'MMMCCL'),
                    (3313, 'MMMCCCXIII'),
                    (3408, 'MMMCDVIII'),
                    (3501, 'MMMDI'),
                    (3610, 'MMMDCX'),
                    (3743, 'MMMDCCXLIII'),
                    (3844, 'MMMDCCCXLIV'),
                    (3888, 'MMMDCCCLXXXVIII'),
                    (3940, 'MMMCMXL'),
                    (3999, 'MMMCMXCIX'))

    def test_to_roman_known_values(self):
        """to_roman should give identical result to numeral with known input"""
        # Halt right there, criminal scum... The docstring is
        # longer than 72 columns... Or is it now?
        # Since it's indented, do I ignore the first 8 spaces??
        for integer, numeral in self.known_values:
            result = roman1.to_roman(integer)
            self.assertEqual(numeral, result)

    def test_from_roman_known_values(self):
        '''from_roman should give known result with known input'''
        for integer, numeral in self.known_values:
            result = roman1.from_roman(numeral)
            self.assertEqual(integer, result)


class ToRomanBadInput(unittest.TestCase):
    """Test for bad inputs."""

    def test_too_large(self):
        """to_roman should fail with large input"""
        self.assertRaises(roman1.OutOfRangeError, roman1.to_roman, 4000)

    def test_zero(self):
        """to_roman should fail if the input is 0"""
        self.assertRaises(roman1.OutOfRangeError, roman1.to_roman, 0)

    def test_negative(self):
        """to_roman should fail if the input is negative"""
        self.assertRaises(roman1.OutOfRangeError, roman1.to_roman, -1)

    def test_non_integer(self):
        """to_roman should fail if the input is non-integer"""
        self.assertRaises(roman1.NotIntegerError, roman1.to_roman, 0.5)
        # it is enough just to test for one specific case, don't overthink it


class RoundTripCheck(unittest.TestCase):
    """test from_roman"""

    def test_roundtrip(self):
        """from_roman(to_roman(n))==n for all n"""
        for integer in range(1, 4000):
            numeral = roman1.to_roman(integer)
            result = roman1.from_roman(numeral)
            self.assertEqual(integer, result)


# this is a little more tricky because there are a lot of invariants
class FromRomanBadInput(unittest.TestCase):
    '''Test for bad input to from_roman.'''

    def test_too_many_repeated_numerals(self):
        """from_roman should fail with too many repeated numerals"""
        for s in ('MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
            self.assertRaises(roman1.InvalidRomanNumeralError,
                              roman1.from_roman, s)

    def test_repeated_pairs(self):
        """from_roman should fail with repeated pairs of numerals."""
        for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
            self.assertRaises(roman1.InvalidRomanNumeralError,
                              roman1.from_roman, s)

    def test_malformed_antecedents(self):
        '''from_roman should fail with malformed antecedents'''
        for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
                  'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(roman1.InvalidRomanNumeralError,
                              roman1.from_roman, s)

    # this was added after we figure out there's a bug
    def testBlank(self):
        '''from_roman should fail with blank string'''
        self.assertRaises(roman1.InvalidRomanNumeralError,
                          roman1.from_roman, '')

    def test_non_string(self):
        """to_roman should fail if the input is non-string"""
        self.assertRaises(roman1.NotStringError, roman1.from_roman, 1)


def main():
    unittest.main(verbosity=2)  # change verbosity to 2 for more verbose output


if __name__ == "__main__":
    main()
