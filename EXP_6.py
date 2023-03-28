from collections import defaultdict


class Graph:
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # defining function which will add the graph
    def addEdgetoGraph(self, x, y):
        self.graph[x].append(y)

    # defining function to print BFS traverse
    def BFSearch(self, n):
        # initially marking all vertices are not visited
        visited_vertices = [False] * len(self.graph)
        # creating a queue for visited vertices
        queue = []
        visited_vertices[n] = True
        queue.append(n)
        while queue:
            # popping the element from the queue which is printed
            n = queue.pop(0)
            print(n, end=" ")
            # getting vertices adjacent to the vertex n which is dequeued
            for c in self.graph[n]:
                if not visited_vertices[c]:
                    queue.append(c)
                    visited_vertices[c] = True


# initializing a graph
graph = Graph()
n = int(input("Enter no.of edges: "))
for i in range(0, n):
    v1 = int(input("Enter v1 value: "))
    v2 = int(input("Enter v2 value: "))
    graph.addEdgetoGraph(v1, v2)

initial = int(input("Enter initial vertex: "))
print(" the Breadth First Search Traversal for the Graph is as Follows: ")
graph.BFSearch(initial)
