# Assignment 2 : Part C
# ChainableTable implements hashtable which uses
# chaining as its collision resolution
# *** This implementation assumes that keys are unique. ***
class ChainableTable(object):
    # inner class to represent a Record
    # with key and value
    class Record:
        def __init__(self, key , value ):
            self.key = key
            self.value = value
            
    # inner class to model chaining for collisions in the hashtable
    class ListChain:
        # initialize the chain to empty list
        def __init__(self):
            self.chain = [] 
        # insert a record in the chain if the record
        # is not found. Returns true if the insert is 
        # successful, false otherwise
        def insert(self, record):
            if self.search(record.key) != None:
                return False
            self.chain.append(record)
            return True
        
        # Do a linear search in the chain to find
        # the record. Return the record if found,
        # or None
        def search(self, key):
            for rec in self.chain:
                if rec.key == key:
                    return rec.value
                
            return None
        
        # Returns a copy of the chain
        def getRecords(self):
            return self.chain[:]

    
    # constructor for ChainableTable initialize a 
    # hashtable with the given size defaults to 32
    # also initialize capacity (cap), records and loadfactor
    # to defaults
    def __init__(self, capacity=32):
        self.hashtable = [None for i in range(capacity)]
        self.cap = capacity
        self.records = 0
        self.loadfactor = 1.0
    
    # insert a record in the hashtable
    def insert(self, key, value):

        # if the key is already in the hash table, return false
        if self.search(key) != None:
            return False
        # hash the key and find the index it maps to in chain list
        index  = hash(key) % self.cap
        # if the hashtable is empty at index slot, 
        # assign a new ListChain object to it.
        if self.hashtable[index] == None:
            self.hashtable[index] = self.ListChain()
        
        # insert the record in ListChain at hashtable[index]
        self.hashtable[index].insert( self.Record(key, value))
        self.records += 1
        
        # if exceeds load factor of 1, double the hashtable
        if self.records == self.cap:
            self.rehash()
        return True
    
    # rehash double the size of the hashtable when 
    # it is full and rehash all the records
    def rehash(self):
        # double the capacity
        self.cap = self.cap * 2
        self.records = 0
            
        existing_records = []
        for i in range(len(self.hashtable)):
            if self.hashtable[i] != None:
                existing_records = existing_records + self.hashtable[i].getRecords()
        
        self.hashtable = [ None for i in range(self.cap)]
        # rehash existing records into newhashtable
        for rec in existing_records:
            self.insert(rec.key, rec.value)
    
    # modifies a record's value with the given
    # key, return true if the the modification is 
    # succcess, false ow.
    def modify(self, key, value):
        index = hash(key) % self.cap
        chain = self.hashtable[index]
        
        for rec in chain:
            if rec.key == key:
                rec.value = value
                return True
        
        return False
                
    # remove the record with the given key
    # by simply deleting the record from 
    # the chain
    def remove(self, key):
        index = hash(key) % self.cap
        
        chain = self.hashtable[index]
        
        for i in range(len(chain)):
            if chain[i].key == key:
                del chain[i]
                self.records = self.records - 1
                return True
        
        return False
        
                
    # Search a record in the hashtable.
    # Returns the record if found, else
    # None
    def search(self, key):
        index = hash(key) % self.cap
        if self.hashtable[index] == None:
            return None
        return self.hashtable[index].search(key)
    
    # Returns the capacity of the hashtable
    def capacity(self):
        return self.cap
    
    # Returns the number of records 
    # in the hashtable
    def __len__(self):
        return self.records
    
# Test client
if __name__ == "__main__":
    ct = ChainableTable()
    # inserting records
    ct.insert("ramesh", "Canadian Tire")
    ct.insert("Balesh", "IBM")
    
    # checking record size and Capacity
    print("Number of records:  " + str(len(ct)))
    print("Capacity " + str(ct.capacity()))
    
    # inserting more items
    ct.insert("Thanesh ", "Doing nothing")
    ct.insert("Rathesh ", "Doing noting")

    # checking record size and Capacity
    print("Number of records " + str(len(ct)))
    print("Capacity " + str(ct.capacity()))

    # do some search
    print(ct.search("ramesh"))
    print(ct.search("Balesh"))
    print(ct.search("Rath"))