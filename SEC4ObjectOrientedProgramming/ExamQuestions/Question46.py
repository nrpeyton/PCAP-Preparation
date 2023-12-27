# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Incorrect (should have got this one)
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 46: Incorrect
What is the output of the following code?
"""
class Spam:
  HAM = 1

  def __init__(self, v=2):
    self.v = v + Spam.HAM
    Spam.HAM += 1

a = Spam()
b = Spam(3)

print(a.v, b.v)

#i)TypeError:__init__() missing 1 required positional argument: 'v'
#ii)3 4
#iii)3 5
#iv)3 3

# Answer: 
