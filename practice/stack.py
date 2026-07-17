class Stack:
    def __init__(self):
        self.items = []

    # O(1)
    def is_empty(self):
        return len(self.items) == 0

    # O(1)
    def push(self, item):
        self.items. append(item)

    # O(1)
    def pop(self):
        if self.is_empty():
            return "Cannot pop, stack is empty"
        return self.items.pop()

    # O(1)
    def peek(self):
        if self.is_empty():
            return "Cannot find top, stack is empty"
        return self.items[-1]

    # O(1)
    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


stack = Stack()

stack.push(5)
stack.push(10)
stack.push(15)

print(f"Stack content = {stack}")
print(f"Popped item = {stack.pop()}")
print(f"Stack content = {stack}")
print(f"Stack item after pop = {stack.peek()}")
print(f"Stack is empty = {stack.is_empty()}")