
# undirectedPath
# check if exists a path between nodeA and nodeB.
# using BFS

from collections import deque

class Queue:
    def __init__(self):
        self.collection = deque()
        self.length = 0
    
    def push(self,data):
        self.collection.append(data)
        self.length = self.length + 1
    
    def pop(self):
        if self.length > 0:
            self.length = self.length -1
            return self.collection.popleft()
        else:
            return None  


    
def makeAdjecencyList(edges):
    result = {}
    for x in edges:
        first = x[0]
        second = x[1]
        if first not in result: result[first] = []
        if second not in result: result[second] = []
        
        result[first].append(second)
        result[second].append(first)
    
    return result



def undirectedPath(edges , start , end):
    adjList = makeAdjecencyList(edges)
    alreadyVisited = {}
    myQueue = Queue()
    myQueue.push(start)

    while myQueue.length > 0 :
        current = myQueue.pop()
        if current == end :
            return True
        else:
            if current not in alreadyVisited:
                alreadyVisited[current] = True
                if current in adjList:
                    for edge in adjList[current]:
                        myQueue.push(edge)

    return False

# edges = [
#   ['i', 'j'],
#   ['k', 'i'],
#   ['m', 'k'],
#   ['k', 'l'],
#   ['o', 'n']
# ]

# edges = [
#   ['i', 'j'],
#   ['k', 'i'],
#   ['m', 'k'],
#   ['k', 'l'],
#   ['o', 'n']
# ]

edges = [
  ['i', 'j'],
  ['k', 'i'],
  ['m', 'k'],
  ['k', 'l'],
  ['o', 'n']
]

print(undirectedPath(edges, 'i', 'o' ))