"""
LAB 4:
BY : Ramesh ( Rameswaran Sinnarajah)

"""
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    # runtime : O(1)
    # it takes a constant amount of time to check if 
    # the head is pointing to None
    def is_empty(self):
        return (self.head == None)

    # runtime : O(1)
    # it takes a constant amount of time to
    # change the head and newNode references
    def prepend(self, data):
        newNode = Node(data)
        
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            
        newNode = None
        
    # runtime: O(n)
    # in the worst case, whole linked list
    # needs to be traversed to reach the last node
    # to perform append operation
    def append(self, data):
        
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode;
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next    
            cur.next = newNode    
            cur = None
        newNode = None
        
    
    # runtime: O(n)
    # in the worst, insertion is done 
    # after the last node
    def insert_after(self, target, data):
        newNode = Node(data)
        newNode.next = target.next
        target.next = newNode
        newNode = None
    
    # runtime: O(n)
    # in the worst case, the last is what being
    # deleted.
    # target can be data or reference to a node
    def delete ( self, target):
        if self.head == None or target == None:
            return False
        if isinstance(target, int ):
            return self.delete_node_with_data(target)
        else:
            return self.delete_node(target)
    
    def delete_node_with_data(self, data):
        prev = None
        cur = self.head
        while cur.data != data and cur.next != None:
            prev = cur
            cur = cur.next
        
        if cur.data == data:
            prev.next = cur.next
            cur.next = None
            cur = None
            return True
            
        cur = None
        return False
    
    def delete_node(self, node):
        cur = self.head
        while cur.next != node:
            cur = cur.next
            if cur == None:
                return False
        cur.next = node.next
        node.next = None
        node = None
        return True
        
    # runtime: O(n)
    # in the worst case, last node is being search
    def search(self, data):
        if self.is_empty():
            return None
        
        cur = self.head
        while cur.data != data and cur.next != None:
            cur = cur.next
        
        if cur.data == data:
            return cur
        
        return None
    
    # runtime: O(n)
    # need to traverse the whole list to count
    # all the nodes
    def size(self):
        if self.is_empty():
            return 0
        cur = self.head
        list_size = 1
        while cur.next != None:
            cur = cur.next
            list_size = list_size + 1
        
        return list_size
        
    # runtime: O(n)
    # need to access all the nodes to store
    # their data in a list
    def to_list(self):
        lst = []
        cur = self.head
        
        while cur != None:
            lst.append(cur.data)
            cur = cur.next
        return lst
    
    # runtime: O(n)
    # print calls to_list method which takes 
    # O(n) in the worst case.
    def print(self) :
        print(self.to_list())
        

# main method for testing purposes.        
if __name__ == "__main__":
    
    ll = SinglyLinkedList()
    
    for i in range(10):
        ll.append(i)
        
    # insert after
    node = ll.search(5)
    print("node value " , node.data)
    
    ll.insert_after(node, 9)
    print(ll.size())
    ll.print()
    print(ll.delete(node))
    ll.print()
    
    print(ll.delete(None))