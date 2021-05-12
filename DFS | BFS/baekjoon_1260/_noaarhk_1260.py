from collections import deque
from typing import List


def dfs(g, start):
    visited = {}
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.setdefault(node)
            stack.extend(g[node])
    return list(visited.keys())


def solution(l: List):
    n, m, v = l[0]

    def _graph(l: List):
        graph = {i: [] for i in range(1, n + 1)}

        for i in range(1, m + 1):
            x, y = l[i]

            graph[x].append(y)
            graph[y].append(x)

        for key in graph:
            graph[key].sort()
        # print(graph)
        return graph

    print('DFS : ', dfs(_graph(l), v))




if __name__ == '__main__':
    # n, m, v = map(int, input().split())
    _input = [
        [4, 5, 1],
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 4],
        [3, 4]
    ]
    solution(_input)
