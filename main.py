#! /usr/bin/env python3
from birthdays import return_birthday
from birthdays import print_birthdays
import argparse


print_birthdays()



parser = argparse.ArgumentParser(prog='This program returns the birthday of famous people')
parser.add_argument('n', help='You have to insert a name in the format: "Name Surname"')
parser.add_argument('-v', '--verbosity', type=int, choices=[0, 1, 2], help='Verbosity level')
 

args = parser.parse_args()
name = args.n



def verbosity_levels(name):
    for a in name:
        if birthdays.return_birthday(a):
            if args.verbosity >= 2:
                print('{} was born the {}'.format(name, birthdays.return_birthday(name)))
            elif args.verbosity >= 1:
                print ('{} : {}'.format(name, birthdays.return_birthday(name)))
            else:
                print (birthdays.return_birthday(name))
    else:
        print ('Sorry, {} is not in the list, '.format(name))
        birthdays.print_birthdays()



return_birthday(name)

# verbosity option 
