# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - CORRECT
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 6: Incorrect
What is the output of the following code?

sorted(['banana', 'pear', 'grapes', 'apple'], key=lambda x: x[::-1])
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#['apple', 'banana', 'grapes', 'pear']
#Type Error: 'key' is an invalid keyword argument for sorted()
#SyntxError: invalid syntax
#['banana', 'apple', 'pear', 'grapes']

# Answer: 4


print(sorted(['banana', 'pear', 'grapes', 'apple'], key=lambda x: x[::-1]))