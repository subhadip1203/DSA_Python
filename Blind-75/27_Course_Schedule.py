
'''
Leetcode : https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] 
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''


class Solution:
    def canFinish(self, numCourses, prerequisites):
        preMap = {i : [] for i in range(numCourses)}
        for (start,end) in prerequisites:
            preMap[start].append(end)
        
        visited = set()

        def dfs(item) :
            if item in visited:
                return False
            elif preMap[item] == []:
                return True
            else:
                visited.add(item)
                for ele in preMap[item]:
                    status = dfs(ele) 
                    if status == False :
                        return False
                visited.remove(item)
                preMap[item] = []
                return True
        
        for item in range(numCourses):       
            if dfs(item) :
                return False
        return True







numCourses = 2
prerequisites = [[1,0]]

print( Solution().canFinish(numCourses,prerequisites))