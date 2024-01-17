"""
Challenge: Squares of Even Numbers
"""

#  <expression>  <for outer_elem in outer_list>  <if condition>

evens_squared = [i*i for i in range(0, 10) if i % 2 == 0]
print(evens_squared)

evens_squared = [i**2 for i in range(0, 10) if i % 2 == 0] # i*i is exactly the same as i**2
print(evens_squared)






"""
Challenge: Reverse Strings
Given a list of strings, use list comprehension to create a new list containing the reverse of each string. For example, from ["abc", "def", "ghi"],
the result should be ["cba", "fed", "ihg"].
"""

ls = ['abc', 'def', 'ghi']


lcompr = [e[::-1] for e in ls] # [ <expression>  <for e in iterable> ]
print(lcompr)

# The ONLY iterables list.methods() can be used on are lists.  For strings, we can use slices.
# Slice notation is "syntactic sugar" for creating and using slice objects, which can be used with: slice(0:11:2); list.__getitem__(slice).  We could even override __getitem__ to change slice notation's behaviour.



"""
Challenge: Square of Odd Indices
Given a list of numbers, use list comprehension to create a list containing the square of each number that is in an odd index in the original list. 
For instance, with [1, 2, 3, 4, 5], the result should be [4, 16] (squares of 2 and 4, which are at indices 1 and 3).
"""

l = [1, 2, 3, 4, 5]
nl = [e**2 for e in l if l.index(e) % 2 == 1]
print(nl)


nl = [e**2 for i, e in enumerate(l) if i % 2 == 1]




"""
Challenge: Divisible by Five
Create a list using list comprehension that contains all numbers from 1 to 100 that are divisible by 5.
"""

l3 = [e for e in range(1, 101) if e % 5 == 0]
print(l3)




"""
Challenge: Uppercase Words
Given a sentence, use list comprehension to create a list of words in the sentence that are in uppercase. For example, from "Hello World, I am LEARNING Python", the result should be ["HELLO", "WORLD", "I", "AM", "LEARNING"].
"""
st = "Hello World, I am LEARNING Python"
l4 = [word for word in st.split() if word.isupper() == True]
print(l4)





"""
Challenge: Extract Digits
Given a string containing a mix of letters and numbers, use list comprehension to create a list of all numeric characters in the string. For instance, with "Python 3.8.5", the result should be ['3', '8', '5'].
"""

st = "Python 3.8.5"
l5 = [c for c in st if c.isnumeric()]
print(l5)








"""
Challenge: Flatten the matrix into a simple list
"""

#  <expression>  <for outer_elem in outer_list>  <for inner_elem in outer_elem>

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [elem for list in matrix for elem in list]
print(flattened)







"""
Challenge: Replace numbers in the list with with 'small', 'medium' or 'large' depending on their value.
"""

#  <expression>  <for elem in iterable>

numbers = [5, 15, 25, 35, 3, 12, 2]
sized = ['Small' if n < 10 else 'Medium' if n < 20 else 'Large' for n in numbers]
print(sized)

True if 1 == 1 else False # This ternary conditional is an expression (expressions are, or evaluate to, a value); where as the standard 'if' conditional is only a statement (statements are assignments and standard 'for' loops, they have side effects and don't evaluate to anything purely on their own).








"""
Challenge: You are given a list of strings representing various colors: ["red", "green", "blue", "yellow", "pink", "black", "white"]. 
Your task is to create a new list that contains only those colors whose names have more than four letters. 
"""

#  <expression>  <for elem in iterable>  <if condition>

colours = ["red", "green", "blue", "yellow", "pink", "black", "white"]
long_named_colours = [colour for colour in colours if len(colour) > 4]
print(long_named_colours)










#           M A T R I X   T R A N S P O S I T I O N

""" Challenge: Transpose this matrix. The transposed matrix should be a list of lists where the rows are turned into columns. """

matrix = [[1, 2, 3], [4, 5, 6]]

"""
    Column1  Column2  Column3
Row1    1       2       3
Row2    4       5       6

"""



# Two illustrations showing the SAME transposition of the above matrix:
"""
          Row1    Row2    Row3
Column1    1       2       3
Column2    4       5       6

        Column1  Column2
Row1        1       4
Row2        2       5
Row3        3       6
"""



transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed) # Output: [[1, 4], [2, 5], [3, 6]]


"""         EXECUTION STEPS:

1. outer loop: i = 0
2. inner loop: first row; first col
3. inner loop: second row; first col

4. outer loop: i = 1
5. inner loop: first row; middle col
6. inner loop: second row; middle col

7. outer loop: i = 2
8. inner loop: first row; last col
9. inner loop: second row; last col
"""


