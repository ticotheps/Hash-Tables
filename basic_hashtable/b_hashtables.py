

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __str__(self):
        return f'key: {self.key}, value: {self.value}'


# '''
# Basic hash table
# Fill this in.  All bucket values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        # self.count = 0
        self.all_buckets = [None] * capacity
        
# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, capacity):                                    
    hash = 5381
    for char in string:
        hash = (( hash << 5) + hash) + ord(char)
    return hash % capacity
  

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    # Uses the 'hash()' function to get the hashed_index where the 
    #   the passed-in 'value' parameter will be inserted at.
    hashed_index = hash(key, hash_table.capacity)
    # Creates a new pair and sets it to a new variable
    pair_in_hand = Pair(key, value)
    # Creates a variable to represent the key/value pair_in_hand at the hashed_index
    pair_in_bucket = hash_table.all_buckets[hashed_index]
    # If the bucket at 'hashed_index' is not empty... 
    if pair_in_bucket is not None:
        # ...and if the passed-in "key" is NOT the same as the "key" in the
        #    bucket...
        if pair_in_hand.key != pair_in_bucket.key:
            # ...print a warning indicating that it isn't empty
            print("Warning, hashed_index at " + str(hashed_index) + " is not empty!")
    # Set the value of that key (from the bucket) equal to the passed-in
    #   "key"
    hash_table.all_buckets[hashed_index] = pair_in_hand
    print(pair_in_hand)

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    # Uses the 'hash()' function to get the hashed_index in order to 
    #   access & delete the value for the passed-in 'key' parameter
    hashed_index = hash(key, hash_table.capacity)
    # If the cell at that 'hashed_index' (the hashed_index value) is empty, which
    #   means that the desired key/value pair doesn't exist... 
    # If the bucket at 'hashed_index' is empty OR the ... 
    if (hash_table.all_buckets[hashed_index] is None or
            hash_table.all_buckets[hashed_index].key != key):
        print("Unable to remove item with key " + key)
    else:
        hash_table.all_buckets[hashed_index] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    # Uses the 'hash()' function to get the hashed_index in order to 
    #   access & retrieve a value for the passed-in 'key' parameter
    hashed_index = hash(key, hash_table.capacity)
    # If the bucket at 'hashed_index' is not empty... 
    if hash_table.all_buckets[hashed_index] is not None:
        # ...and if the key in the bucket is the same as the passed-in key...
        if hash_table.all_buckets[hashed_index].key == key:
            return hash_table.all_buckets[hashed_index].value
      
    print("Unable to find value with key " + key)
    return None


def Testing():
    # print(hash("hello world", 10))
    # print(hash("how are you today?", 10))
    
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
