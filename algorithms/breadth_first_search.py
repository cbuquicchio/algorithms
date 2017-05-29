def bfs(graph, source):

    # records distance from source and
    # keeps track of visited vertices
    level = { source: 0 }
    parent = { source: None }
    breadth = [source]
    i = 1

    while breadth:
        next = []

        for u in breadth:
            for v in graph[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)

        breadth = next
        i += 1

    return level, parent