"""         EXECUTION STEPS (LONG VERSION):

1. Start with the matrix: [[1, 2, 3], [4, 5, 6]]

2. Initialize the outer loop (i): 
   - The range for 'i' is 0 to 2 (inclusive of 0 and exclusive of 3).

3. Outer Loop - First Iteration (i = 0):
   - Inner Loop - First Row: Extract the 0th (first) element from the first row (1).
   - Inner Loop - Second Row: Extract the 0th (first) element from the second row (4).
   - Resulting List for this Iteration: [1, 4].

4. Outer Loop - Second Iteration (i = 1):
   - Inner Loop - First Row: Extract the 1st (middle) element from the first row (2).
   - Inner Loop - Second Row: Extract the 1st (middle) element from the second row (5).
   - Resulting List for this Iteration: [2, 5].

5. Outer Loop - Third Iteration (i = 2):
   - Inner Loop - First Row: Extract the 2nd (last) element from the first row (3).
   - Inner Loop - Second Row: Extract the 2nd (last) element from the second row (6).
   - Resulting List for this Iteration: [3, 6].

6. Combine the Resulting Lists from Each Iteration to Form the Transposed Matrix:
   - The transposed matrix is [[1, 4], [2, 5], [3, 6]].
   - The rows of the original matrix have become columns in the transposed matrix.

"""







# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


"""
TASK:
Write a Python function that takes a list of strings and returns a new list containing every word from the strings in the original list, but only 
if the word contains at least one vowel (a, e, i, o, u). 
"""


# This does the same as the snippet below it.

def words_with_vowels(strings):
    vowels = 'aeiou'
    words = ' '.join(strings).split()
    return [word for word in words if any(v in word.lower() for v in vowels)]

# Example usage
print(words_with_vowels(["Cats and dogs", "Mysterious shadows", "Nymph, crypt, myth"]))
# Expected output: ['Cats', 'and', 'dogs', 'Mysterious', 'shadows']

#                                                                                                                                                      "I want a word for each word in word list if vowel in word for each vowel in vowels"




# Over-complicated and too verbose (keeping here as a reminder r.e. the improvement above)!
def words_with_vowels(strings):

    letter_list = [c for c in str(strings) if c.isalpha() or c == ' ']
    wordlist = ''.join(letter_list).split()
    
    # ----
    
    def filter_func(wordlist):
        vowels = 'aeiou'
        filtered_strings = []
        
        for word in wordlist:
            word_checklist = []
            for v in vowels:
                if v in word:
                    word_checklist.append(True)
                else:
                    word_checklist.append(False)
            if any(word_checklist) == True:
                filtered_strings.append(word)
        
        return filtered_strings
    
    # ----
    
    return filter_func(wordlist)

# Example usage
print(words_with_vowels(["Cats and dogs", "Mysterious shadows", "Nymph, crypt, myth"]))
# Expected output: ['Cats', 'and', 'dogs', 'Mysterious', 'shadows']

# REMEMBER PARENTHESIS ON CALLS



# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =









"""
Another list comprehension: 
Write a Python function that uses a list comprehension to create a list of dictionaries based on the given data. 
Each dictionary should represent a person and contain two keys: name and age.
"""

def create_people(names, ages):
    return [dict(Name = names[i], Age = ages[i]) for i in range(len(names))]

# Example usage
people = create_people(["Alice", "Bob", "Charlie"], [25, 30, 35])
print(people)
# Expected output: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 35}]









"""
Challenge: Advanced List Comprehension
Task: Write a list comprehension to generate a list of tuples. Each tuple should contain a number from 1 to 30 and its square, but only include numbers 
whose square is divisible by 3.
"""

list_of_tuples = [(i, i*i) for i in range(1, 30+1) if i*i % 3 == 0]
print(list_of_tuples)








"""
Challenge: Lambda with Complex Data Types
Task: Create a lambda function that takes a list of dictionaries (each dictionary represents a person with 'name' and 'age' keys) and returns a new list 
of names of people who are 18 or older.
"""

dicts = [dict(Name='Bob', Age=20), dict(Name='Charlie', Age=41), dict(Name='Lidia', Age=19), dict(Name='Laura', Age=18), dict(Name='Alan', Age=55), dict(Name='Zac', Age=16), dict(Name='Alice', Age=17)]

# Using lambda
over_18_names = [dic['Name'] for dic in filter(lambda dic: dic.get('Age') >= 18, dicts)]
print(over_18_names)

# Without lambda
over_18 = [dic.get('Name') for dic in dicts if dic.get('Age') >= 18]
print(over_18)











