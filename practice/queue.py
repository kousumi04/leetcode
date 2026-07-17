class Queue:
    def __init__(self):
        self.items = []

    # O(1)
    def is_empty(self):
        return len(self.items) == 0

    # O(1) (for append)
    def enqueue(self, item):
        self.items.append(item)

    # O(n) for list.pop(0)
    def dequeue(self):
        if self.is_empty():
            return "Cannot dequeue, queue is empty"
        return self.items.pop(0)

    # O(1)
    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]

    # O(1)
    def rear(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[-1]

    # O(1)
    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


queue = Queue()

queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)

print(f"Queue content = {queue}")
print(f"Dequeued item = {queue.dequeue()}")
print(f"Queue content = {queue}")
print(f"Front item = {queue.front()}")
print(f"Rear item = {queue.rear()}")
print(f"Queue is empty = {queue.is_empty()}")
print(f"Queue size = {queue.size()}")