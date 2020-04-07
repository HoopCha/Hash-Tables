# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        #Create the hashed key
        hash_key = self._hash_mod(key)
        #Create a node with the key and value
        node = LinkedPair(key,value)
        #Create the current bucket using the hash_key
        current = self.storage[hash_key]

        #If the list is not empty
        while current:
            #If buckets key is equal to the key
            if current.key == key:
                #Update the value to the new value
                current.value = value
                return
            #Else if the next item in the bucket is none
            elif current.next == None:
                #Set that next item in the bucket to the node
                current.next = node
                return
            #Otherwise cycle to the next item in the bucket amd start again
            else:
                current = current.next
        #Otherwise put the node into the list 
        self.storage[hash_key] = node




    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hash_key = self._hash_mod(key)
        if not self.storage[hash_key]:
            return "The key is not found here!"
        current = self.storage[hash_key]
        last = self.storage[hash_key]
        while current:
            if current.key == key:
                if current.key != last.key:
                    last.next = current.next
                else:
                    self.storage[hash_key] = current.next
                return
            last = current
            current = current.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hash_key = self._hash_mod(key)
        if not self.storage[hash_key]:
            return None
        current = self.storage[hash_key]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        for node in old_storage:
            while node:
                self.insert(node.key, node.value)
                node = node.next



testarr =

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
