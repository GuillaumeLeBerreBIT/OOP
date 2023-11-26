# Every method has a refrence to the class it is easy to get and change class attributes
# Because of that methods rely much less on parameters, global and return (altough you can use it)
# Objects can be influence from the outside and from a lcoal scope of a function

# Scope problem
def update_health(amount):
    monster.health += amount
#
#
#health = 10
#print(health)
#update_health(20)
#print(health)

class Monster:
    
    def __init__(self, health, energy): # Passing it inside another method inside monster class
        self.health = health
        self.energy = energy
        #self.energy = self.set_energy(energy) #To the method down below (1)
        #self.set_energy(energy)     # (2)
        
    def update_energy(self,amount): # This is an easy way to work with scope >> Target attribute and set it to a new value or update whatever you want
        self.energy += amount
    
    def get_damage(self, amount):
        self.health -= amount
        
    #def set_energy(self, energy): 
    #    new_energy = energy * 2 # Doubling and assign to new lcoal variable
    #    #return new_energy       # Returning new energy >> Becomes attribute self.energy (1)
    #    #self.energy = new_energy    # (2)

# Create a HERO class with 2 parameters: damage, monster
# 1. The monster class should have a method that lowers the health -> get_damage(amount)
# 2. The hero class should have an attack method that calls the get_damage method from the monster
# 3. The amount of damage is hero.damage

class Hero:
    
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster
    
    def attack(self):
        self.monster.get_damage(self.damage)
        
# Creating the monster object     
monster = Monster(health = 100, 
                  energy = 50)

# Creating the Hero object 
hero = Hero(damage = 30, 
            monster = monster)

# Health still same
print(monster.health)
# Call the attack function >> Health drops
hero.attack()
print(monster.health)


monster.health += 20
print(monster.health)

update_health(20)       # Even inside a local scope of an function can update anything inside an object
print(monster.health)
# Can use the object to call the function
monster.update_energy(20)
print(monster.energy)

