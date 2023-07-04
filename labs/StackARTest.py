"""
unit test for StackAR

"""

from StackAR import *
import unittest

class StackARTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    # testing pushing items on the stack
    def test_push(self):
        stack = StackAR(5)
        for i in range(5):
            stack.push(i)
        
        self.assertEqual(stack.toList(), list(range(5)))
    
    # testing poping items from the stack
    def test_pop(self):
        stack = StackAR(5)
        lst = []
        for i in range(5):
            stack.push(i) 
        
        print(stack.toList())
            
        for i in range(5):
            lst.append(stack.pop())
        l = list(range(5))
        l.reverse()
        self.assertEqual(lst, l )
    
    # testing getting top item from the stack
    def test_top(self):
        stack = StackAR(5)
        for i in range(5):
            stack.push(i)
            
        self.assertEqual(4, stack.top())
    
    # testing if the stack is full
    def test_isfull(self):
        stack = StackAR(5)
        for i in range(5):
            stack.push(i)
            
        self.assertEqual(True, stack.isFull())        
    
    # testing if the stack is empty
    def test_isempty(self):
        stack = StackAR(5)
            
        self.assertEqual(True, stack.isEmpty())       
    
    
    
# run the unittest 
if __name__ == "__main__":
    unittest.main()
    