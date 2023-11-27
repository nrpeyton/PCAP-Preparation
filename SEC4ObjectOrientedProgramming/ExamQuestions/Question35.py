# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 35: Incorrect
What is the output of the following code?
"""
def foo(self, p):
    print('Hello', p)

class Spam:
    bar = foo

s = Spam()
s.bar('World')  #which is really s.foo(...) ...

#i)SyntaxError: invalid syntax
#ii)NameError: name 'foo' is not defined
#iii)No output
#iv)Hello World

# Answer: 