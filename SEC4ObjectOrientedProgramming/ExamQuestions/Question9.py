3# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - 2/3 Correct
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 9: Incorrect
Which of the option(s) below are valid calls given the code below?
"""


class Spam:
    __ham = 0

    def __eggs(self):
        __ham = 100
        return __ham

    eggs = __eggs


s = Spam()

#---INSERT CODE HERE---

#1)print("s.__ham: ", s.__ham )
#2)print("s.eggs(): ", s.eggs() )
#3)print("s.__eggs(): ", s.__eggs() )
#4)print("s._Spam__ham: ", s._Spam__ham )
#5)print("s._Spam__eggs(): ", s._Spam__eggs() )

# Answer: 2, 4, 5




print("s.eggs(): ", s.eggs() )

print("s._Spam__ham: ", s._Spam__ham )
print("s._Spam__eggs(): ", s._Spam__eggs() )




















#*NOTES:
#-when an instance variable is declared, the object can be referred to as _ObjectName
#    ex. s = Spam()
#        ...
#        s._Spam...
#s.__ham         #you CANNOT call a private var from an instance
#s.eggs()        #eggs as initiated by __eggs
#c     #invalid declaration post its assignment!
#s._Spam__ham    #this is the CORRECT way to call in a "private variable"; vs...
#   SYNTAX: i._ObjectName__privateVariable
#s._Spam__eggs() #WRONG! unlike (above), using an object instance you CANNOT call a method this way!
#   RE: CORRECT: i._ObjectName__privateVariable
#       WRONG!:  i._ObjectName__methodName();
#       ex. s._Spam__eggs() #INCORRECT
#           s.eggs()        #CORRECT!

