from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,value):
        self.container.append(value)

    def pop(self):
        self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def show(self):
        return self.container
