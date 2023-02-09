from queue import Queue

adj_list = {
    "a" : ["b","d"],
    "b" : ["a","c"],
    "c" : ["b"],
    "d" : ["a","e","f"],
    "e" : ["d","f","g"],
    "f" : ["d","e","h"],
    "g" : ["e","h"],
    "h" : ["g","f"]
}

color = {}  # w - not visisted , g - currenty visiting , b - already visisted
parents = {}
step = {}
dfs_travarsal_output = []

time = 0


for node in adj_list:
    color[node] = "w"
    parents[node] = None
    step[node] = [-1,-1]


def DFS(adj_list, root):
    global time
    color[root] = 'g'
    step[root][0] = time
    dfs_travarsal_output.append(root)
    time = time+1

    for subNode in adj_list[root]:
        if color[subNode] == 'w':
            parents[subNode] = root
            DFS(adj_list, subNode)


    color[root] = 'b'
    step[root][1] = time
    time = time+1

DFS(adj_list, 'a')
print(step)