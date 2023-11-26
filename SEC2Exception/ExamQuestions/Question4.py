# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Incorrect
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -
"""
Question 4:
Select which option will call the __init__ method of Exception based on the code below.

class NewException(Exception):
  def __init__(self, message):
    <<< INSERT CODE HERE >>>
    self.message = message
raise NewException("Spam")W
"""



class NewException(Exception):
    def __init__(self, message):
        # Exception.__init__(self, message)
        # super(NewException, self).__init__(message)
        # super.__init__message()
        # super().__init__message()
        self.message = message
raise NewException("Spam")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Answer: 1, 2



''' RESEARCH/LEARNINGS:

1.
super() with Arguments:

Syntax: super(type, object_or_type=None).
Purpose: Bypasses Method Resolution Order (MRO) in multiple inheritance.
Example:


class ParentA:
    def show(self):
        print("ParentA show")

class ParentB(ParentA):
    def show(self):
        print("ParentB show")

class Child(ParentB):
    def show(self):
        super(ParentB, self).show()  # Calls ParentA's show, since ParentA is the superclass of ParentB

# Usage
child = Child()
child.show()  # This will call ParentA's show()




2.
Custom Exception Initialisation:

Direct explicit initialisation of built in exceptions' in the constructor of custom exceptions either with Exception.__init__(message) or using super() 
is not necessary when dealing with Python exceptions.  This realisation emerged from observing that the code functions correctly without this initialisation,
indicating a misconception in the question's context.  In short, none of the four options are actually required, not even the 2 correct options.
'''