
'''
two sum question
where multiple answers can be there
but no deplicate
'''

def twoSum( nums, target):
    sortArr = sorted(nums)
    start = 0
    end = len(sortArr)-1

    results = set()
    while start < end :
        if sortArr[start] + sortArr[end] == target:
            results.add((sortArr[start],sortArr[end])) 
            start +=1 
            end -= 1
            continue
        elif sortArr[start] + sortArr[end] > target :
            end -= 1
        elif sortArr[start] + sortArr[end] < target :
            start += 1
    
    return results






nums = [1,2,7,8,11,1,8,15]
target = 9
print(twoSum( nums, target))