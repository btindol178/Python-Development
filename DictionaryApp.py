# To run this program just type in terminal (python DictionaryApp.py)
# imporet difflib library to see if a word is similar to another
#from difflib import SequenceMatcher
# SequenceMatcher(None,"rainn","rain").ratio() # get word similarity ratio
# from difflib import get_close_matches (to get similar words from list)
# get_close_matches("rainn",["help","pyrimid",'rain'])
import difflib
from difflib import get_close_matches
# load json data
import json
data = json.load(open("C:/Users/blake/OneDrive/Full Stack Development/Application1Dictionary/data.json"))
#str(data) it is a dictionary # This loads the data into a python dictionary

# make function that takes input and loads data
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys()))> 0: # looks for the missspelled word in keys of data if list length is greater than 0
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: "  % get_close_matches(w,data.keys())[0]) # get first element of get close matches and put it in %s formater in string
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "The word does not exist. Please double check it."
        else:
            return "We did not understand your query?"

    else:
        return "The word does not exist. Please double check it."


word = input("Enter word: ")
output = translate(word) #print(translate(word))  because just printing translate(word) gives you ['word1','word2'] output not user friendly
#for item in output:
        #    print(item) # this will print each string letter by letter with new line we dont want this
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output) # dont need to iterate throught the output if it is astring (meaning if the word is in the dictionary)
