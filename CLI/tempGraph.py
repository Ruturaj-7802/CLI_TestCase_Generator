def components(edges):
    graph = {}
    
    for edge in edges:
        u, v = edge
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)

    def dfs(node, visited, component):
        visited[node] = True
        component.append(node)
        for neighbor in graph.get(node, []):
            if not visited[neighbor]:
                dfs(neighbor, visited, component)

    visited = {node: False for node in graph}
    components_vertices = []

    for node in graph:
        if not visited[node]:
            component = []
            dfs(node, visited, component)
            components_vertices.append(component)

    return components_vertices

# Example usage:
# edges= [[1, 10], [10, 2], [2, 3], [2, 4], [4, 7], [5, 8], [8, 9], [9, 6]]
edges = [[1,2], [2,3],[2,4], [4,5]]

components_vertices = components(edges)
print("Vertices in Connected Components:")
print(components_vertices)
