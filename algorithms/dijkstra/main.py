def find_lowest_cost(costs, processed):
    l_node = None
    l_node_value = float("inf")
    for key, value in costs.items():
        if value < l_node_value and key not in processed:
            l_node_value = value
            l_node = key
    return l_node


def dijkstra(graph, start):
    processed = []
    costs = {**graph[start]}

    for key, _ in graph.items():
        if key == start:
            continue
        if key not in costs:
            costs[key] = float("inf")

    parents = {}
    for i in graph[start].keys():
        parents[i] = start

    while True:
        lowest_cost_node = find_lowest_cost(costs, processed)
        if lowest_cost_node is None:
            break
        neighbors = graph[lowest_cost_node].keys()
        for n in neighbors:
            if costs[n] > costs[lowest_cost_node] + graph[lowest_cost_node][n]:
                costs[n] = costs[lowest_cost_node] + graph[lowest_cost_node][n]
                parents[n] = lowest_cost_node
        processed.append(lowest_cost_node)
    # also return parent if needed
    return costs
