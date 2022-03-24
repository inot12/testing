#! /home/toni/.pyenv/shims/python3
"""
Created on Jul 22, 2020

@author:toni

A comparison of run times of python code and cythonized code.
"""

# It is not clear why the following erros show up:
# PyLint: Unable to import 'cythonized_code'
# PyLint: Unable to import 'python_code'
# Unresolved import: slow_func
# Unresolved import: slower_func
# The errors above seem to be false positives.
from cythonized_code import slow_func
from python_code import slower_func


def main():
    slower_func()
    slow_func()


if __name__ == "__main__":
    main()
