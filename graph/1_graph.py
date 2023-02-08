
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


# BFS: Breadth First Search
def mapBFS(adj_list, source):
    level ={}
    parents = {}
    visited ={}
    path = []
    que = Queue()

    for key in adj_list:
        level[key] = -1
        visited[key] = False
        parents[key] = None
    
    level[source] = 1
    visited[source] = True
    que.put(source)

    while not que.empty():
        u = que.get()
        path.append(u)
        for v in adj_list[u]:
            if not visited[v]:
                visited[v] = True
                parents[v] = u
                level[v] = level[u]+1
                que.put(v)

    return {
        "level" : level,
        "visited" : visited,
        "parents" : parents
    }

result = mapBFS(adj_list,"a")
print(result)