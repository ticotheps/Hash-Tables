

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
        self.elements = [None] * self.capacity
        
# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash_djb2(string):
    hash = 5381
    for x in string:
        hash = (hash * 33) + ord(x)
    return hash
  

# def hash(string, max):
#     pass

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    # Gets the index value that the passed-in 'value' will be inserted at
    # Uses the 'hash_djb2()' function to get the index value where the 
    #   the passed-in 'value' parameter will be inserted at.
    key_hash = hash_table.hash_djb2(key)
    # Converts the passed-in parameters (key, value) into a list that can
    #   be inserted at the 'key_hash'
    key_value = [key, value]
    # If the cell at 'key_hash' (the index value) is empty... 
    if hash_table.elements[key_hash] is None:
        # Insert a new list, AT THAT INDEX (key_hash), containing the
        #   values of the passed-in 'key' and 'value' parameters
        hash_table.elements[key_hash] = list([key_value])
        return True
    # If the cell at 'key_hash' is NOT empty...
    else:
        # Iterate through each pair in that cell to check if the passed-in
        #   'key' parameter is equal to any of them...
        for pair in hash_table.elements[key_hash]:
            # ...if the passed-in 'key' parameter already exists...
            if pair[0] == key:
                # ...update its value to the passed-in 'value' parameter
                pair[1] = value
                return True
        # If the passed-in 'key' parameter DOES NOT ALREADY exist within the
        #   list of pairs at that cell, then it is a NEW key, which we will
        #   append to that cell in the hash_table.
        hash_table.elements[key_hash].append(key_value)
        return True


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    # Uses the 'hash_djb2()' function to get the index value in order to 
    #   access & delete the value at the passed-in 'key' parameter
    key_hash = hash_table.hash_djb2(key)
    # If the cell at that 'key_hash' (the index value) is empty, which
    #   means that the desired key/value pair doesn't exist... 
    if hash_table.elements[key_hash] is None:
        # ...return 'False' because there's nothing to delete!
        return False
    # ...if the cell at that 'key_hash' is NOT empty, then iterate through
    #    the pairs at that cell (using 'range' which gives you access to the
    #    index of an item for deletion)...
    for i in range(0, len(hash_table[key_hash])):
        # ...if the passed-in 'key' parameter DOES exist within the items
        #   at this cell...
        if hash_table[key_hash][i][0] == key:
            hash_table[key_hash].pop(i)
            return True

# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    # Uses the 'hash_djb2()' function to get the index value in order to 
    #   access & retrieve a value for the passed-in 'key' parameter
    key_hash = hash_table.hash_djb2(key)
    # If the cell at that 'key_hash' (the index value) is empty... 
    if hash_table.elements[key_hash] is None:
        # Iterate through each pair in that cell to check if the passed-in
        #   'key' parameter is equal to any of them...
        for pair in hash_table.elements[key_hash]:
            # ...if the passed-in 'key' parameter DOES already exists...
            if pair[0] == key:
                # ...return that value
                return pair[1]
    # If the passed-in 'key' parameter does not exist in the cell at that
    #   key_hash, return 'None'
    return None

def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
