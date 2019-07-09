

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * self.capacity
        
# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):                                    
    hash = 5381
    for char in string:
        hash = (( hash << 5) + hash) + ord(char)
    return hash % max
  

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    # Uses the 'hash()' function to get the index where the 
    #   the passed-in 'value' parameter will be inserted at.
    index = hash(key, hash_table.capacity)
    # Creates a new pair and sets it to a new variable
    pair = Pair(key, value)
    # Creates a variable to represent the key/value pair at the index
    stored_pair = hash_table.storage[index]
    # If the bucket at 'index' is not empty... 
    if hash_table.storage[index] is not None:
        # ...and if the passed-in "key" is NOT the same as the "key" in the
        #    bucket...
        if pair.key != stored_pair.key:
            # ...print a warning indicating that it isn't empty
            print("Warning, index at " + str(index) + " is not empty!")
    # Set the value of that key (from the bucket) equal to the passed-in
    #   "key"
    hash_table.storage[index] = pair


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
# def hash_table_remove(hash_table, key):
#     # Uses the 'hash()' function to get the index value in order to 
#     #   access & delete the value at the passed-in 'key' parameter
#     index = hash(key, hash_table.capacity)
#     # If the cell at that 'index' (the index value) is empty, which
#     #   means that the desired key/value pair doesn't exist... 
#     if hash_table.storage[index] is None:
#         # ...return 'False' because there's nothing to delete!
#         return False
#     # ...if the cell at that 'index' is NOT empty, then iterate through
#     #    the pairs at that cell (using 'range' which gives you access to the
#     #    index of an item for deletion)...
#     for i in range(0, len(hash_table[index])):
#         # ...if the passed-in 'key' parameter DOES exist within the items
#         #   at this cell...
#         if hash_table[index][i][0] == key:
#             hash_table[index].pop(i)
#             return True

# '''
# Fill this in.

# Should return None if the key is not found.
# '''
# def hash_table_retrieve(hash_table, key):
#     # Uses the 'hash()' function to get the index value in order to 
#     #   access & retrieve a value for the passed-in 'key' parameter
#     index = hash(key, hash_table.capacity)
#     # If the cell at that 'index' (the index value) is empty... 
#     if hash_table.storage[index] is None:
#         # Iterate through each pair in that cell to check if the passed-in
#         #   'key' parameter is equal to any of them...
#         for pair in hash_table.storage[index]:
#             # ...if the passed-in 'key' parameter DOES already exists...
#             if pair[0] == key:
#                 # ...return that value
#                 return pair[1]
#     # If the passed-in 'key' parameter does not exist in the cell at that
#     #   index, return 'None'
#     return None

def Testing():
    print(hash("hello world", 10))
    print(hash("how are you today?", 10))
    
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    # hash_table_remove(ht, "line")

    # if hash_table_retrieve(ht, "line") is None:
    #     print("...gone tomorrow (success!)")
    # else:
    #     print("ERROR:  STILL HERE")


Testing()
