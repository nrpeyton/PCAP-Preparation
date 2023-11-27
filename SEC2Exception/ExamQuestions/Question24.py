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



# Answer (26-11): 3 - - - - - - - Correct (with research required)
''' Research/Learnings:
Without the 'return' statement, execution would be halted after printing 'try except finally'  instead of exiting the function and continuing.

Also remember the 'finally' branch does NOT catch the exception and does NOT allow execution to continue outside its own scope.

Python's traceback shows chained exceptions when a new one is raised in handling a previous one, detailing both (or more).  For independent exceptions, only the most 
recent uncaught exception is displayed in the traceback.
'''













# Answer: 3; using 'return' without a suffix returns 'None'.
