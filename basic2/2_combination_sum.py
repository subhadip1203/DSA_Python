# https://leetcode.com/problems/combination-sum/


# my first solution

def calculateSum (candidates, target , i, result , current=[] , sum = 0):
    if sum == target:
        result.append(current.copy())
        return
    elif sum > target:
        return None
    else :
        item = candidates[i]
        current.append(item)
        sum = sum+item
        calculateSum (candidates, target , i+1, result , current , sum )
        

def combinationSum(candidates, target , result = []):
    for i in range(len(candidates)):
        calculateSum(candidates, target , i , result)
    return result


# from youtube : https://www.youtube.com/watch?v=OyZFFqQtu98
# fromyoutube : https://www.youtube.com/watch?v=GBKI9VSKdGg

  
# def combinationSum(candidates, target ):
#     result = []

#     def dfs(i = 0,current=[], sum=0) :
#         if sum == target :
#             result.append(current.copy())
#             return
#         elif sum > target  or i >= len(candidates):
#             return
#         else:
#             print("i",i)
#             item = candidates[i]
#             current.append(item)
#             dfs(i,current, sum+item) 
#             current.pop()
#             print('current',current)
#             print("i increased :",i+1)
#             dfs(i+1,current, sum) 
#     dfs()
#     return result

candidates = [2,3,6,7]
target = 8
print(combinationSum(candidates,target))