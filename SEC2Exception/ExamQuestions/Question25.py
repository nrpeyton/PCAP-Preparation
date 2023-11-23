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
#SyntaxError: invalid syntax
#ArithmeticError
#No Output
#AssertionError
#Attribute Error

# Answer: ArithmeticError, AssertionError and AttributeError will all be displayed in the console one after the other.
