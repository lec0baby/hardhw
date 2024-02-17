from collections import deque


def bfs(graph, start, target, function):
    visited = set()
    queue = deque([(start, 0)])

    while queue:
        node, distance = queue.popleft()
        if function(node, target):
            return distance
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, distance + 1))

    return None