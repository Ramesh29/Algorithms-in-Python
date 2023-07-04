
"""
Queue class implements a queue using python list
and follows FIFO method while doing enqueue and dequeue
"""

class Queue(object):
    
    # constructor initializes local variable __queue
    # to a python list
    def __init__(self):
        self.__queue = []
        
    # enqueue append the data at the end of the list
    def enqueue(self, data):
        self.__queue.append(data)
    
    # dequeue remove the first element from the beginning of 
    # the list
    def dequeue(self):  
        if len(self.__queue) == 0:
            return None
        value = self.__queue[0]
        self.__queue = self.__queue[1:]
        
        return value
    
    # top returns the item at the front
    # of the list
    def top(self):
        if len(self.__queue) == 0:
            return None
        
        return self.__queue[0]
    
    # isEmpty returns True if queue is empty,
    # False otherwise
    def isEmpty(self):
        return len(self.__queue) == 0
    
    # getQueue returns a copy of __queue 
    def getQueue(self):
        return self.__queue[:]
    