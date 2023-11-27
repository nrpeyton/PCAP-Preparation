# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 8: Incorrect
What is the output of the following code?
"""

def spam():
    h = Ham()
    h.eggs()

    class Ham:
        def eggs(self):
            print('Hello World')
    return

spam()

#i)SyntaxError: invalid syntax
#ii)Hello World
#iii)UnboundLocalError: local variable 'Ham' referenced before assignment
#iv)No Output

# Answer: 



















"""
#*RE: this is legit!
def spam():
    class Ham:
        def eggs(self):
            print("Hello World")
    return Ham()
"""