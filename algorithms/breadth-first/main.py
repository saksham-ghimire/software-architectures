from collections import deque


def breadth_first(graph, element, start):
    queue = deque()
    queue += graph[start]
    processed = []
    while queue:
        e = queue.popleft()
        if e in processed:
            continue
        if e == element:
            return f"Found"
        else:
            if graph.get(e, None) is not None:
                queue += graph.get(e)
        processed.append(e)
    return f"Not found"


print(
    breadth_first(
        graph={"you": ["a", "b", "c"], "a": ["d", "e"]}, element="e", start="you"
    )
)
