# Queue implementation using a list data structure
class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.insert(0, new_element)

    def peek(self):
        return self.storage[len(self.storage) - 1]

    def dequeue(self):
        return self.storage.pop()


# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Output should be 1
print(q.peek())

# Test dequeue
# Output should be 1
print(q.dequeue())

# Test enqueue
q.enqueue(4)
# Output should be 2
print(q.dequeue())
# Output should be 3
print(q.dequeue())
# Output should be 4
print(q.dequeue())
q.enqueue(5)
# Output should be 5
print(q.peek())
