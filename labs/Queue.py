# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 14:24:43 2023

@author: charl
"""

class Queue(object):
    
    def __init__(self):
        self.__queue = []
        
    
    
    def enqueue(self, data):
        self.__queue.append(data)
    
    def dequeue(self):
        
        if len(self.__queue) == 0:
            return None
        
        value = self.__queue[-1]
        self.__queue = self.__queue[0:-1]
        
        return value
        
    
    def top(self):
        if len(self.__queue) == 0:
            return None
        
        return self.__queue[-1]
    
    def isEmpty(self):
        return len(self.__queue) == 0
    
    
# Queue test client
if __name__ == "__main__":
    q = Queue()
    for i in range(10):
        q.enqueue(i)
        
    for i in range(10):
        print(q.dequeue())