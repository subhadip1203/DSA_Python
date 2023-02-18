from collections import deque

class Stack():
    
    def __init__(self):
        self.container = deque()
        self.lemgth = 0

    def apend(self,data):
        self.container.append(data)
        self.lemgth += 1
    
    def pop(self):
        if self.lemgth > 0:
            self.lemgth -= 1
            return self.container.pop()
        else: 
            return None
    
myStack = Stack()
print(myStack.pop())
