# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Incorrect
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -

"""
What is the output of the following code?

for x in range(1):
    try:
        print(x/x)
    finally:
        continue
"""


#No output
#ZeroDivisionError: division by zero
#0
#1

# Answer: No output


# Notes: Python stops on ZeroDivisionError but jumps to finally; normally returning to the stop point, however 'continue' stops the current iteration, 
# bypassing the stop.  Normally, we would continue the next iteration, but since there are no loops left, the program simply ends with no output.