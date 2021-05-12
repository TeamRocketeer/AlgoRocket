from queue import Queue

graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}


def ex_BFS(graph, start_node):
    visit = []
    queue = Queue

    queue.append(start_node)

    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return visit


def ex_DFS(graph, start_node):
    visit = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
            # can be expressed as below
            # for i in graph[node]:
            #   stack.append(i)

    return visit


