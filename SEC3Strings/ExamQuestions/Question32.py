# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Correct but took me ages
# - - - - - - - Practice Test 1: 3 Strings - - - - - - -
"""
Question 32: Incorrect
What is the output of the following code?

s = '0123456789'
print(s[::2], s[:-2:2], s[2::2])
"""

#i)SyntaxError: invalid syntax
#ii)024680 8 0
#iii)01 01 23
#iv)01 89 23
#v)02468 0246 2468

# Answer: v but need more practice (too slow)




s = '0123456789'
print(s[::2], s[:-2:2], s[2::2])



























# RE: [start:stop:step]yy
#print("s[::2]:", s[::2])        #02468, start at 0, end at 10, skip 2
#print("s[:-2:2]:", s[:-2:2])    #0246, start at 0, end at 10-2=8, skip 2
#print("s[2::2]", s[2::2])       #2468, start at 2, end at 10, skip 2