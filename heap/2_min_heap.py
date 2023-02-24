class MinHeap:
    def __init__(self,capacity):
        self.storage = [None] *capacity
        self.capacity = capacity
        self.currentSize = 0

    # if you are at index   = i
    # Index of parent       = (i-1)/2
    # Index of first child  = 2i+1
    # Index of Second child = 2i+2
    
    def parentIndex(self,i):
        parentIndex = (i-1)//2
        if parentIndex >= 0 :
            return parentIndex
        else:
            return None
    
    def leftChildIndex(self,i):
        leftChildIndex = 2*1+1
        if leftChildIndex < self.capacity :
            return leftChildIndex
        else:
            return None
    
    def rightChildIndex(self,i):
        rightChildIndex = 2*1+2
        if  rightChildIndex < self.capacity :
            return  rightChildIndex
        else:
            return None
    
    def isFull(self):
        if self.capacity == self.currentSize :
            return True
        return False
    
    def swapIndexValue(self,i,j):
        self.storage[i] , self.storage[j] = self.storage[j] , self.storage[i]
    
    def getParentValue(self,i):
        parentIndex = self.parentIndex(i)
        if parentIndex != None:
            return self.storage[parentIndex]
        else:
            return None
        
    # Function to insert a node into the heap
    def addData(self, element):
        if self.isFull():
             raise("capacity full , not possible to add ")
        
        self.storage[self.currentSize] = element
        self.currentSize+= 1
        current = self.currentSize -1
        while self.parentIndex(current)  != None and self.getParentValue(current) > self.storage[current] :
            self.swapIndexValue(current, self.parentIndex(current))
            current = self.parentIndex(current)

    
    def printHeap(self):
        print(self.storage)


myHeap = MinHeap(5)
myHeap.printHeap()
myHeap.addData(5)
myHeap.printHeap()
myHeap.addData(2)
myHeap.printHeap()
myHeap.addData(6)
myHeap.printHeap()
myHeap.addData(10)
myHeap.printHeap()
myHeap.addData(1)
myHeap.printHeap()
