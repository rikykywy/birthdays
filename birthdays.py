"""This code contains two functions and a dictionary "birthdays", that contains 
the dates of birth of 5 famous people and their names. The dictionary has as 
keys the names and as values the dates of birth. The functions operate on this  
dictionary"""

#imort .csv file with data list#
import csv

reader = csv.reader (open('databirth2.csv', 'r'))
d = {}
for row in reader:
    k,v = row  
    d[k]= v


"""The first function prints all the available names in the dictionary before a 
wellcoming phrase"""


def print_birthdays():
    print('Welcome to the dictionary.We know the birthdays of these people:')
     for e in d:
        print(e)

"""The second funtion iterats trough the dictionary and prints, if the name is 
in birthdays, the name requested along with the date of birth of that person. 
Otherwise it returns a statement that says the date of birth of that person is 
not in the dictionary"""


def return_birthday(name):
    if name in d:
        return d[name]
    else:
        return False 

     
