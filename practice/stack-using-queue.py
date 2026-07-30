from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.queue = deque()

    # O(n)
    def push(self, item):
        self.queue.append(item)

        # Rotate the queue so that the new element comes to the front
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    # O(1)
    def pop(self):
        if len(self.queue) == 0:
            return "Stack is empty"
        return self.queue.popleft()

    # O(1)
    def peek(self):
        if len(self.queue) == 0:
            return "Stack is empty"
        return self.queue[0]

    # O(1)
    def is_empty(self):
        return len(self.queue) == 0

    # O(1)
    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(list(self.queue))


# Driver Code
stack = StackUsingQueue()

print(f"Is stack empty? {stack.is_empty()}")

stack.push(100)
stack.push(200)
stack.push(300)
stack.push(400)

print(f"Stack = {stack}")
print(f"Top = {stack.peek()}")
print(f"Size = {stack.size()}")

print(f"Popped = {stack.pop()}")
print(f"Stack = {stack}")

print(f"Popped = {stack.pop()}")
print(f"Stack = {stack}")

stack.push(500)
print(f"After pushing 500 = {stack}")

print(f"Top = {stack.peek()}")

print(f"Popped = {stack.pop()}")
print(f"Popped = {stack.pop()}")
print(f"Popped = {stack.pop()}")

print(f"Stack = {stack}")
print(f"Is stack empty? {stack.is_empty()}")

print(f"Popped = {stack.pop()}")