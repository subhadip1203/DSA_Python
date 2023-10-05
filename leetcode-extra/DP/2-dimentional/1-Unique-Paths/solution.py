class Solution:
    def uniquePaths(self, m, n):
        arr = [[0 for _ in range(m)] for _ in range(n)]

        arr[0][0]= 1 

        for i in range(n):
            for j in range(m):
                if i+1 < n:
                    arr[i+1][j] +=  arr[i][j]
                if j+1 < m:
                    arr[i] [j+1] +=  arr[i][j]

        return arr[n-1][m-1]


       



m = 3
n = 7
print( Solution().uniquePaths(m,n))