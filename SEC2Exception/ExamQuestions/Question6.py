# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Incorrect
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -

"""
Which option(s) will print ELSE given the following code?

try:
    <<< INSERT CODE HERE >>>
except ZeroDivisionError:
  print('ZeroDivisionError')
except TypeError:
    print('TypeError')
else:
    print('ELSE')
"""
try:
    # pass
    # insert "blank"
    # raise TypeError
    # raise ZeroDivisionError
    # raise
    # raise Exception
except ZeroDivisionError:
    print('ZeroDivisionError')
except TypeError:
    print('TypeError')
else:
    print('ELSE')
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Answer (26-11): pass - - - - - - - Correct






















# Answer: pass

# Takeaway:
# Remember 'else' is only executed ON   S U C C E S S F U L   execution in the 'try' block.   I know, it is not intuative and seems back-to-front!
# Instead of thinking "try this, else this", think: "Error-Free? Then Else" or "Try, and if No Interruptions, Then Else".  In other words, the default
# is that we're EXPECTING an error, or else.
# If that's too confusing, just memorise the first sentence!
