from sort import *
from plot import *
import random
import time


import unittest


runtime = {"bubble" : {"ops" : [], "time": [] }, "selection": {"ops" : [], "time": [] }, "quick" : {"ops" : [], "time": [] }, "insertion": {"ops" : [], "time": [] } }


class SortingFuncTest(unittest.TestCase):
    
    size = None


    def setUp(self):
        # generate sample of 100 random numbers 
        self.randomlist = random.sample( range(0,100000), self.size)
        self.randomlist.reverse()
        self.sortedlist = sorted(self.randomlist)


    def tearDown(self):
        self.randomlist = []
        self.sortedlist = []

    def test_bubble_sort(self):
        st = time.time()
        (rlist,ops) = bubble_sort(self.randomlist)
        et = time.time()
        runtime["bubble"]["ops"].append(ops)
        runtime["bubble"]["time"].append(et - st)
        
        self.assertEqual( self.sortedlist, rlist )

    def test_selection_sort(self):
        st = time.time()
        (rlist, ops) = selection_sort(self.randomlist)
        et = time.time()
        runtime["selection"]["ops"].append(ops)
        runtime["selection"]["time"].append(et - st)
        
        self.assertEqual( self.sortedlist, rlist )


    def test_quick_sort(self):
        steps = [0]
        st = time.time()
        quick_sort(self.randomlist, 0, len(self.randomlist) - 1, steps )
        et = time.time()
        runtime["quick"]["ops"].append(steps[0])
        runtime["quick"]["time"].append(et - st)
        
        self.assertEqual( self.sortedlist, self.randomlist )

    def test_insertion_sort(self):
        st = time.time()
        (rlist, ops) = insertion_sort(self.randomlist)
        et = time.time()
        runtime["insertion"]["ops"].append(ops)
        runtime["insertion"]["time"].append(et - st)
        self.assertEqual( self.sortedlist, rlist)

        
"""
    def test_insertion_sort2(self):
        self.sorted_segment = sorted(self.randomlist[0: 50)
        rlist = insertion_sort2(self.randomlist, 0, 49
        self.assertEqual( self.sorted_segment, rlist[0: 50)
"""


if __name__ == "__main__":
    sizes = [10, 50 , 100, 500, 1000, 5000]
    for i in range(6):
        SortingFuncTest.size = sizes[i]
        unittest.main()
        
    #plot the graph
    
    pylab.figure("Operations")
    pylab.title("Operation count T(n) vs n")
    pylab.xlabel('input size(n)')
    pylab.ylabel('Operation count T(n)')
    pylab.legend(loc ='best')
    for k in runtime:
        Tn = runtime[k]["ops"]
        if k == "bubble":
            bsortRt = BubbleSortRunTime(Tn, sizes)
            bsortRt.plotRuntime(':b', "BubbleSort")
        if k == "selection":
            ssortRt = SelectionSortRunTime(Tn, sizes)
            ssortRt.plotRuntime('y-', "SelectionSort")
        if k == 'quick':
            qsortRt = QuickSortRunTime(Tn, sizes)
            qsortRt.plotRuntime('g:', "QuickSort")
        if k == 'insertion':
            isortRt = InsertionSortRunTime(Tn, sizes)
            isortRt.plotRuntime('r-', "InsertionSort")
            
    pylab.figure("ExecutionTime")
    pylab.title("Execution Time T(n) vs n")
    pylab.xlabel('input size(n)')
    pylab.ylabel('Execution Time T(n)')    
    for k in runtime:
        Tn = runtime[k]["time"]
        if k == "bubble":
            bsortRt = BubbleSortRunTime(Tn, sizes)
            bsortRt.plotRuntime('b:', "BubbleSort")
        if k == "selection":
            ssortRt = SelectionSortRunTime(Tn, sizes)
            ssortRt.plotRuntime('y-', "SelectionSort")
        if k == 'quick':
            qsortRt = QuickSortRunTime(Tn, sizes)
            qsortRt.plotRuntime('g:', "QuickSort")
        if k == 'insertion':
            isortRt = InsertionSortRunTime(Tn, sizes)
            isortRt.plotRuntime('r-', "InsertionSort")            
            
    
        
    
        
        
    
    
    
    
        
    
