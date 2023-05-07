import heapq


def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                print("=>",pq)

    return distances


node = {
    'a' : {'b' : 4, 'c' : 1},
    'b' : { 'a':4 , 'c':1 , 'd': 8 },
    'c' : {'a': 1, 'b':1 ,'e':  5, 'd': 2} ,
    'd' : {'b': 8 , 'c': 2, 'e': 11 ,'f':22 },
    'e' : {'c': 5 ,'d': 11 ,'f': 1},
    'f' : {'d': 22 , 'e': 1}
}
source = 'a'
destination = 'b'
print(calculate_distances(node , source))