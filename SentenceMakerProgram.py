#in terminal connect to python first by typing python and seeing >>>
#  Control f5 how you run the program
def sentence_maker(phrase):
    interrogatives = ("how","what","why")
    capitalized = phrase.capitalize() # capitalizes string
    if phrase.startswith(interrogatives):
        return("{}?".format(capitalized))
    else:
        return"{}.".format(capitalized)
print(sentence_maker("how are you"))

results = []
while True:
    user_input = input("Say something: ")
    if user_input == "/end" :
        break
    else:
        results.append(user_input)
print(" ".join(results))
