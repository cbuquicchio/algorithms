def _search_recur(graph, src, explored):
    explored.append(src)

    for edge in graph[src]:
        if edge not in explored:
            _search_recur(graph, edge, explored)

def search(graph, src):
    order = []
    _search_recur(graph, src, order)

    return order
