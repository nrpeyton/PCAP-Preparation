# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Incorrect
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 28: Incorrect
What is the output of the following code?
"""
class A:
    def __init__(self):
        pass

    def spam(self):
        pass

    def ham():
        return self.spam()

a = A()

print(a.ham())

#1)<bound method A.ham of <__main__.A object at 0x000001F709E67Fd0>>
#2)TypeError: ham() takes 0 positional arguments but 1 was given
#3)None
#4)0

# Answer: 2
# Remember: Python implicitly passes the object 'a' as an argument to 'ham', but with 'self' missing, it expects 0 arguments, not 1.