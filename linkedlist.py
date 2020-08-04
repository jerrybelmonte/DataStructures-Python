# LinkedList implementation using a helper Element class
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        index = 1
        current = self.head
        if self.head:
            while current.next and index < position:
                current = current.next
                index += 1
        if index == position:
            return current
        else:
            return None

    def insert(self, new_element, position):
        index = 1
        current = self.head
        previous = current
        if position != 1:
            while current.next and index < position:
                previous = current
                current = current.next
                index += 1
            if index == position:
                new_element.next = current
                previous.next = new_element
        else:
            if self.head:
                new_element.next = current
                self.head = new_element
            else:
                self.head = new_element

    def delete(self, value):
        current = self.head
        if self.head:
            if current.value == value:
                self.head = current.next
                current.next = None
            else:
                while current.next:
                    previous = current
                    current = current.next
                    if current.value == value:
                        previous.next = current.next
                        current.next = None


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Output should print 3
print(ll.head.next.next.value)
# Output should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4, 3)
# Output should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Output should print 2 now
print(ll.get_position(1).value)
# Output should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)
