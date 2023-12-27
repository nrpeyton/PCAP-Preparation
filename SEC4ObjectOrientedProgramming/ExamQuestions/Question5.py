# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 5: Incorrect
What is the output of the following code?
"""
def spam():
    class Ham:
        def eggs(self):
            print('Hello World')
    return Ham()

spam().eggs()

#1) AttributeError: spam() has no attribute 'eggs'
#2) No output
#3) Hello World
#4) SyntaxError: invalid syntax

# Answer: Hello World

"""








Steps:

1. Parses the only the definition of the spam() function and its structure.
Inside spam(), identifies only the definition of the Ham class and its method eggs().

2. The interpreter sees that spam() is designed to return an instance of the Ham class, as indicated by return Ham().

3. Executing spam() and eggs():

Upon encountering spam().eggs(), Python first executes spam(). This execution results in the creation (and return) of a Ham instance, similar to what would happen if you did obj = Ham().
Immediately following the creation of the Ham instance, the eggs() method is called on this instance. This is equivalent to calling obj.eggs() if you had stored the instance in obj.
The execution of eggs() leads to printing "Hello World".
"""