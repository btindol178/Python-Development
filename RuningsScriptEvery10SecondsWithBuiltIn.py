# Searching for methods of string
import builtins
from os import name


dir(str) # put this in command not terminal
dir(__builtins__)

import os

import time

# This prints an infaniate loop that prints every 10 secons
while True: 
    with open("vegetables.txt") as file:
        print(file.read())
        time.sleep(10) # every 10 seconds this runs
    

