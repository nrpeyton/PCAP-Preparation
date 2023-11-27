# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 7: Incorrect
What is the output of the following code?
"""
F = type('Food', (), {'remember2buy': 'spam'})
E = type('Eggs', (F,), {'remember2buy': 'eggs'})
G = type('GoodFood', (E, F), {})
print(F.remember2buy, E.remember2buy, G.remember2buy)

# i)spam eggs eggs
# ii)spam eggs
# iii)SyntaxError: invalid syntax
# iv)Food Eggs GoodFood
# v)No output

# Answer: 


















#*NOTE: see MRO: Method Resolution Order - set of rules that construct linerization of Classes
#   -precedence order diagram, "non-ambiguous hierarchy"
