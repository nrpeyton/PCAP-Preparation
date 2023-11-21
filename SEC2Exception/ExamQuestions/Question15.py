# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -

"""
What is the output of the following code?

class Spam(Exception):
    pass
class Ham(Spam):
    pass
for cls in [Spam, Ham]:
    try:
        raise cls()
    except Spam:
        print("Spam", end=" ")
    except Ham:
        print("Ham", end=" ")
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Spam Ham
#Spam Spam
#Spam Ham Spam Ham
#Invalid Syntax