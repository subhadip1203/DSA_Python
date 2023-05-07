from collections import deque

class Queue():
    def __init__(self):
        self.collection = deque()
        self.length = 0
    
    def push(self,data):
        self.collection.append(data)
        self.length += 1

    def pop(self):
        if self.length > 1:
            self.length -= 1
            return self.collection.popleft()
        
    def print(self):
        print(self.collection)


myQueue = Queue()
print(myQueue.pop())
myQueue.push(1)
myQueue.push(2)
myQueue.push(3)
myQueue.print()
print(myQueue.pop())
myQueue.print()

