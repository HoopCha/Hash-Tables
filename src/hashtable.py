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
        #Create the hashed key
        hash_key = self._hash_mod(key)
        #Create current and previous pointers
        current = self.storage[hash_key]
        previous = None

        #While in the bucket
        while current:
            #If the current key matches the key you want to remove and the previous exists
            if current.key == key and previous:
                #Set the previous to the current next, therefore removing the one between them from the link
                previous.next = current.next
                return
            #Else if the current key matches the key oyu want to remove but previous doesnt exist (aka the first item in the bucket) 
            elif current.key == key and not previous:
                #Set the bucket equal to the next item
                self.storage[hash_key] = current.next
                return
            #If neither of those happen, set previous to current, and move current to the next one, and repeat
            previous = current
            current = current.next
        #If not found at all return error
        return "Key not found"


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        #Create the hashed key
        hash_key = self._hash_mod(key)
        #Create the current bucket using the hash_key
        current = self.storage[hash_key]

        #While in the bucket
        while current:
            #If the current key is equal to the key you want to retrieve
            if current.key == key:
                #Return it
                return current.value
            #Otherwise keep cycling through the bucket
            current = current.next
        #Otherwise return none
        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        #Set an old storage that is equal to the current one
        old_storage = self.storage
        #Double the capacity of the hashtable
        self.capacity *= 2
        #Set the new storage
        self.storage = [None] * self.capacity

        #For each item in the old storage
        for item in old_storage:
            #Go through it and:
            while item:
                #Insert each item
                self.insert(item.key, item.value)
                #Get next item
                item = item.next



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
