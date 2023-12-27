# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Incorrect
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 27: Incorrect
Select the line number from the options(s) which will print Spam
"""
class Spam:
    def v0(self):
        print("Line 3:", __name__)

print("Line 4: ", __name__)

s = Spam()
s.v0()

print("Line 7: ", s.__class__.__name__)
print("Line 8: ", Spam.__name__)
print("Line 9: ", s.__name__)

#1)Line 9
#2)Line 4
#3)Line 7
#4)Line 8
#5)Line 3

# Answer: Line 7, Line 8

"""
__name__:

1. Referencing __name__ without prefixing a 'defined' entity (see below) always returns a string with the name of the currently running module or 
script, at the top-level, this is '__main__'.

2. A class, function, method, or module has a __name__ attribute, but NOT objects:
In Python, functions, methods, and classes have a __name__ attribute because they are defined entities with specific names used for reference and 
introspection. Regular objects, being instances of classes, lack a __name__ attribute as they are identified by their state and behavior rather than a
static name, making such an attribute unnecessary for them.
"""