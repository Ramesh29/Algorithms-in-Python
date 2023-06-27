# -*- coding: utf-8 -*-
"""
Stack implementaion using Array
By : Ramesh

"""

# This class implements functionalities found in array 
# in other languages using python list.

class Array(object):
    
    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nitems = 0
        self.__size = initialSize
        
    def __len__(self):
        return self.__nitems
    
    def get(self, n):
        if n in range(0, self.__nitems):
            return self.__a[n]
        
    def set(self, n, value):
        if n in range(0, self.__siae):
            self.__a[n] = value
        else:
            # set the new element at index n
            self.__a[n] = value
            
        # increase the number of items
        self.__nitems = self.__nitems + 1
    
    def insertEnd(self, value):
        if len(self) == self.__size:
            self.doubleArray()
        
        # set the element at the end of the array
        self.__a[self.__nitems] = value
        self.__nitems = self.__nitems + 1
    
    def removeEnd(self):
        if len(self) == 0:
            return None
        
        value = self.__a[self.__nitems - 1]
        self.__a[self.__nitems - 1 ] = None
        self.__nitems = self.__nitems - 1
        
        return value
        
    
    def getEndValue(self):
        if len(self) == 0:
            return None
        
        return self.__a[self.__nitems - 1]
    
    def isFull(self):
        return self.__nitems == self.__size
    
    def isEmpty(self):
        return len(self) == 0
    
    
    
    def doubleArray(self):
        # increase the array size by doubling as the number of 
        # elements it has
        self.__a = self.__a[:] + [None] * self.__size
        self.__size = self.__size * 2
        print("Array size doubled to " + str(self.__size))
        
    
# StackAR uses Array class to 
# implement a stack
class StackAR:
    
    def __init__(self, size):
        self.stack = Array(size)
        
    def push(self, data):
        # insert data at the last index
        self.stack.insertEnd(data)
    
    def pop(self):
        return self.stack.removeEnd()
    
    def top(self):
        return self.stack.getEndValue()
    
    def isFull(self):
        return self.stack.isFull()
    
    def isEmpty(self):
        return self.stack.isEmpty()
    
    
# StackARClient for testing

if __name__ == "__main__":
    stack = StackAR(5)
    for i in range(10):
        stack.push(i)
        
    print("Top is " , stack.top())
        
    for i in range(11):
        print("Poping...")
        print( stack.pop())
    
    
        
    
