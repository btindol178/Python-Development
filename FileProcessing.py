# fruits.txt is in same directory as fileprocessing
myfile = open("fruits.txt")
print(myfile.read()) # this is a read method 

# another way to do it
file = open("bear.txt")
content = file.read()
print(content)

# close files
myfile2 = open("fruits.txt")
content2 = myfile2.read() #store in variable
myfile2.close() # closes file
print(content2)

# another way to do it
with open("fruits.txt") as myfile3:
    content = myfile3.read()

print(content)

#using file from different directory
# another way to do it
with open("C:/Users/blake/OneDrive/Full Stack Development/OtherDirectory/bear.txt") as myfile3:
    content = myfile3.read()

print(content)

# Writing txt to file.
with open("C:/Users/blake/OneDrive/Full Stack Development/Python 10 Project MasterCourse/vegetables.txt","w") as myfile6:
    content = myfile6.write("Melina is cute")

# another way
with open("C:/Users/blake/OneDrive/Full Stack Development/Python 10 Project MasterCourse/vegetables2.txt","w") as myfile7:
    myfile7.write("Melina is cute\nlike really alot\n cool")
    myfile7.write("DOODIE")

#print 90 characters  of the content
file = open("bear.txt")
content = file.read()
file.close()
print(content[:30])

# define function that gets a single string character and a filepath as parameters and runs the  number of occurances of that character in the file
def foo5(character, filepath="bear.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character) 
print(foo5("e","bear.txt"))

# create a file with name file.txt and write a text snail
with open("file.txt", "w") as file:
    file.write("snail")

# create a file first text that gets the first 90 characters of the bear file 
with open("bear.txt") as file:
    content = file.read()
with open("first.txt", "w") as file:
    file.write(content[:90])

# This appends okra to the previous file of fruits
with open("C:/Users/blake/OneDrive/Full Stack Development/Python 10 Project MasterCourse/fruits.txt","a") as myfile8:
    myfile8.write("Okra")
  
print(content)


# This appends okra to the previous file of fruits and writes
with open("C:/Users/blake/OneDrive/Full Stack Development/Python 10 Project MasterCourse/fruits.txt","a+") as myfile8:
    myfile8.write("Okrazzz")
    myfile8.seek(0)# moves the cursor back to the first position
    content= myfile8.read()
print(content)

# append the text of bear1.txt in otherwears and bear 2 should contain text and the text of bear1 after that
with open("bear1.txt") as file:
    content = file.read()

with open("bear2.txt", "a") as file:
    file.write(content)

# open data.txt and append
with open("data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content)

    # more file processing
    with open("file.txt") as file:
    content = file.read()

# write
with open("file.txt", "w") as file:
    content = file.write("Sample text")

# append
with open("file.txt", "a") as file:
    content = file.write("More sample text")

# apend and read
with open("file.txt", "a+") as file:
    content = file.write("Even more sample text")
    file.seek(0)
    content = file.read()
