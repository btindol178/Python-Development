import os
import time
#pip install pandas do this with not in python in terminal so do exit() first
# This is same things as running script every 10 seconds
# change vegetable to the file path
import pandas
while True:
    if os.path.exists("temps_today.csv"):
        with open("temps_today.csv") as file:
            print(file.read())
    else:
        print("File does not exist")
    time.sleep(10)# Print every 24 hours 86400 seconds