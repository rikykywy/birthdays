import sys
#importing the sys module, useful to get the user inputs#

if len(sys.argv) > 1:
    to_print = sys.argv[1]
else:
    print("Give me an argument to print")
    exit()
#This condition sets the minimum lenght of the input to be stored as one character#
#Otherwise it will return a message that reminds to write enough data as input"
print("The name of this program is {}".format(sys.argv[0]))
print("You entered {}".format(to_print))
#Then it will print what the user typed and the name of the program#
