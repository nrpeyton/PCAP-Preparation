# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Correct
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 11: Incorrect
What is the output of the following code?
"""
class Eggs:
    def __init__(self):
        print('Eggs', end=' ')
class Ham(Eggs):
    def __init__(self):
        print('Ham', end=' ')
class Spam(Ham):
    pass

s = Spam()


#1)Ham Eggs
#2)Type Error: __init__() takes 1 positional argument but 0 were given
#3)Eggs
#4)No output
#5)Ham

# Answer: 5)Ham

"""
Remember: __init__ is the only method that 'is' automatically executed on instantiation, whether inherited or not. Even the __str__ method is not 
automatically executed; it is implicitly called by Python (internally) when printing an object or converting an object to a string.
"""























#RE:
#-Method Resolution Order: set of rule that construct linearization of classes
#   meaning: it will execute the first __init__() it finds in the class method resolution order.
#   ex. Spam.__mro__    #Ham (<class '__main__.Spam'>, <class '__main__.Ham'>, <class '__main__.Eggs'>, <class 'object'>)
