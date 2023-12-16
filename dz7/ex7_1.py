from collections import deque
from typing import Callable, Any


def bfs(graph: dict[Any, list], start, target, function: Callable[Any, Any]) -> int | None:
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