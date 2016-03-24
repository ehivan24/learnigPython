'''
Created on Jan 12, 2015

@author: edwingsantos
'''

class Animal(object):
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0
    
    
    def setName(self, name): #setter
        self.__name = name
        
    def getName(self): #getter
        return self.__name
    
    def setWeight(self, weight): #setter
        self.__weight = weight
        
    def getWeight(self): #getter
        return self.__weight
    
    def setHeight(self, height): #setter
        self.__height = height
        
    def getHeight(self): #getter
        return self.__height
    
    def setSound(self, sound): #setter
        self.__sound = sound
        
    def getSound(self): #getter
        return self.__sound
    
    
    def getType(self):
        print("Animal") 
        
    def toString(self):
        return "{} is {} cm tall and {} kgs and say {}".format(self.__name, self.__height,self.__weight,self.__sound)

    def __init__(self, name, height, weight, sound):
        '''
        Constructor
        '''
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound
        
        
cat = Animal("Wiskers", 33, 20, "Meow")
print cat.toString()



class Dog(Animal):
    __owner = None
    
    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        
        super(Dog, self).__init__(name, height, weight, sound)
        
    def setOwner(self, owner):
        self.__owner = owner
            
    def getOwner(self):
        return self.__owner
        
    def getType(self):
        print("Dog")
        
    def toString(self):
        return "{} is {} cm tall and {} kgs and say {} his owner {} ".format(self.__name, self.__height, self.__weight, self.__sound, self.__owner)
             
            

spot = Dog("spot", 53, 27, "ruff", "Amy")

print "Height: " , spot.getHeight()  
print "Name: " , spot.getName()
print "Owner: ", spot.getOwner()
print "Weight: ", spot.getWeight()
print "Sound: ", spot.getSound()



print "Type: ", spot.getType()