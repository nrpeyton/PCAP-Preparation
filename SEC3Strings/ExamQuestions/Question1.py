# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Incorrect
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 1: Incorrect
What is the output of the following code?

spam.txt

spam ham eggs
spam.py

f = open('spam.txt', 'r')
if 'eggs' in f:
    print('Eggs found')
else:
    print('Eggs not found')
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#SyntaxError: invalid syntax
#Eggs not found
#Eggs found
#TypeError: argument type TextOfWrapper not iterable

'''

Answer: Incorrect; actual output is 'Eggs not found'.
Explanation:
File objects are iterable line by line such that explicit read methods are not always necessary.  The 'in' operator used with file objects checks for (entire) exact 
line matches, including the newline character.  Substring matches 'within' lines don't satisfy the 'in' condition for file objects.
'''
