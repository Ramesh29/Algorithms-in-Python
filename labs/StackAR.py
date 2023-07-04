"""
Array class implements standard functionalities of
array found in other languages using python list
"""
class Array(object):
    
    # initializes class variables
    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nitems = 0
        self.__size = initialSize
        
    # returns the len of the items in the array
    def __len__(self):
        return self.__nitems
    
    # get the item at index 'n'
    def get(self, n):
        if n in range(0, self.__nitems):
            return self.__a[n]
    
    # set the item at the index 'n' to 'value' 
    def set(self, n, value):
        if n in range(0, self.__siae):
            self.__a[n] = value
        else:
            # set the new element at index n
            self.__a[n] = value
            
        # increase the number of items
        self.__nitems = self.__nitems + 1
    
    # insert the value at the end of the array
    def insertEnd(self, value):
        if len(self) == self.__size:
            self.doubleArray()
        
        # set the element at the end of the array
        self.__a[self.__nitems] = value
        self.__nitems = self.__nitems + 1
    
    # remove the value from the end of the array
    def removeEnd(self):
        if len(self) == 0:
            return None
        
        value = self.__a[self.__nitems - 1]
        self.__a[self.__nitems - 1 ] = None
        self.__nitems = self.__nitems - 1
        
        return value
        
    # get the value from the end of the array
    def getEndValue(self):
        if len(self) == 0:
            return None
        
        return self.__a[self.__nitems - 1]
    
    # returns true if array is full, false otherwise
    def isFull(self):
        return self.__nitems == self.__size
    
    # returns true if array is empty, false otherwise
    def isEmpty(self):
        return len(self) == 0
    
    # double the array capacity
    def doubleArray(self):
        # increase the array size by doubling as the number of 
        # elements it has
        self.__a = self.__a[:] + [None] * self.__size
        self.__size = self.__size * 2
    
    # returns a list of items in the array        
    def toList(self):
        return self.__a[:self.__nitems]
        
    
"""
class StackAR implements stack using
Array class.
"""
class StackAR:
    
    # intializes a stack
    def __init__(self, size):
        self.stack = Array(size)
    
    # insert data at the end
    def push(self, data):
        self.stack.insertEnd(data)
    
    #  remove data from the end
    def pop(self):
        return self.stack.removeEnd()
    
    # get the value of the last index 
    def top(self):
        return self.stack.getEndValue()
    
    # return true if stack is full, false otherwise
    def isFull(self):
        return self.stack.isFull()
    
    # return true if stack is empty, false otherwise
    def isEmpty(self):
        return self.stack.isEmpty()
    
    # get the items in the stack as list
    def toList(self):
        return self.stack.toList()
    
    
# StackARClient for testing

if __name__ == "__main__":
    stack = StackAR(5)
    for i in range(10):
        stack.push(i)
        
    print("Top is " , stack.top())
        
    for i in range(11):
        print("Poping...")
        print( stack.pop())
    
    
        
    
