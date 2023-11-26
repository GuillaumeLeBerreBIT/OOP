class Monster: 
    # Keyword unpacking = After knowing all the parameters definitly need
    # Any argument I get after the parameters going to store those in a seperate dictionary
    def __init__(self, health, energy, **kwargs):     
        #print(kwargs)   # {'speed': 120, 'has_scales': False}
        self.health = health              
        self.energy = energy    
        # DUE TO ORDER OF MRO FISH COMES AFTER MONSTER NEED TO CALL INIT IN THE MONSTER CLASS!!!!!!
        #super().__init__(speed = 75, has_scales = False) 
        super().__init__(**kwargs)  # Calling the star again turns each Key - Value pair inside of this dictionary {'speed': 120, 'has_scales': False} 
                                    # into a named argument >> Passing into the init method of next class in the MRO 

    def attack(self, amount):
        print('The monster has attacked')
        print(f'{amount} damage was dealth')
        self.energy -= 20
        
    def move(self, speed):
        print('The monster has moved')
        print(f'The monster has speed of {speed}')
        
class Fish:   
    
    def __init__(self, speed, has_scales, **kwargs):  # Calling init method & parsing the arguments we want to set >> speed, health and energy 
        #print(kwargs) # Empty since no kwagrs neede for now
        self.speed = speed
        self.has_scales = has_scales
        super().__init__(**kwargs)  # Just add it for incase another inheritance is added
    
    def swim(self):
        print(f'The fish is swimming at a speed of {self.speed}')
        
class Shark(Monster, Fish): # Here can ad as many classes as you want
    # Call the init method after calling class & Py knows first item of inheritance Monster then Fish
    # Call speed & has_scales need >> Keyword unpacking
    def __init__(self, bite_strength, health, energy, speed, has_scales):
        # Using ** Python expecting keyword arguments 
        super().__init__(health = health, energy = energy, speed = speed, has_scales = has_scales)
        # Now speed and has_scales does not exist since calling the Monster class as inheritance but not Fish >> Need to call __init__ from Fish
        
        self.bite_strength = bite_strength
        
# Calling the class        
shark = Shark(bite_strength = 50,
              health = 200, 
              energy = 25,
              speed = 120,
              has_scales = False)        
        
#shark.attack(10)
#print(shark.bite_strength)     
#print(shark.has_scales) 
print(shark.speed)   

# Need to look at the order of the init methods are called >> Traceback the order 


# MRO -- > Method of Resolution Order == What order the PARENT init methods are being called
#print(Shark.mro())  # [<class '__main__.Shark'>, <class '__main__.Monster'>, <class '__main__.Fish'>, <class 'object'>] >> Last object inbuild do ot worry
# Left most item is always the first being called && Next 2 classeds is the order being given in class Shark() arguments ^^^^ 