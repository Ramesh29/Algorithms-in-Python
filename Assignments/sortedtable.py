# -*- coding: utf-8 -*-
"""
assignment 2/part A : ananlysis of member functions
Created on Fri Jun 30 09:55:11 2023
@author: Rameswaran (Ramesh) Sinnarajah
"""

class SortedTable:
    # packing the key-value pair into one object
    class Record:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            
    def __init__(self, cap=32):
        # this initializes a list of capacity length with None
        self.the_table = [ None for i in range(cap)]
        self.cap = cap
    
    # Complexity ananlysis of insert:
    # ------------------------------
    # Two main operations done by insert are 
    # doubling the the_table when it is full which
    # takes at most O(n) time Complexity, and
    # performing a bubble sort to keep the Record
    # sorted which takes at worst case O(n2)
    # Therefore, the total time Complexity of insert is
    # O(n) + O(n2) = O(n2)
    def insert(self, key, value):
        if (self.search(key) != None ):
            return False
        
        if (len(self) == self.cap):
            # increase the capacity if list is full
            new_table = [ None for i in range( self.cap * 2)]
            for i in range(self.cap):
                new_table[i] = self.the_table[i]
            self.the_table = new_table
            self.cap = self.cap * 2
            
        self.the_table[len(self)] = self.Record(key, value)
        size = len(self)
        for i in range (0 , size-1 ):
            for j in range(0, size-1-i):
                if(self.the_table[j].key > self.the_table[j+1].key):
                    tmp = self.the_table[j]
                    self.the_table[j] = self.the_table[j+1]
                    self.the_table[j+1] = tmp
        return True
    
    # Complexity ananlysis of modify
    # ------------------------------
    # In the worst case, the item to be modify could be the
    # last item in the table or could not be in the table at all
    # So it would take a linear time
    # Complexity of O(n) + some constant time for assignment
    # Therefore, time Complexity of modify is O(n)
    def modify(self, key, value):
        i = 0
        while ( i < len(self) and self.the_table[i].key != key ):
            i = i + 1
        if( i == len(self)):
            return False
        else:
            self.the_table[i].value = value
            return True
    
    # Complexity analysis of remove 
    # -----------------------------
    # Regardless of where the record is found in the table
    # remove method has the time Complexity of O(n)
    # If the record is the first item in the table, first while loop 
    # to look for the record takes O(1) but the second while loop 
    # will have to shift n-1 items.So that takes O(n) time Complexity.
    # If the record is the last item in the table, the first while 
    # loop would take O(n) time and the second while loop takes 
    # no time at all. In this case, time Complexity is also O(n)
    # Time Complexity is still O(n) if the record appears in the middle of
    # the table ( first while loop runs n/2 times to find it and the second
    # while loop runs n/2 times to shift items) or does not appear at all.
    def remove(self, key):
        i = 0
        size = len(self)
        
        while( i < size and self.the_table[i].key != key ):
            i = i + 1
        if (i == size):
            return False
        
        while( i+1 < size ):
            self.the_table[i] = self.the_table[i+1]
            i = i + 1
        
        self.the_table[i] = None
        return True
    
    # Complexity analysis of search
    # -----------------------------
    # In the worst case, the record could be the last item or
    # does not appear at all in the table. So it takes a linear
    # time Complexity of O(n)
    def search(self, key):
        i = 0
        size = len(self)
        while i < size and self.the_table[i].key != key:
            i = i + 1
        if i == size:
            return None
        else:
            return self.the_table[i].value
    
    # Complexity analysis of capacity
    # -------------------------------
    # it takes a constant time Complexity of O(1) 
    # as it returns the capacity of the table
    def capacity(self):
        return self.cap
    
    
    # Complexity analysis of __len__
    # ------------------------------
    # In the worst case, the table can be full.
    # so the while loop will have to run n ( # of records)
    # times to find the length of the table. so
    # time Complexity is O(n)
    def __len__(self):
        i = 0
        count = 0
        while ( i < len(self.the_table)):
            if ( self.the_table[i] != None ):
                count = count + 1
            i = i + 1
        return count
    
        
    
    