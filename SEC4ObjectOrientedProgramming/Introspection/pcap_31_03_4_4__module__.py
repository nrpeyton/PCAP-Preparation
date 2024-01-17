# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - PCEP-31-03 4.2 - Employ class and class and object properties - - - - - - -

#                                                 _ _ m o d u l e _ _

""" 
1. __module__ only works on objects, classes, functions, and methods, but NOT on variables.  

2. It returns the script's file name (i.e., main.py) that the entity is defined in.

3. It's not an 'attribute' in the traditional sense, and not added for convenience, but an integral, automatically assigned link connecting a class, 
function, or method to its defining Python file (module), making it useful for tracking origins and managing namespaces. 
"""





# Return the list of modules that have been imported in your session:

import sys as sys
#print(sys.modules)



#Return the name of the module where class is defined:

class SomeClass:
    pass

print(SomeClass.__module__)
print(SomeClass.__class__)
print(SomeClass.__class__.__module__)






class A:
    def fun(self):
        pass

a = A()

print(A.__module__) # Output: __main__ is 'main.py'































# __module__ is where every Python class has a built-in class attribute which is the name of the module (main.py) in which the class is defined
# -each class and function has a __module__attribute that returns the name of the module in which the cass is defined