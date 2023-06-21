# Lab 3 - Data Structures and Algorithms
# By: Rameswaran Sinnarajah ( Ramesh )
#########################################


# Function is passed in a number and returns
# factorial of that number
##
def factorial(number):
    if number <= 0 or type(number) != int :
        print("Please enter a positive non-zero integer")
        return
    if number == 1:
        return 1
    else:
        return number * factorial( number - 1 )


# Function is passed in a list of values and key.
# If a matching key is found in the list, it returns
# index of where the key was found,otherwise it returns
# -1
##
def linear_search(list, key, startIndex = 0):
    # if list is empty, key does not exist in the list
    if not list:
        return -1
    # check if the first element is the key
    if list[0] == key:
        return startIndex
    startIndex = startIndex + 1
    return linear_search(list[1:],key, startIndex )


# Function is passed a sorted list of values and key.
# If a matching key is found in the list, it returns
# index of where the key was found. Else returns - 1
##
def binary_search(list, key, startIndex = 0):

    # if only one element is left and not equal to key, return -1
    if len(list) == 1 and list[0] != key:
        return -1
    # calculate the mid index of the list
    mid = len(list)//2

    # if the mid element is the key, then return the actual index of
    # element in the original list
    if key == list[mid]:
        return ( startIndex + mid )
    # if key is less than "mid" element , do the search in the first
    # half of the array.
    elif key < list[mid]:
            return binary_search( list[:mid], key, startIndex )
    # if key is greater than "mid" element, do the search in the second
    # half of the array
    else:
            return binary_search(list[mid:], key, startIndex + mid )


# Function TowerOfHanoi moves disks from towerOne to towerThree 
# using towerTwo while respecting the following rules:
#   1. Only one disk can be moved at a time.
#   2. A disk can only be moved if it is the uppermost disk in the pole.
#   3. A larger disk can't be placed on a smaller disk.


def TowerOfHanoi( numDisk, towerOne, towerTwo, towerThree):
    if numDisk > 0:
        TowerOfHanoi(numDisk -1 , towerOne, towerThree, towerTwo)
        print( str(towerOne) + " to " + str(towerThree))
        TowerOfHanoi(numDisk -1 , towerTwo, towerOne, towerThree)
        

if __name__ == "__main__":
     print(factorial(5))