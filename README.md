
# Deque

Deque (Doubly Ended Queue). Retriving or removing both end is O(1) time complexity. 
- append()
- appendleft()
- pop()
- popleft()


### Deque Usage

```python

from collections import deque

# Stack implementation
stack = deque()
stack.append(1)
stack.append(10)
popResult = stack.pop()
print(popResult)



# Queue implementation
queue = deque()
stack.append(1)
stack.append(10)
popResult = stack.popleft()
print(popResult)

```
<hr> 
<hr> 



# Stack

Its work principle First-In-Last-Out . we can use deque to make a stack

```python

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
    
    def print(self):
        print(self.collection)
    
myStack = Stack()
myStack.apend(10)
myStack.apend(20)
myStack.apend(30)
print(myStack.pop())

```
<hr> 
<hr> 


# Queue

Its work principle First-In-First-Out . we can use deque to make a Queue

```python

from collections import deque

class Queue():
    
    def __init__(self):
        self.container = deque()
        self.lemgth = 0

    def apend(self,data):
        self.container.append(data)
        self.lemgth += 1
    
    def pop(self):
        if self.lemgth > 0:
            self.lemgth -= 1
            return self.container.popleft()
        else: 
            return None
    
    
myQueue = Queue()
myQueue.push(1)
myQueue.push(2)
myQueue.push(3)
myQueue.print()
print(myQueue.pop())

```
<hr> 
<hr> 

# Array 

Its work principle First-In-First-Out . we can use deque to make a Queue

```python

# all zero array
arr = [0 for element in range(5)]

# all None array
arr = [None for element in range(5)]

# two diemntinal array
arr = a = [[0]*3]*3
# it will change all the sub array
arr[1][1] = 3  


# non reference array copy 
arr  = [ [0] * 3 for _ in range(3)]

```
<hr> 
<hr> 

