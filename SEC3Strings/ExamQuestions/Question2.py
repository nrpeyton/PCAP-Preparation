# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Incorrect
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 2: Incorrect
What is the output to the following code?

"XYZ".join("123")
"""

print( "XYZ".join("123"))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#XYZ123
#X123Y123Z
#1XYZ2XYZ3
#TypeError: can only join an iterable
#123XYZ

# Answer:



'''
Question 2b: 
What are the outputs to the following lines?

i) print("XYZ".join(['123']))
ii) print(" ".join(['pip']))
iii) print("ABC".join("928"))
iv) print("8".join("846"))
v) print('0'.join(['6', '9', '2']))
vi) print(0.join([1, 2, 3]))
vii) print(0.join(1))
viii) Question: Given that strings are immutable, why must 'all' their methods be designed to return a value? 

2b Answers:
i) 123
ii) pip
iii) 9ABC2ABC8
iv) 88486
v) 60902
vi) Invalid syntax
vii) Invalid syntax
viii) Reason: Because they can't be modified in place or 'in situ'.
'''

