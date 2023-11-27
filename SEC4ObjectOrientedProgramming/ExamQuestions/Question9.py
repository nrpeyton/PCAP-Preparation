# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
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

#i)print("s.__ham: ", s.__ham )
#ii)print("s.eggs(): ", s.eggs() )
#iii)print("s.__eggs(): ", s.__eggs() )
#iv)print("s._Spam__ham: ", s._Spam__ham )
#v)print("s._Spam__eggs(): ", s._Spam__eggs() )

# Answer: 



























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

