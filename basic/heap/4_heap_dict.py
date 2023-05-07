from heapq  import heappush ,heappop
 
my_heap = []
heappush(my_heap, (2, "wake up"))
heappush(my_heap, (1, "stop sleeping"))
heappush(my_heap, (10, "put a little makeup"))
heappush(my_heap, (9, "you wanted to"))
 
print(my_heap)
print(heappop(my_heap)[1])
print(heappop(my_heap))
