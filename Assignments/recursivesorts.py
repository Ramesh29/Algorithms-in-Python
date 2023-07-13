
# iterative bubble sort
def bubble_sort(arr):
    n = len(arr)
    swapped = False
    # Traverse through all the array elements
    for i in range(n-1):
        for j in range(0, n-1-i):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
        if not swapped:
            return
    
# recursive bubble sort
def recursive_bubble_sort(arr, startIndex, endIndex):
    if startIndex == endIndex:
        return 
    # traverse the array from start index to end index - 1
    for i in range(startIndex, endIndex-1):
       if arr[i] > arr[i + 1]:
           arr[i], arr[i + 1] = arr[ i + 1 ], arr[i]
           
    # recursively call recursive_bubble_sort
    recursive_bubble_sort( arr, startIndex, endIndex-1)

# iterative selection sort
def selection_sort(arr):
    for outer in range(len(arr)-1):
        min = outer
        for inner in range( outer + 1, len(arr)):
            if arr[inner] < arr[min]:
                min = inner
                
        # swap
        arr[outer], arr[min] = arr[min], arr[outer]
        

# recursive selection sort
def recursive_selection_sort(arr, startIndex, endIndex):
    if startIndex == endIndex:
        return
    # replace the first element in the array with the min found in the rest of the array
    minIndex = startIndex
    for i in range(startIndex+1, endIndex):
        if arr[i] < arr[minIndex]:
            minIndex = i
    
    #swap
    arr[startIndex],arr[minIndex] = arr[minIndex], arr[startIndex]
    
    # recursively call seleciton sort
    recursive_selection_sort(arr, startIndex + 1, endIndex)
    
# iterative insertionSort
def insertion_sort(arr):
    for outer in range(1, len(arr)):
        temp = arr[outer]
        inner = outer
        while inner > 0 and temp < arr[inner-1]:
            arr[inner] = arr[inner-1]
            inner = inner - 1
        arr[inner] = temp
        
        
# recursive insertion_sort
def recursive_insertion_sort(arr, startIndex):
    if startIndex == len(arr):
        return
    
    temp = arr[startIndex]
    index = startIndex
    
    while index > 0 and temp < arr[index - 1]:
        arr[index] = arr[index-1]
        index = index - 1
    arr[index] = temp
    
    recursive_insertion_sort(arr, startIndex + 1)
    
    

def quick_sort(nums, low, high):
    if low >= high:
        return
    
    pivot_index = partition(nums, low, high)
    quick_sort(nums, low, pivot_index - 1 )
    quick_sort(nums, pivot_index + 1, high)





def partition(nums, low, high):
    pivot_index = (low + high) // 2
    swap(nums, pivot_index, high)
    
    i = low
    
    for j in range(low, high, 1):
        if nums[j] < nums[high]:
            swap(nums, i , j)
            i = i + 1
            
    swap(nums, i , high)
    
    return i

def swap(nums, i , j ):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

    
    

    

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
 
insertion_sort(arr)
 
print("Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")   
    
arr = [64, 34, 25, 12, 22, 11, -1]
 
recursive_insertion_sort(arr, 1 )
 
print("Sorted array by recursive insertion sort:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")       
    
    

nums = [-2,-1,0,1,0,-1,-2]
print()
quick_sort(nums, 0 , len(nums) - 1)
print(nums)