from collections import defaultdict, deque

def topological_sort(graph):
    indegree = [0] * len(graph)
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1
    
    queue = deque()
    for node, degree in enumerate(indegree):
        if degree == 0:
            queue.append(node)
    
    topological_order = []
    while queue:
        node = queue.popleft()
        topological_order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return topological_order
