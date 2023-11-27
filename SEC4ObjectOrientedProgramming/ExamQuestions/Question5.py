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

#i)AttributeError: spam() has no attribute 'eggs'
#ii)No output
#iii)Hello World
#iv)SyntaxError: invalid syntax

# Answer: 