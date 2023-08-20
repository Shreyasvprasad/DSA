from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

V = int(input("Enter the number of vertices: "))
E = int(input("Enter the number of edges: "))
graph = Graph(V)
for _ in range(E):
    u, v = map(int, input().split())
    graph.add_edge(u, v)
start_vertex = int(input("Enter the start vertex for BFS: "))
print("BFS traversal starting from vertex", start_vertex, ":")
graph.bfs(start_vertex)
