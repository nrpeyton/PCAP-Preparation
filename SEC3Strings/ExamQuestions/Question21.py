# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Correct
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 21: Incorrect
What is the output of the following code?

spam = [4*(3+5), 4*3+5, 4+3*5, (4+3)*5]
spam.sort(reverse=True)
spam
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#TypeError: 'reverse' is an invalid keyword argument for sort()
#[35, 19, 17, 32]
#[35, 32, 19, 17]
#[17, 19, 32, 35]
#[32, 17, 19, 35]

# Answer: 2





# Question 21a: What's the purpose of the last line?
# Answer: Printing the second line would return 'None' because list.sort() does not return a value.  The second line cannot be printed, but the last line can.

# Question 21b: Given the correct answer to Q.21a, why isn't this true for all string methods?
# Answer: All string methods must return a value because strings are immutable and cannot be modified in-place.