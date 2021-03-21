#BFS Breadth Search First transversal of a graph: a node is access by level 
# Visit source node and marked it as visited and add it to the queue. Now pop it out of the queue and find all the neighbours of the source node and if that node is not visited then add it to the visited and add to the queue. Repeat the same with all coming nodes in the queue until the queue is empty.

from queue import Queue
graph_adj_list = {
    "A":["B","D"],
    "B":["A",'C'],
    'C':['B'],
    'D':['A','E','F'],
    'E':['D','F','G'],
    'F':['D','E','H'],
    'G':['E','H'],
    'H':['G','F']
}

class BreadthSearchFirst:
    def __init__(self,adj_list, source):
        self.adj_list = adj_list
        self.source = source
        self.visited = {}
        self.parent ={}
        self.level = {}
        self.final_output = []
        self.queue = Queue()

        for key in adj_list.keys(): #initialize the visited dict, parent dic and level dict according to the number of nodes in the graph
            self.visited[key] = False
            self.parent[key] = None
            self.level[key] = -1
    
    def bsftransverse(self): 
        #initialize the start values to the source node
        self.visited[self.source] = True
        self.parent[self.source] = None
        self.level[self.source] = 0
        self.queue.put(self.source)

        #will lookup the whole graph untill the queue is empty
        while not self.queue.empty():
            #pop out the first node in the queue and find all its neighbours.
            target_node = self.queue.get()
            self.final_output.append(target_node)
            
            #finding the neighbours of the pop out value
            for neighbor_node in self.adj_list[target_node]:
                if self.visited[neighbor_node] == False:
                    self.visited[neighbor_node] = True
                    self.parent[neighbor_node] = target_node
                    self.level[neighbor_node] = self.level[target_node]+1
                    self.queue.put(neighbor_node)
        
        print(self.final_output)
    
    
    def shortestDistanceFromSource(self,node): #find level of current node from the source node
        return self.level[node]

    def shortestPathFromSource(self,node): #find the path from the source node to the destination node
        self.node = node
        path = []
        while self.node is not None:
            path.append(self.node)
            self.node = self.parent[self.node]
        path.reverse()
        return path


graph = BreadthSearchFirst(graph_adj_list,"A")
graph.bsftransverse()
print(graph.shortestDistanceFromSource("G"))
print(graph.shortestPathFromSource("H"))
