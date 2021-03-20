#Adjacency List representation of directed graph.

class Graph:
    def __init__(self):
        self.list = {}

    def createEdge(self,start,end):
        if start in self.list:
            self.list[start].append(end)
        else:
            self.list[start] = [end]

    def display(self):
        for i in self.list:
            print(i, '->','->'.join(str(j) for j in self.list[i]))

if __name__ == '__main__':
    g = Graph()
    g.createEdge(0,1)
    g.createEdge(0,2)
    g.createEdge(1,4)
    g.createEdge(2,3)
    g.createEdge(3,5)
    g.createEdge(4,5)
    g.display()
