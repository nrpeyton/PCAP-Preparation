# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 7: Incorrect
What is the output of the following code?
"""
F = type('Food', (), {'remember2buy': 'spam'})
E = type('Eggs', (F,), {'remember2buy': 'eggs'})
G = type('GoodFood', (E, F), {})
print(F.remember2buy, E.remember2buy, G.remember2buy)

# i)spam eggs eggs
# ii)spam eggs
# iii)SyntaxError: invalid syntax
# iv)Food Eggs GoodFood
# v)No output

# Answer: i)spam eggs eggs














'''
class type(object)

With one argument, return the type of an object. The return value is a type object and generally the same object as returned by object.__class__.



class type(name, bases, dict, **kwds)

With three arguments, return a new type object. This is essentially a dynamic form of the class statement. The name string is the class name and 
becomes the __name__ attribute. The bases tuple contains the direct base classes and becomes the __bases__ attribute; if empty, object, the ultimate base 
of all classes, is added. The dict dictionary contains attribute and method definitions for the class body; it may be copied or wrapped before becoming 
the __dict__ attribute. The following two statements create identical type objects:
'''

#1
class X:
    a = 1

#2
X = type('X', (), dict(a=1))





F = type('Food', (), {'remember2buy': 'spam'}) # is the same as:


class Food:
    remember2buy = 'spam'

F = Food


'''
Note that capital 'F' here is non-conventional, and `food_class = Food` may be preferred.

Instance instantiation can also be done dynamically:
'''
food_instance = type('Food', (), {'remember2buy': 'spam'})()











































#*NOTE: see MRO: Method Resolution Order - set of rules that construct linerization of Classes
#   -precedence order diagram, "non-ambiguous hierarchy"
