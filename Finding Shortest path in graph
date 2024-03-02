import heapq

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1][vertex2] = weight
            self.adj_list[vertex2][vertex1] = weight
        else:
            raise KeyError("One or both vertices not found")

    def astar(self, start, goal):
        open_set = [(0, start)]
        came_from = {}
        g_score = {vertex: float('inf') for vertex in self.adj_list}
        g_score[start] = 0
        f_score = {vertex: float('inf') for vertex in self.adj_list}
        f_score[start] = self.heuristic(start, goal)

        while open_set:
            current = heapq.heappop(open_set)[1]

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                return path[::-1]

            for neighbor in self.adj_list[current]:
                tentative_g_score = g_score[current] + self.adj_list[current][neighbor]

                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return None

    def heuristic(self, vertex, goal):
        # Example heuristic: Manhattan distance
        return abs(vertex[0] - goal[0]) + abs(vertex[1] - goal[1])

# Example usage:
graph = Graph()
graph.add_vertex((0, 0))
graph.add_vertex((0, 1))
graph.add_vertex((1, 0))
graph.add_vertex((1, 1))

graph.add_edge((0, 0), (0, 1), 1)
graph.add_edge((0, 0), (1, 0), 1)
graph.add_edge((0, 1), (1, 1), 1)
graph.add_edge((1, 0), (1, 1), 1)

start = (0, 0)
goal = (1, 1)

path = graph.astar(start, goal)
if path:
    print("Shortest path from", start, "to", goal, ":", path)
else:
    print("No path found from", start, "to", goal)
