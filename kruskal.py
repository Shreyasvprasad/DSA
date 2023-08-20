class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def find_parent(self, parent, node):
        if parent[node] == -1:
            return node
        return self.find_parent(parent, parent[node])

    def union(self, parent, u, v):
        parent_u = self.find_parent(parent, u)
        parent_v = self.find_parent(parent, v)
        parent[parent_u] = parent_v

    def kruskal(self):
        self.edges.sort(key=lambda edge: edge[2])
        parent = [-1] * self.vertices
        mst = []
        for edge in self.edges:
            u, v, weight = edge
            if self.find_parent(parent, u) != self.find_parent(parent, v):
                self.union(parent, u, v)
                mst.append(edge)
        return mst

V = int(input("Enter the number of vertices: "))
E = int(input("Enter the number of edges: "))
graph = Graph(V)
for _ in range(E):
    u, v, weight = map(int, input().split())
    graph.add_edge(u, v, weight)
minimum_spanning_tree = graph.kruskal()
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)
