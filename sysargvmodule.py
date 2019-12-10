import sys
#importing the sys module, useful to get the user inputs#

if len(sys.argv) == 3:
    user_input = sys.argv[1] + " " + sys.argv[2]

else:
    print("Not a valid name")
    exit()

return_birthday(user_input)
#This condition sets the minimum lenght of the input to be stored as one character#
#Otherwise it will return a message that reminds to write enough data as input"
print("The name of this program is {}".format(sys.argv[0]))
print("You entered {}".format(to_print))
#Then it will print what the user typed and the name of the program#
