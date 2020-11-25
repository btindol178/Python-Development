import os
import time

# This is same things as running script every 10 seconds
while True:
    if os.path.exists("vegetables.txt"):
        with open("vegetables.txt") as file:
            print(file.read())
    else:
        print("File does not exist")
    time.sleep(10)