'''
Created on Feb 25, 2015

@author: edwingsantos
'''

import random
import heapq


def bubbleSort(items):
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]



def insertionSort(items):
    for i in range(1,len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1 
            
def heapSort(items):
    heapq.heapify(items)
    items[:] = [heapq.heappop(items) for i in range(len(items))] 


items = [random.randint(-50, 100) for c in range(20)]


print items

#bubbleSort(items)
#insertionSort(items)
heapSort(items)

print items









if __name__ == '__main__':
    pass