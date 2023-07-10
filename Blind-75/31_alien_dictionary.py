"""
video source : https://www.youtube.com/watch?v=IIgisEKjCKA

"""


def alien_order(words):

    # make the graph
    char_graph = {}
    for word in words:
        for char in word :
            char_graph[char] = []

    # populate the graph
    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]
        min_word_length = min(len(word1), len(word2))

        if len(word1) != len(word2) and word1[:min_word_length] == word2[:min_word_length]:
            return ''
        for j in range (min_word_length):
            if word1[j] != word2[j]:
                char_graph[word1[j]].append(word2[j])


    # DFS
    visited = {}
    result = []
    def dfs(c):
        
        # check
        if c in visited:
            return visited[c]
       
        # mark as visited
        visited[c] = True

        # call DFS again
        for neighbour in char_graph[c]:
           if  dfs(neighbour) : 
               return True

        # remove as visited after dfs completed
        visited[c] = False
        result.append(c)
        return False


    # iterate the graph
    for c in char_graph:
        if dfs(c): return ""

    result.reverse()
    return "".join(result)





words = ['wrt' , 'wrf' , 'er', 'ett', 'rftt']
print(alien_order(words))