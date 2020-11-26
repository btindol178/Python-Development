# in terminal pip install mysql-connector
#pip install --upgrade pip
#pip install mysqlclient

# in beggining run line 5 and 6 first
#from pip._internal import main
#main(['install','mysql-connector-python-rf'])
import mysql.connector

# TO VIEW THE TABLES
mydb2 = mysql.connector.connect(host="localhost", user="root", passwd="very_strong_password",database = "megacourse", auth_plugin='mysql_native_password')

mycursor =mydb2.cursor()

words = input("Enter a word: ")
# top one shows top 3
mycursor.execute("SELECT * FROM dictionary2 WHERE word = '%s'" % words)
#mycursor.execute("SELECT * FROM dictionary2 WHERE word = 69;") # finds where the word is 69
results = mycursor.fetchall()
#print(results) # not good format

# better output
for i in results:
    print(i[1]) # for each iteration in results give the second part of tuple the definition
else:
    print("No results found")
