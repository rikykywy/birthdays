"""main.py"""

import sys
import argparse
import sqlite3
from datapackage import birthdays
from scripts import dbmanager

"""If the user inputs one of the names that are present is inside 
   the datapackege names in the list the systeam will display the
   data of birth according to the verbosity level """



"""Define  positional and optional arguments"""

def parse_argument():
    
    parser = argparse.ArgumentParser(
             prog="This program return the birthday of famous people")
    parser.add_argument(
             'n', nargs='+', help='You can insert one or names in the'
             'format: "Name Surname"')
    parser.add_argument('-v', '--verbosity',default=0, action='count', 
                        help='Choose the level of verbosity')
    
    #check username and password from dbmanager.py
    parser.add_argument('-p', help="check password",
                        required=True)
    parser.add_argument('-c', help="check for a usernamename and password"
                        "(requires -p)", required=True)

    args = parser.parse_args()
    return args

"""Print the answer"""
def verbosity_levels(name):
    
    for x in name:
        if birthdays.return_birthday(x):
            if args.verbosity >= 2:
                print ('{} was born the {}'.format(
                       x, birthdays.return_birthday(x)))
            elif args.verbosity >= 1:
                print ('{} : {}'.format(x, birthdays.return_birthday(x)))
            else:
                print (birthdays.return_birthday(x))
        else:
            print ('Sorry, {} is not present in our list, '.format(x))
            birthdays.print_birthdays()
                        
db_corr = 'scripts/userlist.db'


if __name__ == "__main__":
    parse_argument()
    args = parse_argument()
    if dbmanager.check_for_username(args.c, args.p, db_corr):
        verbosity_levels(args.n)        
    
            


