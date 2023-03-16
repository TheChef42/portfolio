# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from dll_sentinel import DLLSentinel


class ChainedHashTable:

    def __init__(self, m, hash_func=hash, get_key_func=None):
        """Initialize each slot with a linkedlist.

        Arguments:
        m -- size of hashtable
        hash_func -- hash function to use. If omitted, uses the builtin	Python function 'hash'.
        get_key_func -- an optional function that returns the key for the
        objects stored. May be a static function in the object class. If
        omitted, then the identity function is used.
        """
        self.m = m
        self.table = [None] * m
        # Initialize every slot in the table with a linked list.
        for i in range(m):
            self.table[i] = DLLSentinel(get_key_func)
        self.hash_function = hash_func
        # If not provided a get_key function, return the object as the key.
        if get_key_func is None:
            self.get_key = lambda x: x
        else:
            self.get_key = get_key_func

    def insert(self, data):
        """Insert an object into the linked list at the appropriate table slot."""
        self.table[self.hash_function(self.get_key(data)) % self.m].prepend(data)

    def search(self, key, data):
        """Return an object with a given key or None if not found."""
        return self.table[self.hash_function(key) % self.m].search(key, data)

    def delete(self, node):
        """Delete an object with a given key from the linked list at the appropriate table slot."""
        self.table[self.hash_function(self.get_key(node.data)) % self.m].delete(node)

    def __str__(self):
        """Return the string representation of this hash table, looking like a Python list."""
        string = "["
        if self.m > 0:
            for i in range(self.m - 1):
                string += str(self.table[i]) + ", "
            string += str(self.table[self.m - 1])
        string += "]"
        return string


# Press the green button in the gutter to run the script.
if __name__ == "__main__":

    from key_object import KeyObject
    from hash_functions import division_hash

    N = int(input("Input the N, which is the amount of values. "))

    # Hashtable of integers.
    hashtable1 = ChainedHashTable(N, get_key_func=KeyObject.get_key)
    print(hashtable1)
    amount_duplicated = 0

    for i in range(N):
        x = input()
        x = x.replace(" ", "")
        key = int(x, 2) % 8
        if str(hashtable1.search(key, x)) == x:
            amount_duplicated += 1
            continue
        hashtable1.insert(KeyObject(x, key))

    print(amount_duplicated)
    print(str(hashtable1).replace(", ", " ").replace("[", "").replace("]", "").replace("None", "").replace("  ", "", 1).replace("  ", "\n").replace(" ", "\n"))




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
