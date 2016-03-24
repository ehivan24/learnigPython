'''
Created on Jan 30, 2015

@author: edwingsantos
'''



"""
import threading 
import time



def timer(name, delay, repeat):
    print "Timer " + name + " started "
    while repeat > 0:
        time.sleep(delay)
        print name + ": " + str(time.ctime(time.time()))  
        repeat -= 1
    print " Timer " + name + "compleated"

def Main():
    t1 = Thread(target=timer, args=("Timer1", 1, 5))
    t2 = Thread(target=timer, args=("Timer2", 2, 5))
    
    t1.start()
    t2.start()
    
    
    
    print "Main Compleated"
    
 

class AsycWrite(threading.Thread):
    def __init__ (self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out  
    def run(self):
        f = open(self.out, "a")
        f.write(self.text + '\n')
        time.sleep(2)
        print "Finished background " + self.out

def Main():
    message = raw_input("Enter a str to store: ")
    background = AsycWrite(message, "out.txt") 
    background.start()
    print "Program can continue to run while it writes "
    print 100 + 4000
    x = 1
    while x < 20:
        print x + 1
        x +=1
        time.sleep(1)
        if x == 18: 
            break 
            
    background.join()
    
    print "Waited until Thread was compleated"
"""

import threading
import time

tLock = threading.Lock()

def timer(name, delay,repeat):
    print "Timer: " + name + " Started"
    tLock.acquire()
    print name + " Aquiered the lock "
    while repeat > 0:
        time.sleep(delay)
        print name + ": " + str(time.ctime(time.time()))
        repeat -= 1
    print name + "is releasing the lock " 
    tLock.release()
    print "Timer: " + name + " Completed"

def Main():
    t1 = threading.Thread(target=timer, args=("Timer1" ,  1, 5))
    t2 = threading.Thread(target=timer, args=("Timer2" ,  2, 5))
    
    t1.start()
    t2.start()
    
    print "Completed"
    print type(t1)
        
if __name__ == '__main__':
    Main()
    