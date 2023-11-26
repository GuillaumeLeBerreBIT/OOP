# Name of class
class Monster:      # -- > Global scope
    
    # When class is created want to have custom variables 
    #health = 90     # -- > Global variables
    #energy = 40
    
    def __init__(self, health, energy):         # Can give parameters to the dunder method
        print('The monster was created')
        
        # self.health refers to health from class && health refers to argument parsed
        self.health = health                # Can set the health the parameter parsed in when object is called
        self.energy = energy                # CAN CREATE THE ATTRIBUTE INSIDE HERE DO NOT NEED THEM ABOVE ANYMORE
    
    def __len__ (self):
        return self.health      # Can use when calling len() function to see amount of health >> len(monster1) >> Will give health of monster
    
    def __abs__ (self):
        return self.energy      # Same principle 
    
    def __call__(self):             # Create a function when calling the variable the object is stored in == monster1()
        print('The monster was called')
        
    def __add__(self, other):
        return self.health + other
    
    def __str__(self):              # When printing the variable return a string instead of memory adress
        return f'Monster health: {self.health}, Energy: {self.energy}'
    
    # Methods
    # Whenever method called -- > Python automatically passes a reference to the class as the first argument in this Method
    # FIRST PARAMETER == REFERENCE TO THE CLASS ITSELF, then following arguments can be used as normal function
    # FIRST PARAM allows to influence variables outside this function
    def attack(self, amount):
        print('The monster has attacked')
        print(f'{amount} damage was dealth')
        self.energy -= 20
        print(self.energy)   # This is looking on the FIRST ARGUMENT it gets, thus reference of the class itself  -- > From there can get Energy
        # If this was local function monster.energy would not work because would create a local variable would not work with the global ones

    def move(self, speed):
        print('The monster has moved')
        # Print how the monster has moved at certain speed
        print(f'The monster has speed of {speed}')
        
# The 'self' from attack and move have no corelation (no conflict) BUT thyey both reference the Monster class. Self is used as convention
    
#monster = Monster()   # Turned class into object saved in a method
#print(monster.health)   # Can only find that variable in the Class, Scope of monster Class
#monster.attack(40)
# Movement of monster
#monster.move(30)

# All have same amount of Health, Energy, Attack and Move BUT want to change Health and Energy 
monster1 = Monster(health = 10, energy = 20)    # Everytime creating a monster calling Dunder method __init__
monster2 = Monster(50, 100)                     

print(monster1.health)
print(monster2.health)

# Can print the diretory listing of class -- > Returns all dunder methods, attributes and normal methods
print(dir(Monster))
# Attribute!!! --> Gives all of the attributes of a method inside a dictionary
print(monster1.__dict__)
print(vars(monster1))
# Can print when __call__
print(monster1())
# Health of monster1 is added to its current one
print(monster1 + 55)
# When printing if __str__ it will no longer show the memory address of that isntance but string want to return and its values
print(monster1)



############################## OOP ##############################
# What are objects?
# -- > An MONSTER OBJECT is a container for VARIABLES (health, energy, stamina, ...) and FUNCTIONS (attack, movement, animations, ...)
# The variable is only existent in the container
# Altough have special names
# VARIABLES in an object are called ATTRIBUTES
# FUNCTIONS are called METHODS
#
# Can have multiple objects -- > 3 monsters with different health, energy levels aka VARIABLES
# But this does not apply for METHODS -- > All for instance Attack, Move
# Each object has its own Attributes and Methods && Methods are not the same because they reply to their respective Object
# 
# Can have Mosnter 3 interact with Mosnter 2 and reduce the health -- >> Object-Oriented Programming - OOP == Organizing code via different objects
# 
# Monster 2 Attacks Monster 1 (Method) which reduced the health Monster 1 and Energy of Mosnter 2 (Variables)
# Can also have obstacle with POS and SIZE && All other Monsters and Players have move method which can interact with the Obstacle
# Player can be parsed as One attribute in the Menu, Can add function/object inside another object as an attribute -- > Select change weapon
# -- > OBJECTS INTERACT WITH EACH OTHER
# 
# What are Classes? A blueprint for an object == Creating an object we need a CLASS ++ Class can accept arguments to customise the object
# 
# Class -- > Health, Energy (Variables) not being set which is done when the class is used to create an object
#            Also has 2 methods Attack, Move
#            -- > Use the class to create OBJECT and in the process giving specific values for Health, Energy
# 
# Class can inherit from another class == OBJECT have Attributes and Methods from both classes
# Monster class with Health, Energy, Attack and Move can be given to a class Shark with only Speed (A), Bite (M) and inherit those Attributes and Methods
#
############################## __Dunder__ (Double Underscore) METHODS ##############################
# 
# Is not callable by the user -- > Called by python when somethiong is happening
# __init__ is called when the object is created -- > IMPORTANT
# __len__ called when object is passed into len()
# __abs__ called when object is called into abs()
# 
