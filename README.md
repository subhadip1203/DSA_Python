
# shortcut

If given a linked list then
1. Two pointers

If the input array is sorted then
1. Binary search
2. Two pointers

If asked for all permutations/subsets then
1. Backtracking

If given a tree or a graph then
1. DFS
2. BFS

If recursion is banned then
1. Stack

If must solve in-place then
1. Swap corresponding values
2. Store one or more different values in the same pointer

If asked for maximum/minimum subarray/subset/options then
1. Dynamic programming

If asked for top/least K items then
1. Heap

If asked for common strings then
1. Map
2. Trie

General Tips
1. Map/Set for O(1) time & O(n) space
2. Sort input for O(nlogn) time and O(1) space


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

