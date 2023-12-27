# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 25: Incorrect
Select the option(s) which will return the dictionary or other mapping object used to store an object’s (writable)
attributes of the following code
"""
class Person:
    name = "John"
    age = 36
    country = "USA"

p = Person()

#1) print("p.__dict__: ", p.__dict__)
#2) (print("vars(p): ", vars(p))
#3) print("vars(Person): ", vars(Person) )
#4) print("Person.__dict__:", Person.__dict__)

# Answer: 3, 4

""" __dict__: Python has seperate dictionaries for objects and classes. The object.__dict__ typically only shows instance variables but not methods 
(exception: unless a method is dynamically created), but Class.__dict__ shows both. 

vars(object_OR_class): Returns the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.
"""