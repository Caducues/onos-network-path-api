import heapq

def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    visited = set()

    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]
        if node == end:
            return path
        for adjacent, weight in graph.get(node, {}).items():
            if adjacent not in visited:
                heapq.heappush(queue, (cost + weight, adjacent, path))
    return None
