def dfs_pass(graph, src, explored, order=None, components=None, leader=None):
    explored.add(src)

    if components != None and leader != None:
        components[leader].append(src)

    for edge in graph_get(graph, src):
        if edge not in explored:
            dfs_pass(graph, edge, explored, order, components, leader)

    if order != None:
        order.append(src)

def graph_get(graph, node):
    try:
        return graph[node]
    except KeyError:
        return []

def graph_set(graph, src, dest):
    try:
        graph[src].append(dest)
    except KeyError:
        graph[src] = [dest]


def graph_reverse(graph):
    new_graph = {}

    for node in graph:
        for edge in graph_get(graph, node):
            graph_set(new_graph, edge, node)

    return new_graph


def find_strong_components(graph):
    explored = set([])
    reversed_graph = graph_reverse(graph)
    order = []

    for node in reversed_graph:
        if node not in explored:
            dfs_pass(reversed_graph, node, explored, order)

    del reversed_graph
    explored.clear()

    components = {}

    for node in reversed(order):
        if node not in explored:
            components[node] = []
            dfs_pass(graph, node, explored, None, components, node)

    return components

def dfs_first_pass(graph, src, visited):
    order = []
    order_tracking = set([])
    stack = []
    stack.append(src)

    while len(stack):
        top = stack[-1]
        edges = graph_get(graph, top)
        visited.add(top)
        trigger = True

        for edge in edges:
            if edge not in visited:
                stack.append(edge)
                trigger = False;
                break

        if trigger:
            order.append(stack.pop())

    return order

def dfs_second_pass(graph, src, visited, components, leader):
    stack = []
    stack.append(src)
    components[leader] = set([])

    while len(stack):
        top = stack[-1]
        edges = graph_get(graph, top)
        visited.add(top)
        components[leader].add(top)
        trigger = True

        for edge in edges:
            if edge not in visited:
                stack.append(edge)
                trigger = False;
                break

        if trigger:
            stack.pop()

# An iterative approach that avoids blowing up the stack when operating
# on large graphs
def find_iterative(graph):
    reversed_graph = graph_reverse(graph)
    visited = set([])
    order = []
    components = {}

    for node in reversed_graph:
        if node not in visited:
            order += dfs_first_pass(reversed_graph, node, visited)


    del reversed_graph
    visited.clear()

    for node in reversed(order):
        if node not in visited:
            dfs_second_pass(graph, node, visited, components, node)

    return components
