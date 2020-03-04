#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        node = self.head # assign new variable
        distance = 0
        if self.head == None: # Checking head node if it contains None
          return 0
        while node != None: # If node doesn't contain None
          distance += 1
          node = node.next # Reassigns node from previous node to new node until node = None
        return distance

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        if self.head == None: # If head node is None, then assigns the new item given into the head and tail node, which are both the same
          self.head = Node(item)
          self.tail = self.head
        else: # If head node doesn't contain None, continue to the next node, reassign current tail node to equal new node and reassigns its tail to be tail.next
          self.tail.next = Node(item)
          self.tail = self.tail.next

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        new = Node(item)
        if self.is_empty():
          self.head = new
          self.tail = new
          return
        new.next = self.head
        self.head= new
          



    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        if self.head == None:
          print('List is empty') # List returns None, so empty list
          return
        else:
          node = self.head 
          while node != None: # Checks if node has None for data 
            if quality(node.data): # If quality data function returns true using node.data
              return node.data # return this node's data
            node = node.next # Continue to next node
          print('Cannot find, sorry') # If information cannot be found
          return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        if self.is_empty():
          raise ValueError(f'Item not found: {item}')
          return
        currentNode = self.head
        if currentNode.data == item:
          self.head = currentNode.next
          if currentNode.next == None:
            self.tail = None
          return
        previous_node = None
        while currentNode != None:
          if currentNode.data == item:
            if currentNode.next == None:
              self.tail = previous_node
            previous_node.next = currentNode.next
            return
          previous_node = currentNode
          currentNode = currentNode.next
          print(currentNode)
        raise ValueError(f'Item not found: {item}')

    def replace(self, new_data):
      for item in self.items():
        if item[0] == new_data[0]:
          print(f'Replacing {item} with: {new_data}')
          self.delete(item)
        else:
          continue
        self.append(new_data)    


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
