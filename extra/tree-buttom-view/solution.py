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


position_dict = {}
minimum = {"val" : 0}
maximum = {"val" : 0}

def buttom_view(treeHead , minimum, maximum):
    q = deque()
    q.append((treeHead, 0))
    while q:
        current =  q.popleft()
        current_node = current[0]
        current_position = current[1]
        position_dict[current_position] = current_node.val
        minimum["val"] = min(minimum["val"]  , current_position)
        maximum["val"] = max(maximum["val"] , current_position)
        if current_node.left:
            q.append( (current_node.left , current_position-1) )

        if current_node.right:
            q.append( (current_node.right , current_position+1) )

buttom_view(myTree, minimum, maximum)
print(minimum, maximum)
i = minimum["val"] 

result = []
while i <= maximum["val"] :
    if position_dict[i]:
        result.append(position_dict[i])
    i+= 1

print(result)



        
