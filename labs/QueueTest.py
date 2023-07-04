"""
unit test for Queue.py

"""

from Queue import *
import unittest

class QueueTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    # test if items are enqueued right
    def test_enqueue(self):
        l = [ i for i in range(10)]
        q = Queue()
        for item in range(10):
            q.enqueue(item)
            
        self.assertEqual( l , q.getQueue() )
    
    def test_dequeue(self):
        l = [ i for i in range(10)]
        q = Queue()
        for item in range(10):
            q.enqueue(item)
        
        self.assertEqual(0, q.dequeue())
    
    def test_top(self):
        l = [ i for i in range(10)]
        q = Queue()
        for item in range(10):
            q.enqueue(item)
            
        self.assertEqual(0 , q.top())
        
    
    def test_isEmpty(self):
        l = [ i for i in range(10)]
        q = Queue()
        for item in range(10):
            q.enqueue(item)
            
        for item in range(10):
            q.dequeue()
            
        self.assertEqual( q.isEmpty(), True)
    
# run the unittest 
if __name__ == "__main__":
    unittest.main()
    

