# HashTable implementation with string keys and simple hashing function
def calculate_hash_value(string):
    return ord(string[0]) * 100 + ord(string[1])


class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    def store(self, string):
        hash_value = calculate_hash_value(string)
        if self.table[hash_value]:
            if string not in [self.table[hash_value]]:
                self.table[hash_value].append([string])
        else:
            self.table[hash_value] = list()
            self.table[hash_value].append([string])

    def lookup(self, string):
        hash_value = calculate_hash_value(string)
        if self.table[hash_value]:
            if [string] in self.table[hash_value]:
                return hash_value
        return -1


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 7469
print(calculate_hash_value('JERRY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('JERRY'))

# Test store
hash_table.store('JERRY')
# Should be 7469
print(hash_table.lookup('JERRY'))

# Test store edge case
hash_table.store('JERRIE')
# Should be 7469
print(hash_table.lookup('JERRIE'))
