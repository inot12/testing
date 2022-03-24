#! /home/toni/.pyenv/shims/python3
"""
Created on May 1, 2020

@author:toni
"""

from name_function import get_formatted_name


def display_name():
    """
    Displays a neatly formatted full name.
    """
    print("Enter 'q' any time to quit.")
    while True:
        first = input("\nPlease give me a first name: ")
        if first == 'q':
            break
        last = input("\nPlease give me a last name: ")
        if last == 'q':
            break

        formatted_name = get_formatted_name(first, last)
        print(f"\tNeatly formatted name: {formatted_name}.")


def main():
    display_name()


if __name__ == "__main__":
    main()
