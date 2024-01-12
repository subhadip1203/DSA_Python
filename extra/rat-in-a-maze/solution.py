def findPath(row, column, maze, current_path, result, memo):
    if row == len(maze) - 1 and column == len(maze[0]) - 1:
        result.append(current_path)


    # for going Down
    if row + 1 < len(maze) and maze[row + 1][column] == 1 and memo[row + 1][column] == 0:
        memo[row + 1][column] = 1
        findPath(row + 1, column, maze, current_path + 'D', result, memo)
        memo[row + 1][column] = 0

    # for going Left
    if column - 1 >= 0 and maze[row][column - 1] == 1 and memo[row][column - 1] == 0:
        memo[row][column - 1] = 1
        findPath(row, column - 1, maze, current_path + 'L', result, memo)
        memo[row][column - 1] = 0

    # for going Right
    if column + 1 < len(maze[0]) and maze[row][column + 1] == 1 and memo[row][column + 1] == 0:
        memo[row][column + 1] = 1
        findPath(row, column + 1, maze, current_path + 'R', result, memo)
        memo[row][column + 1] = 0

    # for going Up
    if row - 1 >= 0 and maze[row - 1][column] == 1 and memo[row - 1][column] == 0:
        memo[row - 1][column] = 1
        findPath(row - 1, column, maze, current_path + 'U', result, memo)
        memo[row - 1][column] = 0


result = []
m = [
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1]
]


memo = [[0 for i in range(len(m[0]))] for j in range(len(m))]
memo[0][0] = 1  # Starting point
findPath(0, 0, m, '', result, memo)
print(result)
