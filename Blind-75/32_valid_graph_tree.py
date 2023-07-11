"""
Lintcode : https://www.lintcode.com/problem/178/

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to check whether these edges make up a valid tree.
"""


"""
a graph tree is valid if :
1. no circle is there
2. no unconnected node is there
"""

class Solution:
    def valid_tree(self, n, edges):
        
        # make the graph
        graph_tree = {}
        for i in range (n):
            graph_tree[i] = []

        # populate the graph
        for source, destination in edges:
            graph_tree[source].append(destination)
            graph_tree[destination].append(source)


        # DFS
        visited = {}
        def isCycle(current,parent):
            # check visisted
            if current in visited and visited[current] == True:
                return True

            #mark visisted
            visited[current] = True

            #call DFS
            for node in  graph_tree[current]:
                if node == parent:
                    continue
                elif isCycle(node,current):
                    return True
            return False



        # call DFS
        if isCycle(0,0):
            return False
        
        if len(visited) == n:
           return True
        else:
            return False

n = 5 
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print( Solution().valid_tree(n,edges))


n = 5 
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
print( Solution().valid_tree(n,edges))