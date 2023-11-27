# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Incorrect
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -
"""
Question 20: Incorrect
What is the output of the following code if spam.txt does not exist?

import sys
try:
    f = open('spam.txt')
    s = f.readline()
except:
    raise
"""
import sys

try:
    f = open('spam.txt')
    s = f.readline()
except:
    raise
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#FileNotFoundError: [Errno 2] No such file or directory: 'spam.txt'
#the script will run but will not print anything
#"None" will be printed
#Compile time errors

# Answer (26-11): 1 - - - - - - - Correct









# Answer: 1