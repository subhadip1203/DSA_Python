'''
Leetcode : https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.


'''



class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def dfs (node ,memo):
    if node.val in memo :
        return memo[node.val]
    else:
        cloneNode = Node(node.val)
        memo[node.val] = cloneNode

        for neighbor in node.neighbors:
            cloneNode.neighbors.append( dfs(neighbor, memo))
        
        return cloneNode

class Solution:
    def cloneGraph(self, node):
        memo = {}
        return dfs(node, memo) if node else None
