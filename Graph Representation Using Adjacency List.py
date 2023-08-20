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

    def print_adj_list(self):
        for vertex, neighbors in self.adj_list.items():
            print(vertex, "->", neighbors)

V = int(input("Enter the number of vertices: "))
E = int(input("Enter the number of edges: "))
graph = Graph(V)
for _ in range(E):
    u, v = map(int, input().split())
    graph.add_edge(u, v)
graph.print_adj_list()
