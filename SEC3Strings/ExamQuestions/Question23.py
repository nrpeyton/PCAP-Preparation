# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Incorrect (but think I only entered the wrong option number).
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 23: Incorrect
What is the output of the following code?

d = { 'zero':0, 'one':1, 'three':3, 'two':2 }
for k in sorted(d.keys()):
    print(d[k], end=' ')
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# zero one two three
# TypeError: sorted expected 2 arguments, got 1
# 0 1 2 3
# 1 3 2 0
# one three two zero

# Answer: 





d = { 'zero':0, 'one':1, 'three':3, 'two':2 }
for k in sorted(d.keys()):
    print(d[k], end=' ')
























'''
d = {'zero': 0, 'one': 1, 'three': 3, 'two': 2}
for k in sorted(d.keys()):  # RE: sorted() SORT KEYS ALPHABETICALLY (LEXICOGRAPHICAL)
    print(d[k], end=' ')
'''