#  good explaination of heap 
# https://www.section.io/engineering-education/heap-data-structure-python/

class MaxHeap:
    def __init__(self, capacity):
        self.arr = [None]*capacity
        self.maxIndex = capacity-1
        self.currentIndex = None

    # if you are at index   = i
    # Index of parent       = (i-1)/2
    # Index of first child  = 2i+1
    # Index of Second child = 2i+2

    def getParentIndex(self,i):
        index = (i-1)//2
        if  index >= 0:
            return index
        return None
    
    def getParentValue(self,i):
        parentIndex = self.getParentIndex(i)
        if parentIndex is not None:
            return self.arr[parentIndex]
        return None
    
    
    def leftChildIndex(self,i):
        leftIndex = 2*i+1
        if leftIndex <=  self.maxIndex:
            return leftIndex
        return None
    
    def getLeftChildValue(self,i):
        leftIndex = self.leftChildIndex(i)
        if leftIndex is not None:
            return self.arr[leftIndex]
        return None
    
    def rightChildIndex(self,i):
        rightIndex = 2*i+2
        if rightIndex <=  self.maxIndex:
            return rightIndex
        return None
    
    def getRightChildValue(self,i):
        rightIndex = self.rightChildIndex(i)
        if rightIndex is not None:
            return self.arr[rightIndex]
        return None

    def hepifyUp(self):
        tempIndex = self.currentIndex
        while self.getParentValue(tempIndex) and self.getParentValue(tempIndex) < self.arr[tempIndex]:
            #exchange value of parent and child
            parentIndex = self.getParentIndex(tempIndex)
            self.arr[parentIndex] , self.arr[tempIndex] = self.arr[tempIndex] , self.arr[parentIndex]
            # make parent Index as tempIndex
            tempIndex = parentIndex

    def addData(self, val):
        if self.currentIndex == self.maxIndex:
            raise("capacity full")
        else:
            if self.currentIndex is None:
                self.currentIndex = 0
            else:
                self.currentIndex += 1

            self.arr[self.currentIndex] = val
            self.hepifyUp()

    def heapifyDown(self,currentIndex):
        leftIndex = self.leftChildIndex(currentIndex)
        rightIndex = self.rightChildIndex(currentIndex)
        if leftIndex > self.currentIndex :
            return
        else:
            if self.getLeftChildValue(currentIndex) and self.getLeftChildValue(currentIndex) > self.arr[currentIndex] :
                self.arr[currentIndex] , self.arr[leftIndex] = self.arr[leftIndex] , self.arr[currentIndex]
                self.heapifyDown(leftIndex)
            
            if self.getRightChildValue(currentIndex) and self.getRightChildValue(currentIndex) > self.arr[currentIndex] :
                self.arr[currentIndex] , self.arr[rightIndex] = self.arr[rightIndex] , self.arr[currentIndex]
                self.heapifyDown(rightIndex)
    
    def getMaxData(self):
        if self.currentIndex > 0 :
            maxdata = self.arr[0]
            self.arr[0] , self.arr[self.currentIndex] = self.arr[self.currentIndex] , None
            self.currentIndex = self.currentIndex -1
            self.heapifyDown(0)
            return maxdata
        elif self.currentIndex == 0:
            maxdata = self.arr[0]
            self.arr[0] = None
            self.currentIndex = None
            return maxdata
        else:
            raise("empty heap")

    def print(self):
        print(self.arr)




myHeap = MaxHeap(10)
myHeap.addData(20)
myHeap.addData(15)
myHeap.print()
myHeap.addData(13)
myHeap.addData(11)
myHeap.print()
myHeap.addData(30)
myHeap.addData(40)
myHeap.print()
print( myHeap.getMaxData() )
myHeap.print()
