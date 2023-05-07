
# double-ended queue
# lits a dobly link-list
# appends and pops from either side  with O(1) performance
# 

from collections import deque

stack = deque()
print("Start : ",stack)
stack.append(1)
stack.append(10)
stack.append(20)
print("After Append : ",stack)
popResult = stack.pop()
print("popresult : ",popResult)
print("After pop : ",stack)

stack = deque()
stack.appendleft("a")
stack.appendleft("b")
print(stack)
print("After AppendLeft : ",stack)
popLeftResult = stack.popleft()
print("popLeftResult : ",popLeftResult)
print("After popLeft : ",stack)

stack = deque()
