# The Operating System generates an error code as an integer, i.e., '2' which is passed to Python.  Python translates this into an exception.
# Therefore we can not add arguments to organic exceptions in the same way we can when raising an exception manually.
# For organic exceptions, Python creates or fills the e.errno variable and e.args tuple automatically based on the "organic" error.  
# For example, below we print the e.args tuple:

try:
    open('non_existant_file.txt', 'r')
except FileNotFoundError as e:
    print(e.__str__(),      e,      str(e),      sep='   ') # Output: [Errno 2] No such file or directory: 'non_existant_file.txt'   [Errno 2] No such file or directory: 'non_existant_file.txt'
    print()
    print(e.errno) # Output: 2
    print()
    print(e.args) # Output: (2, 'No such file or directory')






# We can also use the os.strerror function to translate the error code '2' integer stored in e.errno to a brief description of the error.
# This may not be necessary as Python already did this translation above when receiving the '2' error from the Operating System, however it does provide it as a convenient string.      Bonus: The function could also still be valuable when dealing with lower-level operations or when you have an error code and need to programmatically convert it to a message.
    from os import strerror
    print('\n' * 5)
    print(strerror(e.errno)) # Output: No such file or directory

""" Output:

[Errno 2] No such file or directory: 'non_existant_file.txt'   [Errno 2] No such file or directory: 'non_existant_file.txt'

2

(2, 'No such file or directory')






No such file or directory
"""