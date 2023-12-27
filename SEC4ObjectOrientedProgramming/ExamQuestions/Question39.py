# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Incorrect
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 39: Incorrect
What is the output of the following code?
"""


class Ham:
    def __init__(self):
        print(type(self).__name__ + '.__init__()', end=' ')
        self.update()

    def update(self, param):
        print(type(self).__name__ + '.update(param)', end=' ')


Ham()
print("***DEBUG: help(Ham.update), ", help(Ham.update))


# 1)TypeError: update() missing 1 required positional argument 'param'
# 2)Ham.__init()__() Ham.update(param)
# 3)Ham.i__init__() Ham.update()
# 4)syntaxError: invalid syntax

# Answer: 1

""" Remember: type(object) returns the type (i.e., class) of the an object.  It does NOT return 'object' when used on an object! """

























# *NOTE:
# if there were no compile time errors, observe:
#    def update(self):
#         print(type(self).__name__ + '.update()', end=' ')
#   ...
#   OUTPUT:
#   Ham.__init__() Ham.update()
