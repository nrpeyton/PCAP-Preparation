from random import sample, randrange

class Filer:
    sentence = ['sample', 'takes', 'a', 'and', 'returns', 'list']
    def write(self, mode, lines_to_add):
        file = open('text.txt', mode)
        for i in range(lines_to_add):
            # Add a line to file consisting of a random sized sample of 'sentence'.
            sentence_sample = sample(Filer.sentence, k=randrange(len(Filer.sentence)+1)) 
            sentence_sample_st = ' '.join(sentence_sample) + '\n'
            file.write(sentence_sample_st)
        file.close()

lines_to_add = 1 # Change number of lines to add
mode = 'a' # Change mode: write or append



class Reader(Filer):
    def all_per_line(self):
        self.st = ''
        for l in open('text.txt', 'r'):
            self.st+= l
    

    def all_at_once(self):
        file = open('text.txt', 'r')
        self.st = file.read()
        file.close()
    
    def one_line(self):
        file = open('text.txt', 'r')
        self.st = file.readline()
        file.close()

    def few_lines(self):
        file = open('text.txt', 'r')
        self.st = ' '.join(file.readlines(200)) # Hint = 200 bytes.  After 200 bytes is reached, no further whole lines will be read.


    def __str__(self):
        return self.st

f = Reader()
f.write(mode, lines_to_add)
f.all_per_line()
f.all_at_once()
f.one_line()
f.few_lines()
print(f)









"""MISTAKES:
-Incorrectly tried to use 'f' for both the name of an instance (of the reader class) and the open() object simultaneously.
-Tried to call close() on 'f' when it wasn't even a file object.  When iterating over an open() object directly, for example: `for l in open('text.txt', 'r'):`, we're only creating an unnamed, or "anonymous", file object.
-Class variables to instances/objects are 'class.variable', not just 'variable'.   In other words, even if referring to a class variable inside a method of the same class, we still need to refer to it as 'class.variable' not just 'variable'.
"""