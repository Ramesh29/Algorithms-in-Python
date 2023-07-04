"""
Node class houses data stored in linked list

"""
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

"""
StackLL implements stack using Linked List
"""
class StackLL:
    
    # initializing class variables
    def __init__(self):
        self.head = None
        
    # Push a new item on the top of the stack
    def push(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        
    
    # Pop a node from the top of a stack
    def pop(self):
        if self.isEmpty():
            return None
        node = self.head
        self.head = self.head.next
        
        node.next = None
        
        return node        
    
    # returns the data from the top of a stack
    def top(self):
        if self.isEmpty():
            return None
        return self.head.data
    
    # return true if stack is full, false otherwise
    def isEmpty(self):
        return self.head == None
    
    # return stack items as list
    def toList(self):
        lst = []
        temp = self.head
        while temp != None:
            lst.append(temp.data)
            temp = temp.next
        
        return lst
    

if __name__ == "__main__":
    stackLL = StackLL()
    for i in range(10):
        stackLL.push(i)
    
    print(stackLL.top())
        
    for i in range(10):
        print(stackLL.pop().data)