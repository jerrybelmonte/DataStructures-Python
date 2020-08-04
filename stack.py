# Stack implementation using a LinkedList data structure.
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

    def insert_first(self, new_element):
        if self.head:
            new_element.next = self.head
            self.head = new_element
        else:
            self.head = new_element

    def delete_first(self):
        if self.head:
            delete_element = self.head
            self.head = self.head.next
            delete_element.next = None
            return delete_element
        else:
            return None


class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        remove_element = self.ll.delete_first()
        return remove_element


# Test cases
# Set up some Elements
element_1 = Element(1)
element_2 = Element(2)
element_3 = Element(3)
element_4 = Element(4)

# Start setting up a Stack
stack = Stack(element_1)

# Test stack functionality
stack.push(element_2)
stack.push(element_3)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())
stack.push(element_4)
print(stack.pop().value)
