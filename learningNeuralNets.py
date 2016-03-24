'''
Created on Jan 16, 2015

@author: edwingsantos
'''

if __name__ == '__main__':
    pass

import numpy as np

x = np.array([1,2,3,4,5,6,8,9,0,4,3,2,1])
a =np.array([[3,4,5],[2,3,4]])
b = np.array([[1,3],[2,4],[3,5]])

a1 =  np.array([[2,3,4],[3,5,6]])
b2 = np.array([[4,3,6],[8,5,1]])

print np.dot(a,b)
print np.cross(a1, b2)

print np.where(a>3,1,0)
print np.transpose(a)



