'''
Created on Jun 3, 2020

@author: toni
'''

import sys

from fruitful_functions import duration

sys.path.insert(
    0, "/home/toni/eclipse-workspace/useful_scripts/important_functions/")


def say_hello_to(name):
    print(f"Hello {name}!")


print(duration(say_hello_to("Taki")))
