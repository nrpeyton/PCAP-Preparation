#                                                       r a n d o m ( )
from random import random, randrange, randint
print(random()) # Returns a float betwen 0 and 1.





#                                                       r a n d r a n g e ( )

# random.randrange([start=0], stop [, step=1]) # Returns a randomly selected integer from the specified range (stop exclusive).

random.randrange(0, 10, 2) # Despite start's default, start MUST be included IF using a step.







#                                                       r a n d i n t ( )

randint(start, stop+1) # This method is an alias for randrange(start, stop+1).