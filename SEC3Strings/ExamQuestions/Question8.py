# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - INCORRECT
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 8: Incorrect
What is the output of the following code?

>>> s = 'Hello World'
>>> for i in len(s):
...     s[i] = s[i].upper()
>>> s
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Hello World
#Type Error: 'str' object does not support item assignment
#HELLO WORLD
#TypeError: 'int' object is not iterable

# Answer: 



s = 'Hello World'
for i in len(s):
    s[i] = s[i].upper()

