# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Incorrect
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -
"""
Question 25: Incorrect
What is the output of the following code?

def f():
    try:
        raise ArithmeticError
    except:
        raise AssertionError
    finally:
        raise AttributeError
    return
f()
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#1. SyntaxError: invalid syntax
#2. ArithmeticError
#3. No Output
#4. AssertionError
#5. Attribute Error

# Answer (26-11): 2, 4, 5  - - - - - - - Correct (with research required):

''' Learnings/Research: 
Read question 24's learnings first!  In this question (25), the 'return' statement is not within the scope of the 'finally' branch so is not executed.
Therefore, the output is simply the traceback showing the chained (i.e., all) exceptions.
'''

















# Answer: ArithmeticError, AssertionError and AttributeError will all be displayed in the console one after the other.
