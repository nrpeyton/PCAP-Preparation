# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 42: Incorrect
Which of the option(s) below are valid given the following code?
"""
class Spam:
    __ham, ham = '__ham', 'ham'

    def __eggs(self):
        pass

    eggs = __eggs

s = Spam()
#INSERT CODE HERE

#1)print(s.__module__)
#2)print(__module__)
#3)print(Spam.__module__)
#4)print("s.__Spam_eggs.__module__")
#5)print(s.ham.__module__: )
#6)print("s.eggs.__module__")

# Answer: 1, 3, 4, 6






# __module__ only works on objects, classes, functions, and methods, but NOT on variables.  
# It returns the script's file name (i.e., main.py) that the entity is defined in.
# See ./pcap_31_03_4_4__module__.py for more details.
