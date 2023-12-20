# https://www.geeksforgeeks.org/python-program-for-rat-in-a-maze-backtracking-2/

def findPath(row, column, maze, current_path, result):
    # path to go will be  Down Left Right Up

    if row ==len(maze)-1 and column == len(maze[0])-1 :
        result.append(current_path)
    
    # for going Down
    if row+1 < len(maze) and maze[row+1][column] == 1:
        findPath(row+1, column, maze, current_path+'D' , result)
    
    # for going Left
    if column-1 <=0  and maze[row][column-1] == 1:
        findPath(row, column-1, maze, current_path+'L' , result)

    # for going Right
    if column+1 < len(maze[0])  and maze[row][column+1] == 1:
        findPath(row, column+1, maze, current_path+'R', result)

    # for going Up
    if row-1 <= 0  and maze[row-1][column] == 1:
        findPath(row-1, column+1, maze, current_path+'U', result)



   





result = []
m = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]


findPath(0, 0, m, '',result)
print(result)