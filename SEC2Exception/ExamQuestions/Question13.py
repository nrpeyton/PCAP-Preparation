# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -

"""
What is the output of the following code?

for x in range(1):
    try:
        print(x/x)
    finally:
        break
"""
for x in range(1):
    try:
        print(x/x)
    finally:
        break

# ZeroDivisionError: division by zero
# 0
# 1
# No output