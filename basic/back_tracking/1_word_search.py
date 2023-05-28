'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

'''

def search(board,i,j,word, word_index = 0 , visited = None):
    if visited == None : 
        visited = {}
    row_count = len(board) 
    col_count= len(board[0]) 
    word_lengh = len(word)
    
    key = str(i)+str(j)
    
    if  word_index == word_lengh :
        return True
    if i < row_count and j < col_count and i >=0 and j >= 0  and visited.get(key, None) == None and  word[word_index] == board[i][j] :
        visited[key] = True
        print(i,j, board[i][j],  word_index , word[word_index] , key)
        if search(board,i+1,j,word, word_index+1, visited) :
            return True
        if search(board,i-1,j,word, word_index+1 , visited) :
            return True
        if search(board,i,j+1,word, word_index+1 , visited) :
            return True
        if search(board,i,j-1,word, word_index+1 , visited) :
            return True
    visited[key] = None
    return False

def isExists(board, word):
    rows = len(board)
    col = len(board[0])
    for i in range(rows):
        for j in range(col):
            print("----")
            if search(board,i,j,word) :
                return True
    return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(isExists(board, word))

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(isExists(board, word))

board = [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]]
word = "aaaaaaaaaaaaa"
print(isExists(board, word))