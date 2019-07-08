

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
    # Gets the hash value (index) from the hash function
    key_hash = hash_table.hash_djb2(key)
    # Converts the passed-in parameters into an array
    key_value = [key, value]
    
    if hash_table.elements[key_hash] is None:
        hash_table.elements[key_hash] = Pair(key, value)
        return True
    else:
        for pair in hash_table.elements[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return True
        hash_table.elements[key_hash].append(key_value)
        return True


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    pass


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    pass


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
