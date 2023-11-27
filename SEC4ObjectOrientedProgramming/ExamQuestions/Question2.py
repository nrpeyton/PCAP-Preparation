# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 2: Incorrect
Which of the option(s) below is / are valid given the following code?
"""
class Spam:
    __ham, ham = '__ham', 'ham'

    def __eggs(self):
        pass

    eggs = __eggs

s = Spam()
#<<< INSERT CODE HERE >>>

#i)print(Spam.__name__)
#ii)print(s.ham.__name__)
#iii)print(s._Spam__eggs.__name__)
#iv)print(s.eggs.__name__)
#v)print(s._Spam__ham.__name__)
#vi)print(s.__name__)

# Answer: 




















"""
*NOTE:
-__name__ is a built-in attribute that prints the name of the class,
 type, function, method, descriptor, or generator instance.
#ex the following code illustrates the use of __name__:

class Bar(object):
    def foo():
      #...
      pass

    print foo.__name__  #foo
print Bar.__name__      #Bar
"""
