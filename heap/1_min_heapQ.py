import heapq

data = [10,20,43,1,2,65,44,2,3,14]

heapq.heapify(data)
print(data)

# if you are at index   = i
# Index of parent       = (i-1)/2
# Index of first child  = 2i+1
# Index of Second child = 2i+2

minVal = heapq.heappop(data)
print(minVal)
print(data)
