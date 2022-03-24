def Queue_bfs(start_v):
    visited = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for i in graph[v]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    return visited
