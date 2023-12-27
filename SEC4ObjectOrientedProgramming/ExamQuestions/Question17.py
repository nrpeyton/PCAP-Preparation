# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Correct
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 17: Incorrect
What is the output of the following code?
"""

class Spam:
    def __init__(self, v):
        self.ham = v                #3
        self.__ham = self. ham + 1  #4
s = Spam(100)                       #5
print(s.ham, s.__ham)               #6

#i)Error in Line 6
#ii)Error in Line 4
#iii)Error in Line 5
#iv)100 101
#v)Error in Line 3

# Answer: Error in Line 6 - attempted to access a private variable from outside the class without its mangled name.

# Bonus: Spaces before and/or after dots '.' are permitted.