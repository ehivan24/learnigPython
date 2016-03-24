'''
Created on Feb 24, 2015

@author: edwingsantos
'''
from timeit import reindent
import string
from numpy import square


hello = r"long sTring"
hello2 = u"long\u0020string"
num = 234

print hello, hello2

for c in hello2:
    print c
    
print ord('a')
print chr(97)

def whatIsIt(obj):
    return type(obj)



def containAny(seq, aset):
    for c in seq:
        if c in aset: return True
    
    return False
            
    

print whatIsIt(hello)
print whatIsIt(num)


print ' Welcome '.center(20,'#')
print '*' * 20


print containAny("helloWorld", ' ')


print containAny(hello, 's')


line = """
Even if the lines in s 
are initially 
"""

print reindent(line, 2)

form_letter = '''Dear $customer,
     I hope you are having a great time.
     If you do not find Room $room to your satisfaction,
     let us know. Please accept this $$5 coupon.
                 Sincerely,
                 $manager
                 ${name}Inn'''
letter_template = string.Template(form_letter)
print letter_template.substitute({'name':'Sleepy', 'customer':'Fred Smith',
                                       'manager':'Barney Mills', 'room':307,
                                      })




msg =  string.Template('the $number of $square ')
for number in range(10):
    square = number * number
    print msg.substitute(locals())
    

str = string.Template('$who likes $what')

name = raw_input('who: ')
likes = raw_input('likes: ') 
print (str.substitute(who=name, what=likes))





if __name__ == '__main__':
    pass