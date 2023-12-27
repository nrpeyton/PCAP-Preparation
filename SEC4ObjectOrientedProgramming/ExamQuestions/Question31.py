# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Correct
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 31: Incorrect
What is the output of the following code?
"""


class A:
    def spam(self):
        return 'A.spam'

    def ham(self):
        return self.spam()


class B:
    def spam(self):
        return 'B.spam'


class C(B, A):
    pass


c = C()

print(c.spam(), c.ham())

# i)B.spam A.spam
# ii)B.spam B.spam
# iii)A.spam A.spam
# iv)TypeError: Cannot create a consistent method resolution

# Answer: B.spam B.spam

""" Bonus: The MRO originates from class C and remains unchanged through chained method calls like 'ham' → 'spam'. The context 'self' stays as a C instance, 
preserving the MRO's inheritance sequence. """





































# *RE: Method Resolution Order -
# print("C.__mro__", C.__mro__)  # method resolution order for function execution
#   C.__mro__ (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
