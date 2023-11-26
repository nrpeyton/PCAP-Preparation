# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - CORRECT WITH CHECK
# - - - - - - - Practice Test 2: 3 Strings - - - - - - -
"""
Question 5: Incorrect
What is the output of the following code?

t = "Spam Ham"
print(t.rfind("am") == t.find("am"))
print(t.rfind("am", 3) == t.find("am", 3))
print(t.rfind("am", -3) == t.find("am", -3))
"""


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#True True True
#False False False
#False True True
#True will be printed followed by TypeError: rfind takes 1 argument (2 given)

# Answer: 3 but need to check how rfind works



t = "Spam Ham"
print(t.rfind("am") == t.find("am"))
print(t.rfind("am", 3) == t.find("am", 3))
print(t.rfind("am", -3) == t.find("am", -3))