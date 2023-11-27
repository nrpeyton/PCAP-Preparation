# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
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

#i)<bound method A.ham of <__main__.A object at 0x000001F709E67Fd0>>
#ii)TypeError: ham() takes 0 positional arguments but 1 was given
#iii)None
#iv)0

# Answer: 