# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Incorrect
# - - - - - - - Practice Test 1: 4 Object Orientd Programming - - - - - - -
"""
Question 18: Incorrect
What is the output of the following code?
"""
class MyClass:
    FOO = 100

    def __init__(self):
        self.bar = []

    def add(self, p):
        self.bar.append(p)

d, e = MyClass(), MyClass()
d.add('spam')
e.add('ham')
e.FOO = 200
MyClass.FOO = 300

print(d.bar, d.FOO, e.bar, e.FOO)


#1)['spam']100['ham']300
#2)['spam']300['ham']300
#3)['spam']100['ham']200
#4)['spam']300['ham']200


# Answer: #4)['spam']300['ham']200

# Learning: d.FOO did start off as `FOO = 100` on line 8, but never noticed it was modified on line 20!  
# Remember Python searches the instance first then the class.