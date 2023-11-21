# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -
"""
Question 27:
What is the output of the following code?

class E(Exception):
    def __init__(self, message="Stop"):
        self.message = message
    def __str__(self):
        return "Surprise"

try:
    raise Exception
except E as e:
    print(e)
else:
    print("Goodbye")
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Surprise
#Goodbye
#Unhandled Exception
#Stop
