class Node :
    def __init__(self, data):
        self.data = data
        self.left =None
        self.right=None
    def printData(self):
        print(self.data)


a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.printData()
