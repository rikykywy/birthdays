# Find famous people birthdays!
The repository we choose is "birthdays" wich contains the birthdays of several famous people.
By running main.py file by your terminal it will retur the dates of birth of the person you searched for, given a valid input and if it is present in our database databirth.csv contained in the datapackage folder.
To be able to run the code, you need first to insert your credentials (username and password).

## How to:
In the case of incorrect credentials, the program will return that either the password or the username is invalid.
Insert the name/s of the famous person you want to know the birthday of and your right credentials in order to get this outcome:
```
$ python3 main.py 'Albert Einstein' 'Alan Turing' -c username -p password -vv
User is present, password is valid
Albert Einstein was born the  03/14/1879
Sorry, Alan Turing is not in the list, 
We know the birthdays of these people:
Donald Trump
Rowan Atkinson
Albert Einstein
Ada Lovelace
Benjamin Franklin
```

## How to populat
If you want to only access the database, because you are already registered, you can run the ```main.py``` only. Instead, if you are registering for the first time you have to use the ```dbmanager.py``` in which you can find some useful instructions.

## Add a new user:
To add a new user into the database, these are the arguments you need to insert in ```dbmanager.py``` file:
* -h, --help: tells you the possible arguments you can insert
* -a: username
* -p: password

```
$ python dbmanager.py -a username -p password
Username username successfully added
```

## Credentials validition:
To check if your credentials are valid, please insert in ```dbmanager.py``` your new username and password, as the output will be:
```
$ python dbmanager.py -c username -p password
User is present, password is valid
```

## Execute the main application

The database contains this information:

Name and Surname	Birthday
Albert Einstein	03/14/1879
Benjamin Franklin	01/17/1706
Rowan Atkinson	01/06/1955
Ada Lovelace	12/10/1815
Donald Trump	06/14/1946

If you type a name that is not in the database, the program returns this message:

```
$ python main.py 'Alan Turing' -c username -p password
User is present, password is valid
Sorry, Alan Turing is not in the list, 
We know the birthdays of these people:
Rowan Atkinson
Ada Lovelace
Benjamin Franklin
Albert Einstein
Donald Trump
```
## Verbosity:
There are three different outup options, according by the number of -v you put at the end of the input.

1) If you omit -v, it will return only the date of the birthday. 03/14/1879
2) One -v: returns only name and date of birth. Albert Einstein : 03/14/1879
3) -vv: returns a sentence. Albert Einstein was born the 03/14/1879

## Test:
To test the application there are three functions, in the folder named ```tests/test_csv/```. In order to repeat the tests: ```python3 -m unittest -v -b tests/test_csv.py```. This output will follow: 

```
$ python3 -m unittest -v -b tests/test_csv.py
test_empty_datafile (tests.test_csv.TestMain)
Check the presence of data inside the csv file. ... ok
test_no_datafile (tests.test_csv.TestMain)
Check if there is a csv file. ... ok
test_valid_extension (tests.test_csv.TestMain)
Check the extension of the file. ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```


## PEP-8:
All the python modules and codes have been tested into the text regulation of PEP-8.

## Credits:
Pasti Riccardo-
Pasqualini Marco-
Gatti Giovanni-
Makosa Sara.

Composing the READ TAILS team!
