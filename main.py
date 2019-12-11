#! /usr/bin/env python3
from birthdays import return_birthday
from birthdays import print_birthdays
import argparse


parser = argparse.ArgumentParser(prog = 'This program returns the birthday of famous people')
parser.add_argument('-n', help='You have to insert a name in the format: "Name Surname"')
parser.add_argument('-v', '--verbosity', type=int, choices=[0,1,2], help='Decide the level of verbosity')


args = parser.parse_args()
name = args.n
birthday_data= return_birthday(name)


return_birthday(name)

#verbosity option
