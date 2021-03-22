#finding cycle in a directed graph using DFS transversal
# Whiteset = set contains all the unvisited vertices
# greyset = set contains all the visited vertices
# balckset = set contains all the processed vertices(include after all the adjacent of it is processed) 


from queue import Queue

class DepthFirstSearch:
    def __init__(self,adj_list):
        self.whiteset = set([key for key in adj_list.keys()])
        self.greyset = set()
        self.blackset = set()
        self.adj_list =adj_list

    def iscycle(self):
        while len(self.whiteset) != 0:
            current = next(iter(self.whiteset))
            if self.dfs(current,self.whiteset,self.greyset,self.blackset,self.adj_list):
                return True
        return False


    def dfs(self,current,whiteset,greyset,blackset,adj_list):
        self.greyset.add(current)
        self.whiteset.remove(current)
        for neighbour in adj_list[current]:
            if neighbour in self.blackset:
                continue
            if neighbour in self.greyset:
                return True
            if self.dfs(neighbour,whiteset,greyset,blackset,adj_list):
                return True
        self.blackset.add(current)
        self.greyset.remove(current)
        return False



if __name__ == '__main__':
    adj_list = {
    0:[1],
    1:[2,3,4],
    2:[],
    3:[2],
    4:[5],
    5:[6],
    6:[4]
    }
    graph = DepthFirstSearch(adj_list)
    if(graph.iscycle()): print("cycle is present")
    else: print("cycle is not present")
