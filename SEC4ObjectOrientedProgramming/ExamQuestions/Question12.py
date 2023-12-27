# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 12: Incorrect
    Select the choices which will return TRUE?
"""
class Spam:
  ham = 36

spam = Spam()

#1)print("hasattr(spam, 'ham') :", hasattr(spam, 'ham') )
#2)print("spam.hasattr('ham') :", spam.hasattr('ham') )
#3)print("hasattr(pam, 'ham') :", hasattr(pam, 'ham') )
#4)print("hasattr('spam', 'ham') :", hasattr('spam', 'ham') )
#5)print("hasattr('Spam', 'ham') :", hasattr('Spam', 'ham') )

# Answer: 1

""" Remember: hasattr(object_OR_class, 'attribute') checks if an object (or class) contains an attribute, but only the second argument is 
(and must be) a string. """
