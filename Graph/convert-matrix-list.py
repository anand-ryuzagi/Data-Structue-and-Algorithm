#practice to convert a adjacency matrix into a adjacency list

class Node:
    def __init__(self, fromkey, key, weight):
        self.fromkey = fromkey
        self.key = key
        self.weight = weight

    def getdetails(self):
        return f"{self.fromkey} | {self.key} | {self.weight}"

    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def setFromKey(self, fromkey):
        self.fromkey = fromkey

    def getFromKey(self):
        return self.fromkey

    def setWeight(self, weight):
        self.weight = weight

    def getWeight(self):
        return self.weight


class PrimAlgo:
    def __init__(self,nodes):
        self.nodes = nodes
        self.adj_list = {}

    def addEdge(self,fromKey,toNode):
        if fromKey not in self.adj_list:
            self.adj_list[fromKey] = []

        self.adj_list[fromKey].append(toNode)

    def adj_matrixToadj_list(self,matrix):
        length = len(matrix)
        for i in range(length):
            for j in range(length):
                if matrix[i][j] != 0:
                    self.addEdge(i, Node(i, j, matrix[i][j]))

    def printAdj_list(self):
        for i in range(len(self.adj_list)):
            for j in self.adj_list[i]:
                print(i, j.getdetails())
            print("-------------------------------------------")
            



if __name__ == '__main__':
    matrix = [
        [0, 5, 2, 0, 0, 0, 0],
        [5, 0, 10, 0, 6, 0, 0],
        [2, 10, 0, 15, 9, 0, 0],
        [0, 0, 15, 0, 8, 0, 0],
        [0, 0, 9, 8, 0, 11, 5],
        [0, 6, 0, 0, 11, 0, 0],
        [0, 0, 0, 0, 5, 0, 0]
    ]
    pa = PrimAlgo(7)
    pa.adj_matrixToadj_list(matrix)
    pa.printAdj_list()
