"""
Jon Shallow
UNHM COMP705/805 Lab 1
An Introduction to Python
Jan 19, 2018

The purpose of this file is to learn BASIC python syntax and data structures.
There is an accompanying test file. Place both files in the same directory,
and then run:
$ python tests.py

You will see a print out of tests that are being run, and your result.
Please see: https://www.python.org/dev/peps/pep-0008/ for style guidelines
"""

def give_me_a_string():
    return("nick")

def give_me_an_integer():
    return(12)
def give_me_a_boolean():
    return(True)

def give_me_a_float():
    return(1.31)

def give_me_a_list():
    return([1,2,3])

def give_me_a_dictionary():
    return({"first" : "nick", "last" : "bielinski"})

def give_me_a_tuple():
    return(('nick', 'bielinski', 1995, 2017))

def sum_numbers_one_to_ten():
    runningtotal = 0
    for counter in range(11):
        runningtotal += counter
    return (runningtotal)

def check_is_even(number):
    if number % 2 == 0:
    	return (True)
    else:
	return (False)
def check_is_less_than(number1, number2):
    if(number1 < number2):
    	return(True)
    else:
	return(False)
def factorial(n):
    if n == 1:
        return (True)
    else:
        return n * factorial(n-1)
def give_me_an_exponent(n):
    return(5**n)
