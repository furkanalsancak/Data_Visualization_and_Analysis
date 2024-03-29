import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt
import pandas as pd

plt.style.use("fivethirtyeight")


'''

In this block of code, we are reading data from data.csv file
We are getting the value from the column 'LanguagesWorkedWith, and splitting the languages each person know,
and storing them in a list
Then, we are creating a counter() variable, which counts how many times something is read
Inside a for loop, we are going through each row, getting the languages, and splitting them with ';' and storing them in a list
We are updating our counter variable with that list, each time for each row. 
Counter takes a List, and counts the items within that list

'''


data = pd.read_csv('data.csv')
# set these variables to all of the values in the respective columns in data.csv
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']
print(type(ids)) 


language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

# print(language_counter)


languages = []
popularity = []

for item in language_counter.most_common(15): # gets the most common 15 values counted
    languages.append(item[0])
    popularity.append(item[1])
    
print(languages)
print(popularity)



languages.reverse() #reversing these values, because we want the bars ranked from most to least
popularity.reverse()

plt.barh(languages, popularity) # takes y axis first

plt.title("Most Popular Languages")
# plt.ylabel("Programming Languages") # no need because languages are labels themselves
plt.xlabel("Number of People Who Use")

plt.tight_layout()

plt.show()