# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 16: Incorrect
What is the output of the following code?
"""

class Ham:
    def __init__(self):
        print('Ham', end=' ')
class Eggs:
    def __init__(self, end=' '):
        print('Eggs')
class Spam(Ham, Eggs):
    pass

s = Spam()

#1)Eggs
#2)Ham
#3)No output
#4)Ham Eggs

# Answer: Ham


















"""
One Class, One Spot:
"Each class should show up only once in the whole tree."

Subclasses First:
"A class comes before its parent."

Order Matters:
"Keep the order of parents as they are written." If a class has two parents, list them in the same order as in the class definition.

Respect the Line-Up:
"If one parent is usually ahead of another in line, keep it that way." Imagine two lines merging; if people from line A usually go before line B, 
keep that order.
"""


""" print("Spam.__mro__: ", Spam.__mro__) """  #(<class '__main__.Spam'>, <class '__main__.Ham'>, <class '__main__.Eggs'>, <class 'object'>)
