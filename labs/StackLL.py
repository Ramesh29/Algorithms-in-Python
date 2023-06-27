"""
StackLL : Stack implementation using Linked List
By : Ramesh
"""
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class StackLL:
    
    def __init__(self):
        self.head = None
        
    
    def push(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        
        
    
    def pop(self):
        if self.isEmpty():
            return None
        node = self.head
        self.head = self.head.next
        
        node.next = None
        
        return node        
    
    def top(self):
        if self.isEmpty():
            return None
        return self.head.data

    
    
    def isEmpty(self):
        return self.head == None
    

if __name__ == "__main__":
    stackLL = StackLL()
    for i in range(10):
        stackLL.push(i)
    
    print(stackLL.top())
        
    for i in range(10):
        print(stackLL.pop().data)