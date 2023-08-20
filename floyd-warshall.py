INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    dist = [[0 if i == j else graph[i][j] if graph[i][j] != 0 else INF for j in range(n)] for i in range(n)]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

# Example graph: adjacency matrix representation
graph = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]

all_pairs_shortest_paths = floyd_warshall(graph)
for row in all_pairs_shortest_paths:
    print(row)
