#! /home/toni/.pyenv/shims/python3
"""
Created on May 8, 2020

@author:toni
"""

# import re

# notice that this iterable is a tuple, because we expect that it won't change
roman_numeral_map = (('M', 1000),
                     ('CM', 900),
                     ('D', 500),
                     ('CD', 400),
                     ('C', 100),
                     ('XC', 90),
                     ('L', 50),
                     ('XL', 40),
                     ('X', 10),
                     ('IX', 9),
                     ('V', 5),
                     ('IV', 4),
                     ('I', 1))

# =============================================================================
# roman_numeral_pattern = re.compile('''
#     ^                   # beginning of string
#     M{0,3}              # thousands - 0 to 3 Ms
#     (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
#                         # or 500-800 (D, followed by 0 to 3 Cs)
#     (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
#                         # or 50-80 (L, followed by 0 to 3 Xs)
#     (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
#                         # or 5-8 (V, followed by 0 to 3 Is)
#     $                   # end of string
#     ''', re.VERBOSE)

# def to_roman(n):
#     """
#     convet integer to a Roman numeral
#     """
#     #==========================================================================
#     # if n > 3999:
#     #     raise OutOfRangeError('number out of range (must be less than 4000)')
#     # if n == 0:
#     #     raise OutOfRangeError('number out of range (cannot be 0)')
#     # if n < 0:
#     #     raise OutOfRangeError('number out of range (cannot be negative)')
#     #==========================================================================
#     if not (0 < n < 4000):
#         raise OutOfRangeError('number out of range (must be 1..3999)')
#
#     if not isinstance(n, int):
#         raise NotIntegerError('number not an integer')
#
#     result = ''
#     for numeral, integer in roman_numeral_map:
#         while n >= integer:
#             result += numeral
#             n -= integer
#     return result

# def from_roman(s):
#     """Convert roman numeral to integer."""
#     if not s:
#         raise InvalidRomanNumeralError('Input can not be blank')
#     # above statement added to fix the bug
#     if not isinstance(s, str):
#         raise NotStringError('input not a string')
#     # above statement added to check if input is string
#     if not roman_numeral_pattern.search(s):
#         raise InvalidRomanNumeralError('Invalid Roman numeral: {0}'.format(s))
#     result = 0
#     index = 0
#     for numeral, integer in roman_numeral_map:
#         while s[index:index+len(numeral)] == numeral:
#             result += integer
#             index += len(numeral)
#     return result
# =============================================================================


# two examples how to define exceptions which will be used for unit testing
class OutOfRangeError(ValueError):
    pass


class NotIntegerError(ValueError): pass


class InvalidRomanNumeralError(ValueError): pass


class NotStringError(ValueError): pass


# with this new refactored code,
# the execution time of test_roman 1 is roughly 5 times lower
# unit test went from 0.025 to 0.005 s
# in this case, lookup tables are faster then regular expressions
# and generally, try to avoid regular expressions whenever you can, it's messy
to_roman_table = [None]
from_roman_table = {}


def to_roman(n):
    '''convert integer to Roman numeral'''
    if not 0 < n < 4000:
        raise OutOfRangeError('number out of range (must be 1..3999)')
    if int(n) != n:
        raise NotIntegerError('non-integers can not be converted')
    return to_roman_table[n]


def from_roman(s):
    '''convert Roman numeral to integer'''
    if not isinstance(s, str):
        raise NotStringError('Input must be a string')
    if not s:
        raise InvalidRomanNumeralError('Input cannot be blank')
    if s not in from_roman_table:
        raise InvalidRomanNumeralError('Invalid Roman numeral: {s}')
    return from_roman_table[s]


def build_lookup_tables():

    def to_roman(n):
        result = ''
        for numeral, integer in roman_numeral_map:
            if n >= integer:
                result = numeral
                n -= integer
                break
        if n > 0:
            result += to_roman_table[n]
        return result

    for integer in range(1, 4000):
        roman_numeral = to_roman(integer)
        to_roman_table.append(roman_numeral)
        from_roman_table[roman_numeral] = integer


build_lookup_tables()


def main():

    print(to_roman(5))
    print(to_roman(643))
    b = 2
    c = NotIntegerError()
    print(isinstance(b, NotIntegerError))
    print(isinstance(c, NotIntegerError))

    print(to_roman(0))
    print(to_roman(-4))


if __name__ == "__main__":
    main()
