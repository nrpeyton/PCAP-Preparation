# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Correct
# - - - - - - - Practice Test 1: 3 Strings - - - - - - -

'''
Question 30:
Which option(s) results True?  And given a correct response to A, C and E; explain your reasoning.

Options:
A) not 'hello' is 'Hello'
B) 'hello' > 'Hello'
C) 'hello' is 'Hello'
D) 'hello' <= 'Hello'
E) 'hello' is 'hello'
'''

# Answer: A, B, E; due to string interning, where Python reuses an object for identical immutable strings for efficiency.








print(not 'hello' is 'Hello')
print('hello' > 'Hello')
print('hello' is 'Hello')
print('hello' <= 'Hello')
print('hello' is 'hello')
