"""
Sorting module contains a set of sorting algorithms
"""


# Bubble Sort
# parameter: a list of numbers
# returns : a tuple of sorted list and operation count
def bubble_sort(alist):
    steps = 0
    size = len(alist)
    
    for i in range(size-1):
        for j in range(size-1-i):
            if alist[j] > alist[j+1]:
                alist[ j ], alist[ j + 1 ] = alist[ j + 1 ], alist[ j ]
                steps += 4
    return (alist, steps)

# Selection Sort
# parameter: a list of numbers
# returns : a tuple of sorted list and operation count
def selection_sort(alist):
    steps = 0
    size = len(alist)
    
    for i in range(size):
        minIndex = i
        for j in range(i+1, size):
            if alist[j] < alist[minIndex]:
                minIndex = j
                steps += 2
                
        if minIndex != i:
            alist[minIndex], alist[i] = alist[i], alist[minIndex]
            steps += 4
    
    return (alist, steps)

# insertion sort
# parameter: a list of numbers
# returns : a tuple of sorted list and operation count
def insertion_sort(alist):
    steps = 0
    size = len(alist)
    
    for i in range(size):
        j = i
        
        while j > 0 and alist[ j - 1 ] > alist[ j ]:
            alist[j - 1], alist[ j ] = alist[ j ], alist[ j - 1 ]
            j = j - 1
            steps += 5 # 3 for swaps , 2 for comparison

    return (alist, steps)


#quick_sort
# parameter: a list of numbers, low index, high index, and a list to keep track of operation counts
# returns : sort the list of numbers, and steps list
def quick_sort(alist, low, high, steps):
    if low >= high:
        return
    
    pivot_i, psteps = partition(alist, low, high)
    steps[0] = steps[0] + psteps
    
    quick_sort( alist, low, pivot_i-1 , steps )
    quick_sort( alist, pivot_i+1, high, steps )    
    
def partition( alist, low, high):
    steps = 0
    pivot_i = ( low + high) // 2
    alist[pivot_i] , alist[high] = alist[high], alist[pivot_i]
    
    i = low
    
    for j in range(low, high):
        if alist[j] <= alist[high]:
            alist[i], alist[j] = alist[j], alist[i]
            i = i + 1
            steps = steps + 6 # 1 for comparison, 3 for swap, 1 addition, 1 assignment
            
    alist[i], alist[high] = alist[high], alist[i]
    
    return i, steps


# insertion_sort2
# parameers: a list of numbers, left index and right index
# returns: the list with element sorted between left and right inclusive.
def insertion_sort2(alist, left, right):
    
    for i in range(left, right+1):
        j = i
        
        while j > left and alist[ j - 1 ] > alist[ j ]:
            alist[ j - 1 ], alist[ j ]  = alist[ j ] , alist[ j - 1 ]
            j = j - 1
            
    return alist


    


