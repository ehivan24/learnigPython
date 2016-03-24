'''
Created on Jan 9, 2015

@author: edwingsantos
'''

if __name__ == '__main__':
    pass

import random
import sys 
import os



    
def addNumbers(fNum, sNum):
    sumNum = fNum + sNum
    
    return sumNum
    
print ('fNum =')
    
fNumr = 2323 #sys.stdin.readline()
print ('sNum = ')
sNumr = 12344 #sys.stdin.readline()



#int(fNumr)
print ("%s %s %.3f" % (fNumr, sNumr, 1.34837))    

print (addNumbers(5, 6))


grocery =['apples','bananas','grapes','juice','milk']

print grocery[0]

grocery[0] = 'soup'

print grocery[0]

print grocery[1:]

grocery2 = ['bread','water','dogs','fish','cats']

new = [grocery,grocery2]

grocery.append('onions')

grocery.insert(0, 'pickle')

grocery2.remove('dogs')

grocery.sort()
print grocery
print new

print new[1][0:2]


print len(grocery)

print max(new)
print min(new)

piTuple = (3,3,4,1,2,4,5)
newTuple = list(piTuple) 

print len(piTuple)

print newTuple
print piTuple


dictinary = {"batman":"bruce","Superman":"ken","Spiderman":"peter"}

print dictinary

print dictinary.get("batman")

print len(dictinary)
print max(dictinary)

print min(dictinary)

dictinary['Spiderman'] = 'New PeterParker'

print dictinary

print dictinary.keys()

print dictinary.values()

for values in dictinary.values():
    if values == 'bruce':
        print 'found Bruce'
    print values


testFile = open('test.txt', "wb")

print testFile.mode

testFile.write(bytes("last line to write to file\n"))
testFile.close()


testFile = open("test.txt","r+")

print testFile.readline()
testFile.close()

os.remove('test.txt')

print dir(os)

