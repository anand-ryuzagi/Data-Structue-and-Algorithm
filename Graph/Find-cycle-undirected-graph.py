#finding cycle in a undirected graph using BFS transversal
#Status : 0 for not visited
#Status : 1 for visited
#Status : 2 for processed


from queue import Queue

class BreadthFirstSearch:
    def __init__(self,adj_list):
        self.adj_list = adj_list
        self.status = {}
        self.parent = {}
        self.queue = Queue()

        for vertices in adj_list:
            self.status[vertices] = 0
            self.parent[vertices] = None

    def bfsTransverse(self,source):
        self.status[source] = 1
        self.parent[source] = None
        self.queue.put(source)

        while not self.queue.empty():
            target_node = self.queue.get()
            self.status[target_node] = 2
            
            for neighbour in self.adj_list[target_node]:
                if self.status[neighbour] ==1:
                    return True
                if self.status[neighbour] == 0:
                    self.status[neighbour] = 1
                    self.parent[neighbour] = target_node
                    self.queue.put(neighbour)
                
        return False
        

    


if __name__ == '__main__':
    adj_list = {
    0:[1],
    1:[0,3],
    2:[3,4],
    3:[1,2,4],
    4:[2,3]
    }
    graph = BreadthFirstSearch(adj_list)
    if(graph.bfsTransverse(0)): print("cycle is present")
    else: print("Not a cycle")

    adj_list2 ={
        1:[4],
        2:[4],
        3:[4],
        4:[1,2,3,5],
        5:[4,6],
        6:[5]
    }
    graph2 = BreadthFirstSearch(adj_list2)
    if(graph.bfsTransverse(1)): print("cycle is present")
    else: print("Not a cycle")
