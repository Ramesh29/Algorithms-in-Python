# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 22:56:31 2023
Class Runtime
    - contains data pertaining to the runtime of each sorting algorithm and 
    - a plotting function.
@author: charl
"""

import pylab
import math

class Runtime:
    def __init__(self, Tn, n):
        self.Tn = Tn
        self.n = n
        

    def plotRuntime(self, style, legend):
        pylab.plot(self.n, self.Tn, style, label=legend)
        pylab.legend()


class BubbleSortRunTime(Runtime):
    def __init__(self, Tn, n):
        super().__init__(Tn, n)
    

class SelectionSortRunTime(Runtime):
    def __init__(self, Tn, n):
        super().__init__(Tn, n)
        

class InsertionSortRunTime(Runtime):
    def __init__(self, Tn, n):
        super().__init__(Tn, n)

class QuickSortRunTime(Runtime):
    def __init__(self, Tn , n):
        super().__init__(Tn, n)
        
        
