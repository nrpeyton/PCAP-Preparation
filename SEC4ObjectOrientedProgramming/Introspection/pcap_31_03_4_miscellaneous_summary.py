#                                                     _ _ s t r i n g _ _                                                                                            # type: ignore # pylint: disable=all                                 
class A:
    def fun(self):
        pass

a = A()
#                       NOTES:                              OUTPUT:
print(a, a.__str__())   # both call object.__string__()     <__main__.A object at 0x7f4c8e9c6310> <__main__.A object at 0x7f4c8e9c6310>








#                                                     _ _ n a m e _ _    

""" __name__ can supply the name of a class, function, method, or module, but NOT an object or variable.  Think DEFINED (def) only. """
print(__name__) # Output: module name, e.g., __main__

class A:
    def __init__(self):
        pass
    def method(self):
        pass
    def __prvtMthd(self):
        pass
a = A() #                                                            NOTES:                                 OUTPUT:
print(A.__name__) #                                                                                         A
print(a.__init__.__name__           ,     A.__init__.__name__) #     __specialMethods__ are NOT mangled     __init__    __init__
print(a.method.__name__             ,     A.method.__name__) #                                              method      method
print(a._A__prvtMthd.__name__       ,     A._A__prvtMthd.__name__) #                                        __prvtMthd  __prvtMthd







#                                                     _ _ m o d u l e _ _   

""" __module__ can supply the module name (i.e., main.py) that contains the entity your querying.  Use on functions, classes, methods and objects, but NOT variables """

class ExampleClass:
    pass
print(ExampleClass.__module__) # Output: __main__





#                                                     _ _ d i c t _ _    
""" 
Instance: Contains only the instance-specific writable attributes that are explicitly added to the object, i.e., instance variables only.
Class: Holds the namespace of the class including class variables, class methods, class's module, class docstring, and weakref.
"""
class A:
    cv = 'cv'
    def __init__(self):
        self.iv = 'iv'
        self.__v = 'v'
a = A()                                                 #OUTPUT:                                                    
print(A.__dict__)                                       {'__module__': '__main__', 'cv': 'cv', '__init__': <function A.__init__ at 0x7f4fac0ae0e0>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}    
print(a.__dict__)                                       {'iv': 'iv', '_A__v': 'v'}
print(vars(a))                                          {'iv': 'iv', '_A__v': 'v'}

a.__vi = 'vi'
print(a.__dict__)                                       {'iv': 'iv', '_A__v': 'v', '__vi': 'vi'}









#                                                   _ _ b a s e s _ _

# Special class attribute:  Classname.__bases__
class Chordata:
    pass

class Reptiles(Chordata):
    pass

class Snakes(Reptiles):
    pass

class Python(Snakes, Reptiles):
    pass

print(Python.__bases__)  # Output: (<class '__main__.Snakes'>, <class '__main__.Reptiles'>)

'''
Output:
- A tuple containing the direct base classes (direct superclasses) of the 'Python' class.
- In this case, the 'Python' class inherits from the 'Snakes' class.
- Outputs as a tuple, even if there is only one base class.
'''

print(Python.__bases__[0].__name__) # Output: Snakes








#                                                     t y p e ( )
class A:
    def fun(self):
        pass

a = A()
#                       NOTES:                              OUTPUT:
print(type(A))          # Returns the type object          <class 'type'>       
print(type(a.fun))      #                                  <class 'method'>
print(type(a))          #                                  <class '__main__.A'>







#                                                   i s i n s t a n c e ( )
isinstance(object, Class_or_tuple)






#                                                   i s s u b c l a s s ( )
issubclass(Class, Class_or_tuple)








#                                                   h a s a t t r ( )

hasattr(object_or_Class, 'attribute')   # attribute: variables and methods
