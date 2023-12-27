class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        if self.pages >= 250:
            return True
        else:
            return False

    def __str__(self):
        return self.title + ' by ' + self.author + ', ' + str(self.pages) + ' pages'

# Example usage
my_book = Book("1984", "George Orwell", 328)
print(my_book)  # Should print: 1984 by George Orwell, 328 pages
print(my_book.is_long())  # Should print: True










class Vehicle:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def get_description(self):
        return str(self.year) + ' ' + self.make + ' ' + self.model

class Car(Vehicle):
    
    def __init__(self, make, model, year, is_electric):
        super().__init__(make, model, year)             # alternative way:      Vehicle.__init__(self,  make, model, year)       
        self.is_electric = is_electric
        
    def get_description(self):
        if self.is_electric:
            return super().get_description() + ' ' + '(Electric)'
        else:
            return super().get_description() + ' ' + '(Gas)'

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def get_description(self):
        if self.has_sidecar:
            return super().get_description() + ' ' + '(Sidecar)'
        else:
            return super().get_description()


# Example usage
car = Car("Tesla", "Model S", 2020, True)
print(car.get_description())  # Expected: 2020 Tesla Model S (Electric)

motorcycle = Motorcycle("Harley-Davidson", "Roadster", 2019, False)
print(motorcycle.get_description())  # Expected: 2019 Harley-Davidson Roadster


# MAJOR MISTAKES/THINGS FORGOTTEN:
# Forgot to pass args to super() when initialising an object with a combination of inherited and non-inherited attributes:
#   Rules are: The subclass's __init__ method still requires parameters even for inherited instance attributes.  They are passed to the superclass via super's arguments

# MINOR MISTAKES/TYPOS:
# Forgot 'self' prefix when using method attributes
# Forgot to change int to str when returning int based attributes
# Forgot parenthesis when calling methods

# STANDARDS:
# Boolean conditionals can be simplified.
"""                             C H A L L E N G E

Base Class - Vehicle:
-Attributes: make (string), model (string), year (integer).
-Constructor: Initialize the attributes.
-Method: get_description, which returns a string in the format: "Year Make Model".

Subclass - Car:
-Inherits from Vehicle.
-Additional Attribute: is_electric (boolean).
-Constructor: Initialize inherited attributes and is_electric.
-Override Method: get_description to include information about whether the car is electric. Format: "Year Make Model (Electric)" or "Year Make Model (Gas)" depending on the is_electric attribute.

Subclass - Motorcycle:
-Inherits from Vehicle.
-Additional Attribute: has_sidecar (boolean).
-Constructor: Initialize inherited attributes and has_sidecar.
-Override Method: get_description to include information about whether the motorcycle has a sidecar. Format: "Year Make Model (Sidecar)" or "Year Make Model".
"""









