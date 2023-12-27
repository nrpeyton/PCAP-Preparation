# - - - - - - - SECTION 3: STRINGS - - - - - - -
# - - - - - - - PCAP-31-03 3.3 - Employ built - in string methods

"""
1. Some of the methods offered by strings are:

capitalize() - sets a string to sentence case (capital first letter only);
center() - centers the string inside the field of a known length. Optional fill character must be exactly one character long."""             'abc'.center(10, '#')         """  Output: ###abc####
count() - counts the occurrences of a given character;
find() - returns the index of the first character (leftmost character) of the first occurence of a substring in a string.  Or -1 if not found."""      'string'.find('substring', startInclusive, endExclusive)                     """
rfind() - returns the index of the first character (leftmost character) of the last occurence of a substring in a string:  Or -1 if not found."""      'string'.find('substring', startInclusive, endExclusive)                     """
join() - joins all items of a tuple/list into one string (the INVOKED STRING acts as item SEPERATOR);
lower() - converts all the string's letters into lower-case letters;
lstrip() - removes the white characters from the beginning of the string (or specified adjacent characters);
replace() - replaces a given substring with another;
rstrip() - removes the trailing white spaces from the end of the string (or specified adjacent characters);
split() - splits the string into a substring list using a given delimiter;
strip() - removes the leading and trailing white spaces (or specified adjacent characters);"""                 '?    abc ?'.strip('?')         """ Output: `       abc  `                                                            """"""
swapcase() - swaps the letters' cases (lower to upper and vice versa)
title() - makes the first letter in each word upper-case;
upper() - converts all the string's letter into upper-case letters.

2. String content can be determined using the following methods (all of them return Boolean values):

startswith() - does the string begin with a given substring?
endswith() - does the string end with a given substring?

isalnum() - does the string consist ONLY of letters and digits?
isalpha() - does the string consist ONLY of letters?
islower() - does the string consists ONLY of lower-case letters?
isspace() -does the string consists ONLY of white spaces?
isupper() - does the string consists ONLY of upper-case letters?
isascii() - does the string consist ONLY of ASCII characters?

""""""































































# 3) Find and Replace

someStringWithLength = "I'm just a plain ole plain ole string"
"""
print(f'\nsomeStringWithLength.count("plain"): {someStringWithLength.count("plain")}')

print(f'\nsomeStringWithLength.find("ole"): {someStringWithLength.count("ole")}')
print('someStringWithLength.find("plain"): {someStringWithLength.count("plain", 12)}')

print(f'\nsomeStringWithLength.rfind("ole"): {someStringWithLength.count("ole")}')

print(f'\nsomeStringWithLength.rindex("ole"): {someStringWithLength.index("plain")}')

print(f'\n')
print(' '.join(someStringWithLength))

print(f'\n')
print(someStringWithLength.split(' '))
"""
someListOfRandomNumbers = ['8', '4', '7', '6', '46']
print(f'\nsorted(someListOfRandomNumbers): {sorted(someListOfRandomNumbers)}')

someStringOfRandomNumbers = '847646'
print(f'sorted(someStringOfRandomNumbers): {sorted(someStringOfRandomNumbers)}')
print(f'sorted(someStringWithLength): {sorted(someStringWithLength)}')

someListOfCaseSensitiveNames = ['Mike', 'raph', 'don', 'Leo']
print(f'\nsorted(someListOfCaseSensitiveNames): {sorted(someListOfCaseSensitiveNames)}')
print(f'sorted(someListOfCaseSensitiveNames, key = len): {sorted(someListOfCaseSensitiveNames, key = len)}')
print(f'sorted(someListOfCaseSensitiveNames, key = str.lower): {sorted(someListOfCaseSensitiveNames, key = str.lower)}')

print(f'\nsomeListOfRandomNumbers = :{someListOfRandomNumbers}')
print(f'someListOfRandomNumbers.sort(): {someListOfRandomNumbers.sort()}')
print(f'someListOfRandomNumbers after sort(): {someListOfRandomNumbers}')





