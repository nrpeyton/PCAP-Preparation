# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Incorrect
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 10: Incorrect
Which option will return True given the following code?

spam = 'FuBar'
ham = spam[:]
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#spam.startswith(ham)
#spam.equals(ham)
#id(spam)==id(ham)
#spam==ham
#spam.endswith(ham)

# Answer: 



''' Question 10b:
What distinguishes slicing a list to create a new list in Python from slicing a string, considering how Python handles memory and object references for mutable and 
immutable types?

A) Slicing both lists and strings always creates deep copies of the objects, resulting in different memory locations.

B) Slicing a list creates a new list object, but slicing a string does not necessarily create a new string object due to Python's optimization for immutable types.

C) Slicing a string always results in a new string object in a different memory location, but slicing a list reuses the same list object.

D) Slicing neither a list nor a string creates a new object; both operations only create references to the original objects.
'''

# 10b Answer: 











spam = 'FuBar'
ham = spam[:]
print(spam.startswith(ham))
print(id(spam)==id(ham))
print(spam==ham)
print(spam.endswith(ham))