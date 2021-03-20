#Adjacency List representation of weighted directed graph.

class Graph:
    def __init__(self):
        self.list = {}

    def createEdge(self,start,end,weight):
        if start in self.list:
            self.list[start].append((end,weight))
        else:
            self.list[start] = [(end,weight)]

    def display(self):
        for i in self.list:
            print(i, '->','->'.join(str(j) for j in self.list[i]))

if __name__ == '__main__':
    g = Graph()
    g.createEdge(0,1,45)
    g.createEdge(0,2,12)
    g.createEdge(0,2,32)
    g.createEdge(1,4,64)
    g.createEdge(2,3,78)
    g.createEdge(3,5,90)
    g.createEdge(4,5,99)
    g.display()
