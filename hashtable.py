#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.count = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n) Need to go through all buckets to get each value from all key-value pairs"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n) Need to go through each bucket to get all key-value pairs"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                values.append(value)
        return values
    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) to run throgh all buckets to return allkey-value pairs"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(1) because count is incremented by 1 whenever the set() method is called, therefore no need to travel through eah bucket"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        return self.count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(n/b) because you have to try each item in a bucket"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        try:
            self.get(key)
        except KeyError:
            return False
        else:
            return True

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: O(n/b) to run through each item(s) in a bucket"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        item, bucketLinkedList = self.get_item(key)
        if item:
            return item[1]
        else:
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(n/b) need to traverse through each item(s) in a bucket"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        item, bucketLinkedList = self.get_item(key)
        if item:
            bucketLinkedList.replace(item, (key, value))
        else:
            bucketLinkedList.append((key, value))
            self.count += 1

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(n/b) because I have to traerse through each item(s) in each bucket"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        item, bucketLinkedList = self.get_item(key)
        if item:
            bucketLinkedList.delete(item)
            self.count -= 1
        else:
            raise KeyError('Key not found: {}'.format(key))

    def get_item(self, key):
        bucketLinkedList = self.buckets[self._bucket_index(key)]
        item = bucketLinkedList.find(lambda node: node[0] == key)
        return item, bucketLinkedList


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
