
def binarySearch(myArr , searchNum):
    start = 0
    end = len(myArr)-1

    if myArr[start] == searchNum:
        print('found mid at ',start)
    elif myArr[end] == searchNum:
        print('found mid at ',end)
    
    else: 
        while start < end-1:
            mid = (start+end)//2
            if searchNum == myArr[mid]:
                print('found mid at', mid)
                break
            elif searchNum < myArr[mid] :
                end = mid
            else:
                start = mid
    
        


myArr = [1,2,3,4,5,6,7,8,9]
for x in myArr:     
    binarySearch(myArr , x)

