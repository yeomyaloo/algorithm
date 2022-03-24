def recursive_dfs(v, visited = []):
    visited.append(v)
    for i in graph[v]:
        if i not in visited:
            visited = recursive_dfs(i, visited)
        return visited