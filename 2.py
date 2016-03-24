'''
Created on Feb 25, 2015

@author: edwingsantos
'''
import string

def doSomethingWithTheWord(filepath):
    for line in open(filepath):
        for word in line.split():
            srt = string.upper(word)
            #print( word.upper())


file = open('out.txt','rb')
str =  file.readlines()


print str
print file
try:
    for line in range(5):
        #str.append('echo')
        print str
        
finally:
    file.close()

file2 = open('out.txt', 'ab')

file2.write("Searching and Replacing Text in a File")
file2.close()

file3 = open('out.txt', 'r').readlines()

doSomethingWithTheWord(file)




if __name__ == '__main__':
    pass