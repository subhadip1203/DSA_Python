
'''
youtube : https://www.youtube.com/watch?v=73sneFXuTEg&t=100s
'''


from collections import  deque

def find_topological_sort (myList,num):

    # keep track of which items are child of how many nodes
    dependency_list = [ 0 for i in range (num) ]
    # dependency_list become like this
    # dependency_list = [0, 0, 0, 0, 0, 0]
  
    
    
    # for dependency list
    adj_list = {}
    for source, destination in myList:
        if source not in adj_list:  adj_list[source] = []
        adj_list[source].append(destination)
        dependency_list[destination] += 1
    # adj_list  become like this :
    # adj_list = {
    #   5 : [0,2],
    #   2 : [3],
    #   3: [1]
    # }
    # -----------------------------------------------------
    # and dependency_list = [2, 2, 1, 1, 0, 0]
    # means 
    # 0  and 1has 2 parents
    # 2 and 3  has 1 parents
    #  4 and 5 has no parents




    # to store only those item , who have no dependencies
    my_queue = deque()
    for i in range (num):
        if dependency_list[i] == 0:
            my_queue.append(i)
    # only added 4 ,5 as these have no parents and dependencies



    result = []
    while len(my_queue)  > 0:
        first_element = my_queue.popleft()
        result.append(first_element)
        if first_element in adj_list:
            for child in adj_list[first_element]:
                dependency_list[child] -= 1
                if dependency_list[child] == 0:
                    my_queue.append(child)
        
    return result



myList = [
    [5,2],
    [2,3],
    [3,1],
    [5,0],
    [4,0],
    [4,1]
]
num = 6
print(find_topological_sort (myList , num))


