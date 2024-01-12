from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


myTree = Node(20)
myTree.left = Node(8)
myTree.right = Node(22)
myTree.left.left = Node(5)
myTree.left.right = Node(3)
myTree.right.right = Node(25)
myTree.left.right.left = Node(10)
myTree.left.right.right = Node(14)


def BFS(root):

    result = []

    q = deque( [root] if root else [] )

    while q:
        level = []
        current_queue_length = len(q)
        for item in range(current_queue_length):
            currentNode = q.popleft()
            level.append(currentNode.val)
 
            if currentNode.left:
                q.append(currentNode.left)
            if currentNode.right:
                q.append(currentNode.right)

        if len(result) %2 == 0:
            result.append(level)
        else:
            result.append(list(reversed(level)))

    return result


print(BFS(myTree))



