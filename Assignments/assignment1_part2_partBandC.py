class Node:
	# Node is internal.  Feel free to add
	# to the argument list for its init function if you want
	# you can add additonal data members if you like
	def __init__(self, data , next = None, prev = None):
		self.data = data
		self.next  = next
		self.prev  = prev
            

class SortedList:
    def __init__(self):
        self.front = None
        self.back = None
        
    """
    # METHOD: insert
    # TIME CMPLEXITY = O(n) 
    #   - In the worst case, we have traverse upto n-1 node ( last node can be accessed using back reference)
    #     to find the node smalller than data we are trying to insert. That gives a time complexity of O(n)  
    """    
    def insert(self, data):
        # creat a new node
        newNode = Node(data)
        # list is empty 
        if self.front == None:
            self.front = newNode
            self.back = newNode
        else:
            if data <= self.front.data:
                self.insertAtFront(data)
            elif data >= self.back.data:
                self.insertAtEnd(data)
            else:
                self.insertInMiddle(data)
                
        
    def insertAtFront(self, data):
        newNode = Node(data)
        newNode.next = self.front
        self.front.prev = newNode
        # reset front
        self.front = newNode
        newNode = None # unset reference
        
        
    def insertAtEnd(self,data):
        newNode = Node(data)
        newNode.prev = self.back
        self.back.next = newNode
        # reset back
        self.back = newNode
        newNode = None # unset reference
        
    def insertInMiddle(self,data):
        newNode = Node(data)
        # search for the right place to insert
        curNode = self.front
        while curNode.data <= data:
            curNode = curNode.next
        
        #inser the data here
        curNode.prev.next = newNode
        newNode.prev = curNode.prev
        newNode.next = curNode
        curNode.prev = newNode
        
        #unset references
        newNode = None
        curNode = None
    """
    # METHOD: remove
    # TIME COMPLEXITY = O(n)
    #   - In the  worse case, the node we are trying to remove could be the second last node.
    #   - in this case, we still have to traverse n-1 nodes. So time comlexity is O(n)
    """
    def remove(self, data):
        # check if the list is empty
        if self.isEmpty():
            print("List is empty")
            return False
        # if the data is absence return False
        if self.is_present(data) == False:
            return  False
        if self.front == self.back:
            if self.front.data == data:
                self.front = None
                self.back = None
                return True
            else:
                return False
        if self.front.data == data:
            self.removeFirstNode()
            return True
        elif self.back.data == data:
            self.removeLastNode()
            return True
        else:
            self.removeInMiddle(data)
            return True
        
    
    def removeLastNode(self):
        temp = self.back
        self.back = self.back.prev
        temp.prev = None
        self.back.next = None
        # unset temp
        temp = None
        
    
    def removeFirstNode(self):
        temp = self.front
        self.front = self.front.next
        temp.next = None
        self.front.prev = None
        # unset temp
        temp = None
        
    def removeInMiddle(self, data):
        curNode = self.front
        while curNode.data != data:
            curNode = curNode.next
        
        # remove node pointed by curNode
        curNode.prev.next = curNode.next
        curNode.next.prev = curNode.prev
        
        # unset references
        curNode.prev = None
        curNode.next = None
        curNode = None
        
        

    # function to check if a node is present
    """
    # METHOD: IS_PRESENT
    # TIME COMPLEXITY = O(n)
    #   - In the worst case, we have to traverse to the end of the list
    #     to find a node. So, the time complexity is O(n)
    """
    def is_present(self, data):
        curNode = self.front
        while curNode != None:
            if curNode.data == data:
                return True
            curNode = curNode.next
        return False
    
    def isEmpty(self):
        if self.front == None:
            return True
        return False
    
    # print the content of the list
    def print(self):
        curNode = self.front
        while curNode != None:
            print(curNode.data, end="-")
            curNode = curNode.next
    
    # print the lengh of the list
    """
    # METHOD: __len__
    # TIME COMPLEXITY: O(n)
    #   - We need to traverse to the end of the list to count all the nodes. So it is O(n)
    """
    def __len__(self):
        curNode = self.front
        count = 0
        while curNode != None:
            count = count + 1
            curNode = curNode.next
        return count
    
    def __iter__(self):
        curr = self.front
        while curr:
            yield curr.data
            curr = curr.next
    
    def __reversed__(self):
        curr = self.back
        while curr:
            yield curr.data
            curr = curr.prev

            

if __name__ == "__main__":
    
    # testing 
    sortedList = SortedList()
    
    # test insertion
    sortedList.insert(10)
    sortedList.insert(9)
    sortedList.insert(8)
    sortedList.insert(1)
    
    # test removal
    print(sortedList.remove(111))
    
    # printing the content of the list.
    for i in sortedList:
        print(i)


    
    

    