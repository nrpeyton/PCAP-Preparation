# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Correct
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 11: Incorrect
What is the output of the following code?

spam = chr('a')
ham = ord(spam)
print(spam, ham)
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#TypeError: an integer is required( got type str)
#TypeError: ord() takes exactly two arguments( 1 given)
#97 a
#Syntax Error
#TypeError: chr() takes exactly two arguments( 1 given)

# Answer: 1




























spam = chr('a')    #ERROR! spam = chr('a'); TypeError: an integer is required (got type str)
ham = ord(spam)    #RE!: chr(i)- return the string representing a char whose Unicode code is an int
                   #     ord(c)- given a string representing Unicode character, return an integer
print(spam, ham)
