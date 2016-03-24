'''
Created on Jan 15, 2015

@author: edwingsantos
'''

if __name__ == '__main__':
    pass

'''

try:
    x = 5  + 'ham'
except:
    print 'dam it'
    
try:
    x = 5 + 'ham'
except:
    pass

#raise TypeError('Error')



try:
    
    x= 5 +'ham'
except ZeroDivisionError:
    print "will not see this"
finally:
    print 'final error' 
'''
        
def doesNothing():
    pass
    
def makeOne():
    return 1

def addTen(myInt):
    myInt + 10
    return myInt


def myFunc():
    """
        I doc something
    """
    
    #commenting
    pass




print myFunc()

x1 = 12
print dir()

y = addTen(x1)
print x1 ,y

doesNothing()
    
x = makeOne()
print x



high = 10
ans = 7

guess =  raw_input("guess a number: from 0 to %d " %high)

while(int(guess) != ans):
    if(int(guess) < ans):
        print "higher"
    else:
        print "lower"
    guess = raw_input("guess a number: from 0 to %d " %high)

print "Winner"





