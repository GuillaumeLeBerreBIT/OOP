# Inheritance means that 1 class gets attributes and methods from another class (or classes)
# Have Monster == Health, Energy, Attack and Move == Parent 
# Shark = Speed, Bite == Child
# Want Shark == Health, Energy + SPeed, Attack + Bite, Move as well == Object 
# This makes it easy to reuse code
# Class can inherit from an unlimited number of other classes
# & Class can also be inherited from an unlimited number of classes
#

# Name of class
class Monster: 
    
    def __init__(self, health, energy):     
        
        self.health = health              
        self.energy = energy               

    def attack(self, amount):
        print('The monster has attacked')
        print(f'{amount} damage was dealth')
        self.energy -= 20
        
    def move(self, speed):
        print('The monster has moved')
        print(f'The monster has speed of {speed}')
        
# If u want inherit from another class Add as argument in class
# To call Attributes need to call the __init__() FIRST!!
class Shark(Monster):   # Gets all Attributes and Methods from Monster
    
    def __init__(self, speed, health, energy):  # Calling init method & parsing the arguments we want to set >> speed, health and energy
        # Can use the arguments to call the health & speed from PARENT Class
        # Passing 3 arguments which here SELF now refers to the __init__ from here which is the Shark itself & 2 ARGUMENTS for Monster __init__
        #Monster.__init__(self, health, energy)  
        # Same method
        super().__init__(health, energy) # This gets the PARENT CLASS AND MUCH MORE USED ESPECIALY WITH COMPLEX INHIRITENCE!!
        #super().move(speed = 10)    # Can still call the MOVE method from the PARENT >> When calling init from Shark, still calling move method from PARENT 
        self.speed = speed
        
    def bite(self):
        print('Shark has bitten')
    
    # Can overwrite the speed from the parent class by overwriting the Method from PARENT >> Using the same name in the Child CLASS!!!
    def move(self):
        print('The shark has moved')
        print(f'The speed of the shark is {self.speed}')

# Creating the object can now use all 
# Shark method has now 3 arguments which last two are inhireted from the Monster
shark = Shark(speed = 120, health = 100, energy = 80)
#shark.attack(30)
print(shark.speed)
print(shark.health)
print(shark.energy)

# Exercise
# Create a scorpion class that inherits from monster
# Health, Energy from the parent
# poison_damage attribute
# Overwrite the damage method to show poison damage

class Scorpion(Monster):
    
    def __init__(self, poison_damage, scorpion_health, scorpion_energy):
        # Inherit the attributes from the Monster class
        # Here do not sert parameters as an attribute >> Using the Monster attributes and giving the health from arguments
        super().__init__(health = scorpion_health, energy = scorpion_energy)
        self.poison_damage = poison_damage
        
    def attack(self):
        print('Scorpion has poisend oppenent')
        print(f'Amount of damaga dealth {self.poison_damage}')

scorpion = Scorpion(poison_damage = 50, 
                    scorpion_health = 20, 
                    scorpion_energy = 10)
# It now calls the attack method from the Scorpion class
scorpion.attack()
# Still uses the same move mechanic from the monster class
scorpion.move(5)

