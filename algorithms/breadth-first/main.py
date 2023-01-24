from collections import deque


def breadth_first(graph, element, start):
    queue = deque()
    # for empty graph ..
    if graph.get(start, None) is None:
        return f"not found"
    queue += graph[start]
    processed = []
    while queue:
        e = queue.popleft()
        if e in processed:
            continue
        if e == element:
            return f"found"
        else:
            if graph.get(e, None) is not None:
                queue += graph.get(e)
        processed.append(e)

    return f"not found"
