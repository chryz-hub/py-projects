# import the json library
import json
# library for close matchng of words
from difflib import get_close_matches

# load a json file
data = json.load(open("data.json"))

# defines the function translate() in a more suitable way
def translate(word):
    word = word.lower()
    # using conditions to get the proper definations despite the manner of input
    if word in data:
        return data[word]
    elif word.title() in data :
        return data[word.title()]
    elif word.upper() in data :
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0 :
# getting the closest word and the meaning
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("Press yes or no: ")
        if decide == "yes":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "no":
            return ("-------The word does not exist!-------")
        else:
            return("----You have entered the wrong input!, please enter yes or no ----")
    else:
        print("-----You have entered the wrong word, please check it again!-----")


# For the user
word = input("Enter the word you want to search for: ")
#called out the function we defined above
output= translate(word)
#if the defination of a word is more than one, it is a list automatically
#Iteration for the definations in a list to be seperated and more visible for people to understand
if type(output) == list :
    for item in output :
        print(item)
else:
    print(output)
