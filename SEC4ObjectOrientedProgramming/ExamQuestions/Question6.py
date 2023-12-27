# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 6: Incorrect
Select the choices which will return TRUE?
"""
class X:
    pass

class Y:
    pass

class Z(X, Y):
    pass

# i)print("issubclass(Z, (list, X, Y))", issubclass(Z, (list, X, Y)))
# ii)print("issubclass(X, Z) and issubclass(Y, Z): ", issubclass(X, Z) and issubclass(Y, Z))
# iii)print("issubclass(Z, X, Y: ", issubclass(Z, X, Y))
# iv)print("issubclass(Z, X) and issubclass(Z, Y): ", issubclass(Z, X) and issubclass(Z, Y))

# Answer: 1, 4












'''                             i)print("issubclass(Z, (list, X, Y))", issubclass(Z, (list, X, Y)))

The issubclass() function in Python, when used with a tuple as its second argument, offers a flexible way to check class inheritance against multiple 
potential parent classes. This functionality can be summarized with the analogy that the tuple in issubclass(Z, (Class1, Class2, Class3)) is essentially 
just an expanded second argument. Instead of the function being limited to a single class comparison like issubclass(Z, Class1), the tuple allows for 
a list-like collection of classes to be checked.  

Remember, in issubclass(Z, (list, X, Y)), the class 'list' is unrelated to X and Y; it's simply another class included in the tuple for checking. 
This could be any class, built-in (like float) or user-defined. The specific choice of list or float isn't related to X or Y; they are just examples of 
additional classes incorporated into the tuple for the subclass check

This analogy highlights the following points:

-Flexibility: The tuple acts like a container for multiple class or type objects, allowing issubclass to perform multiple subclass checks in one go.
-Simplicity: By using a tuple, the function maintains its simple two-argument structure while gaining the ability to check against multiple classes.
-Dynamic Checking: The tuple can be dynamically created and modified, making issubclass adaptable to different situations and requirements.

In this way, the tuple in the issubclass function serves as a straightforward yet powerful tool, demonstrating Python's emphasis on readable, efficient, 
and flexible code design.
'''
