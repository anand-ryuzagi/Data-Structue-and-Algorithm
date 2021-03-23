#Topological sort using kahn's algorithm.

from queue import Queue

class TopologicalSort:
    def __init__(self,adj_list,num_nodes):
        self.adj_list = adj_list
        self.num_nodes = num_nodes
        self.indegree = [0 for i in range(self.num_nodes)]
        self.topological = []
        self.queue = Queue()

    def kahnSort(self):
        for key in self.adj_list.keys():
            for to in self.adj_list[key]:
                self.indegree[to] = self.indegree[to]+1

        # print(self.indegree)
        
        for i in range(len(self.indegree)-1):
            if self.indegree[i] == 0:
                self.queue.put(i)

        while not self.queue.empty():
            no_dependents = self.queue.get()
            self.topological.append(no_dependents)

            for to in self.adj_list[no_dependents]:
                self.indegree[to] = self.indegree[to] - 1
                if self.indegree[to] == 0:
                    self.queue.put(to)
        
        if len(self.topological) != self.num_nodes:
            return 0
        return self.topological


if __name__ == '__main__':
    test_case1 ={
        2:[0,4],
        0:[1,3],
        4:[3,5],
        3:[1],
        5:[1],
        1:[]
    }
    topo = TopologicalSort(test_case1,6)
    print(topo.kahnSort())
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    test_case2 ={
        2:[0,4],
        0:[3],
        4:[3,5],
        3:[1],
        5:[1],
        1:[0]
    }
    topo = TopologicalSort(test_case2,6)
    print(topo.kahnSort())
