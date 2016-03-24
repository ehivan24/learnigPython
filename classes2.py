'''
Created on Jan 15, 2015

@author: edwingsantos
'''

if __name__ == '__main__':
    pass

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.armor = 5
        
    def food(self, food):
        if (food == "apple"):
            self.health -= 20
            self.armor -= 3
        elif (food == "tuna"):
            self.health += 20
            self.armor += 2
        else:
            self.health += 1
        

Bob = Hero("Peter")

print Bob.name
print Bob.health
print Bob.armor

Bob.food("apple")
print Bob.health

print Bob.armor
Bob.food("tuna")
print Bob.health
Bob.food("tuna")
print Bob.health
print Bob.armor


            
            
        
            
        