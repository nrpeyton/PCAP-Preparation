# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - - Incorrect
# - - - - - - - Practice Test 1: 3 Strings - - - - - - -
"""
Question #35: INCORRECT
which of the calls below are valid String function calls and will return True?
"""
#1)'Abc'.istitle()
#2)'123abc'.islower()
#3)'abc'.isalpha()
#4)'123'.isdigit()
#5)'123abc:'.isidentifier()
#6)'abc123'.isalnum

print("'Abc'.istitle(): ", 'Abc'.istitle())
print("'123abc'.islower(): ", '123abc'.islower())
print("'abc'.isalpha(): ",'abc'.isalpha())
print("'123'.isdigit(): ", '123'.isdigit())
print("'123abc:'.isidentifier(): ", '123abc'.isidentifier())
print("'abc123'.isalnum: ", 'abc123'.isalnum() )

# Answer: All true except 5.  In Python, only identifiers can be used as names.  Names can contain numbers, letters, and underscores, but cannot start with a number.