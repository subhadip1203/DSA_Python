'''
Leetcode : https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
'''
class Node:
    def __init__(self, val = 0):
        self.val = val
        self.neighbors = []

class Solution:
    def __init__(self):
        self.memo={}
    
    def cloneGraph(self, node):
        if  node.val in self.memo:
            return self.memo[node.val]
        else:
            currentNode =Node(node.val)
            for n in node.neighbors:
                currentNode.neighbors.append(self. cloneGraph(self, n))
            self.memo[node.val] = currentNode
            return currentNode