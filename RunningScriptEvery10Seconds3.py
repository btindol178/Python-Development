import os
import time
# pip install numpy==1.18.4
#pip install pandas do this with not in python in terminal so do exit() first
# This is same things as running script every 10 seconds
# change vegetable to the file path
#pip install --upgrade pip

import pandas # after installing not in python go to python to import

while True:
    if os.path.exists("temps_today.csv"):
       data = pandas.read.csv("temps_today.csv")
       print(data.mean()["st1"]) # This opens the file and then takes the mean every 10 secons

    else:
        print("File does not exist")
    time.sleep(10)# Print every 24 hours 86400 seconds