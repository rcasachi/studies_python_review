s = """w'o"w"""
repr(s) # Output: '\'w\\\'o"w\''
str(s) # Output: 'w\'o"w'
# eval(str(s)) == s # Gives a SyntaxError
eval(repr(s)) == s # Output: True

import datetime
today = datetime.datetime.now()
str(today) # Output: '2016-09-15 06:58:46.915000'
repr(today) # Output: 'datetime.datetime(2016, 9, 15, 6, 58, 46, 915000)'

# Overriding in class
class Represent(object):
    
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __repr__(self):
        return "Represent(x={},y=\"{}\")".format(self.x, self.y)
    
    def __str__(self):
        return "Representing x as {} and y as {}".format(self.x, self.y)

r = Represent(1, "Hopper")

print(r) # prints __str__
print(r.__repr__) # prints __repr__: '<bound method Represent.__repr__ of Represent(x=1,y="Hopper")>'

rep = r.__repr__() # sets the execution of __repr__ to a new variable
print(rep) # prints 'Represent(x=1,y="Hopper")'

r2 = eval(rep) # evaluates rep
print(r2) # prints __str__ from new object
print(r2 == r) # prints 'False' because they are different objects
