# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Incorrect
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 4: Incorrect
What is the output of the following code?

"/spam/ham/eggs/".split("/")
"""


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#('spam', 'ham', 'eggs'
#['spam', 'ham', 'eggs']
#["", 'spam','ham', 'eggs', '']
#("", 'spam','ham', 'eggs', 'e

# Answer: 


print("/spam/ham/eggs/".split("/"))




# Question 4b: Which 'only' string method is prefixed by a separator?
# 4b Answer: The .join() method is unique in that the method is called on the separator, which is inserted between each element of an iterable: 'sep'.join(iterable)





''' Question 4c: What is the output of the following lines?

print(' '.join([['abc'], ['def']]))

print(' '.join(['a', 'b']))

print('z'.join('a'))

print('z'.join('a', 'b'))

4c Answers:

i) TypeError: sequence item 0: expected str instance, list found

ii) a b

iii) a

iv) TypeError: join() takes exactly one argument (2 given)
'''
