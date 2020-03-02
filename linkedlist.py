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
        if self.head == Node(item):
          self.tail = self.head
        else:
          current = self.head
          self.head = Node(item)
          self.head.net = current
          



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
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        current_node = self.head
        previous = None

        found = False

        while current_node:
          if self.head.data == item:
            if self.head.next is not None:
              self.head = self.head.next
              found = True
              break

        if self.head == None: # Checks if this is an empty list
          raise ValueError('Item not found: {}'.format(item))
        else:
          if self.head.data == item: # Checks if head node is the item
            self.head = self.head.next # Reassigns head node to node after previous head
            if self.head == None: # Checks if tail node is item 
              self.tail = self.head
            return
          node = self.head # Points to the first node within list
          locked_on = False # Random variable with boolean variable
          while node.next != None: # loop goes through list of nodes 
            if node.next.data == item: # If data from node is same as item looked for
              locked_on = True # Somewhat visual change to represent item has been found
              break
            node = node.next # Otherwise move on to the next node
          if locked_on:
            if node.next == self.tail: # This automatically checks if tail node is the correct node with item that is being looked for
              self.tail = node
              node.next = None
              return
            temp_var = node.next # Assigns next pointer to equal the node after the deleted node then deletes temp variable
            del temp_var
          else:
            raise ValueError('Item not found: {}'.format(item))

    def replace(self, item, new_data):
      found = False
      current_node = self.head

      while current_node is not None:
        if current_node.data == item:
          current_node.data = new_data
          return True
        current_node = current_node.next
      if not found:
        raise ValueError('Item was not found: {}'.format(item))    


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
