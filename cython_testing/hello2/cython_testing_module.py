'''
Created on Jun 3, 2020

@author: toni
'''

import sys

from fruitful_functions import execution_time
from hello import say_hello_to

sys.path.insert(
    0, "/home/toni/eclipse-workspace/useful_scripts/important_functions/")

execution_time(say_hello_to, "Taki")
