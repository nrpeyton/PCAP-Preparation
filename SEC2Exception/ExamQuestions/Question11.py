# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Incorrect
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -

"""
Question 11: 
What is the output of the following code?

try:
    raise Exception
except BaseException:
    print("Spam")
except Exception:
    print("Ham")
except:
    print("Eggs")
"""


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Answer (26-11): Spam - - - - - - - Correct















# Answer: Spam

# Takeaway:
# In Python exception handling, order except blocks from specific to general exceptions.  Python matches exceptions to the first suitable except block. 
# Placing a general exception before a specific one can lead to unintended handling, as the general block will catch all instances, including those for 
# specific exceptions.

try:
    raise Exception
except BaseException:
    print("Spam")
except Exception:
    print("Ham")
except:
    print("Eggs")