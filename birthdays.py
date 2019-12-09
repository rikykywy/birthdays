#This code contains two functions and a dictionary "birthdays", that contains the dates of birth of 5 famous people and their names. The dictionary has as keys the names and as values the dates of birth. The functions operate on this dictionary#

birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}

#The first function prints all the available names in the dictionary before a wellcoming phrase#
def print_birthdays():
    print('Welcome to the birthday dictionary. We know the birthdays of these people:')
    for name in birthdays:
        print(name)

#The second funtion iterats trough the dictionary and prints, if the name is in birthdays, the name requested along with the date of birth of that person. Otherwise it returns a statement that says the date of birth of that person is not in the dictionary#
def return_birthday(name):
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

