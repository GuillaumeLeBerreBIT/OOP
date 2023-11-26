# Name of class
class Monster: 
    '''A monster that has some attributes'''
    def __init__(self, health, energy):     
        
        self.health = health              
        self.energy = energy       
        
        # Private attributes
        self._id = 5    # By convention can not be changed, should not changed when adding first underscore        

    def attack(self, amount):
        print('The monster has attacked')
        print(f'{amount} damage was dealth')
        self.energy -= 20
        
    def move(self, speed):
        print('The monster has moved')
        print(f'The monster has speed of {speed}')
        

monster = Monster(health = 20, energy = 10)


# Hasattr and Setattr
print(hasattr(monster, 'health'))   # To check if the obejct has the attribute set
if hasattr(monster, 'health'):      # Useful way to check whether a class has a certain attribute
    print(f'The monster has {monster.health} health')
    
setattr(monster, 'weapon', 'Sword') # Can set for an attribute a certain value, which can be printed
print(monster.weapon)
# This can be used to set lots of new attributes
new_attributes = (['weapon', 'Axe'], ['armor', 'Shield'], ['potion', 'Mana'])

for att, val in new_attributes:
    setattr(monster, att, val)

print(vars(monster))

# Doc
print(monster.__doc__)  # This prints u-out the docstring of the object, can be usefull for very long texts on a class. Working on big projects 
help(monster)   # Can see the attributes, Docstring ad methods
#help(str)  # Can use it on functions to print out