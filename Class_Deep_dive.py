############################## Python and Classes ##############################
# function and method both execute a block of code
# Difference is METHOD belongs to an object 
# Function == len('test) -- > works with dict, list, string
# Method == 'test'.upper() -- > Only works with str

test_v = 'a'
# __len__ is called when parsing string into len function
print(dir(test_v))    # Will give Dunder methods, Attributes and Normal methods -- > Can call all those objects

def test():
    pass

# This object is special because of __call__ method -- > When adding brackets it will execute
print(dir(test))
# FUNCTION == Object with the Dunder __call__ method (with extra things)

# Can store function inside variable == Function is an object
a = test
a.another_attribute = 10 

print(dir(a))   # Function has then another attribute


# More common
# Here creating an object of a function -- > Can pass around the object for instance to Test class
def add(a,b):
    return a + b

class Test():
    
    def __init__(self, add_function):
        self.add_function = add_function    # Can here store the function inside an attribute 
        
# Can parse the object wich is a function        
test_c = Test(add_function = add) # Not use brackets want to get the function itself, the object of the function

 
print(test_c.add_function(3,4)) # Here can the attribute from outside the function


## EXERCISE
# Create a monster class with a parameter called func, store this func as a parameter

class Monster():
    
    def __init__(self, func):
        # Turn the parameter into an attribute
        self.func = func    

# Create another class, called Attacks, that has 4 methods:
# Bite, strike, slash, kick (each method should print some text)
        
class Attacks():
    
    def bite(self):
        print('Monster has bitten')
    
    def strike(self):
         print('Monster has striked')
    
    def slash(self):
         print('Monster has slashed')
    
    def kick(self):
         print('Monster has kicked')
     
# Want to create an monster object and give it one of the attack methods from the attack class        
monster = Monster(func = Attacks().slash)   # Attacks is returning a class -- > turn it into object with () -- > From this object get the bite method
monster.func()
# Alternatively
attacks = Attacks()
monster = Monster(func = attacks.bite)   
monster.func()

