#DFS  Depth First Search transversal of a graph: The algorithm starts at the root node and explores as far as possible along each branch before backtracking. 

# Visit source node and marked it as visited and add it to the stack. Now pop it out of the stack and find all the neighbours of the source node and if that node is not visited then add it to the visited and add to the stack. Repeat the same with all coming nodes in the stack until the stack is empty.

# It focuses on the last value in the stack or you can say that it focuses to reach out the last node as possible.


class DepthFirstSearch:
    def __init__(self,adj_list):
        self.adj_list = adj_list
        self.visited = {}
        self.parent = {}
        self.stack = []
        self.final_output = []

        for vertices in adj_list:
            self.visited[vertices] = False
            self.parent[vertices] = NotImplemented

    def dfsTransverse(self,source):
        self.visited[source] = True
        self.parent[source] = None
        self.stack.append(source)

        while len(self.stack) !=0:
            target_node = self.stack.pop()
            self.final_output.append(target_node)

            for neighbour in self.adj_list[target_node]:
                if self.visited[neighbour] == False:
                    self.visited[neighbour] = True
                    self.parent[neighbour] = target_node
                    self.stack.append(neighbour)
        
        print(self.final_output)
    
    def shortestPath(self,node):
        self.node = node
        path = []
        while self.node is not None:
            path.append(self.node)
            self.node = self.parent[self.node]
        path.reverse()
        print(path)

if __name__ == '__main__':
    adj_list = {
    0:[1,2,3],
    1:[0,3],
    2:[0,3],
    3:[0,1,2,4],
    4:[3]
    }
    graph = DepthFirstSearch(adj_list)
    graph.dfsTransverse(0)
    graph.shortestPath(4)
