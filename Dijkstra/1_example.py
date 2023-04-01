from  heapq import heappush , heappop , heapify
import sys

def dijkstra(nodes , source ):
    # get the path for optimal route, trace back to source node
    minPQ = []

    # Visited Nodes
    visitedNodes = {}
    
    #costs
    calculatePath = {}

    for x in nodes:
        calculatePath[x]= { 'costs' : 999999999 , 'pre' : None , 'index': None }
    calculatePath[source]['costs']=0
    calculatePath[source]['pre']=source
    calculatePath[source]['index'] = 0
    
    #pushing source , where distance from source to source is zero
    heappush(minPQ, (0, source))

    while len(minPQ) > 0:
        smallestHeap = heappop(minPQ)
        currentNodeDistance = smallestHeap[0]
        currentNodeName = smallestHeap[1]
        
        visitedNodes[currentNodeName] = True

        for childName in nodes[currentNodeName]:
            if childName not in visitedNodes:
                childPathDistance = nodes[currentNodeName][childName]+ currentNodeDistance
                # updating the calculatedPath dict
                if childPathDistance < calculatePath[childName]['costs']:
                    calculatePath[childName]['costs']= childPathDistance
                    calculatePath[childName]['pre']= currentNodeName
                    
                    #if already in heap before, not fresh node
                    if calculatePath[childName]['index'] != None:
                        index = calculatePath[childName]['index']
                        minPQ[index][0] = childPathDistance
                        heapify(minPQ)
                    # freah node
                    else:
                        heappush(minPQ, (childPathDistance, childName))
                        currentIndex = len(minPQ)-1
                        calculatePath[childName]['index'] = currentIndex
    print(calculatePath)

node = {
    'a' : {'b' : 2, 'c' : 1},
    'b' : { 'a':2 , 'c':3 , 'd': 8 },
    'c' : {'a': 4, 'b':3  ,'e':  5, 'd': 2} ,
    'd' : {'b': 8 , 'c': 2, 'e': 11 ,'f':22 },
    'e' : {'c': 5 ,'d': 11 ,'f': 1},
    'f' : {'d': 22 , 'e': 1}
}
source = 'a'
destination = 'f'
dijkstra(node , source)