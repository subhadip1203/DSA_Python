"""
Check if a undirected graph is cyclic ot not

"""

def find_cycle(paths):
    # create graph tree
    graph_tree = {}

    for node1,node2 in paths:
        if node1 not in graph_tree:
            graph_tree[node1]= []
        graph_tree[node1].append(node2)

        if node2 not in graph_tree:
            graph_tree[node2]= []
        graph_tree[node2].append(node1)

    # create DFS function
    visited = {}
    def checkCycle(current, parent):

        #check if visited
        if current in visited and visited[current] == True:
            return True

        # if not visisted , mark visisted
        visited[current] = True

        # do DFs call again on child
        for child in graph_tree[current]:
            if child == parent:
                continue
            else:
                if checkCycle(child, current):
                    return True
                
        return False


    # call DFS function
    if checkCycle(1,1) : 
        return True
    else:
        return False





paths = [
    [1,3],
    [3,4],
    [2,3],
    [3,6],
    [6,7],
    [7,8],
    [8,3]
]
print(find_cycle(paths))


