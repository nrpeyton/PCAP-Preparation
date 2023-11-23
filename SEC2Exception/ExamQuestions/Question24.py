# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Correct
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -
"""
Question 24: Incorrect
What is the output of the following code?

def f():
    try:
        print('try ', end='')
        raise ArithmeticError
    except:
        print('except ', end='')
        raise AssertionError
    finally:
        print('finally')
        return
f()
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#try except <AssertionError logs> finally
#try <ArithmeticError logs> except <AssertionError logs> finally
#try except finally
#try except <AssertionError logs>
#try except finally <AssertionError logs>
#try except finally <ArithmeticError logs> <AssertionError logs>

# Answer: 3; using 'return' without a suffix returns 'None'.
