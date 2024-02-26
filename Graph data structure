class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
        else:
            raise KeyError("One or both vertices not found")

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].remove(vertex2)
            self.adj_list[vertex2].remove(vertex1)
        else:
            raise KeyError("One or both vertices not found")

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for v in self.adj_list[vertex]:
                self.adj_list[v].remove(vertex)
            del self.adj_list[vertex]
        else:
            raise KeyError("Vertex not found")

    def __str__(self):
        return str(self.adj_list)


# Example usage:
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')

graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'D')
graph.add_edge('D', 'A')

print("Graph:")
print(graph)

graph.remove_edge('B', 'C')

print("\nGraph after removing edge between B and C:")
print(graph)

graph.remove_vertex('A')

print("\nGraph after removing vertex A:")
print(graph)
