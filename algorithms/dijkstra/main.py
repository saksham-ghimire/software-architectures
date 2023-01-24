processed = []


def find_lowest_cost(costs):
    l_node = None
    l_node_value = float("inf")
    for key, value in costs.items():
        if value < l_node_value and key not in processed:
            l_node_value = value
            l_node = key
    return l_node


def dijkstra(graph, start):
    costs = {**graph[start]}

    for key, value in graph.items():
        if key == start:
            continue
        for i in value.keys():
            costs[i] = float("inf")

    parents = {}
    for i in graph[start].keys():
        parents[i] = start

    while True:
        lowest_cost_node = find_lowest_cost(costs)
        if lowest_cost_node is None:
            break
        neighbors = graph[lowest_cost_node].keys()
        for n in neighbors:
            if costs[n] > costs[lowest_cost_node] + graph[lowest_cost_node][n]:
                costs[n] = costs[lowest_cost_node] + graph[lowest_cost_node][n]
                parents[n] = lowest_cost_node
        processed.append(lowest_cost_node)

    return parents, costs


graph = {
    "book": {"lp": 5, "poster": 0},
    "lp": {"drum": 20, "guitar": 15},
    "poster": {"guitar": 30, "drum": 35},
    "guitar": {"piano": 20},
    "drum": {"piano": 10},
    "piano": {},
}

parents, costs = dijkstra(graph, "book")
print(f"lowest cost to reach piano is {costs['piano']} with chart \n-> piano")
current_value = "piano"

while current_value != "book":
    current_value = parents[current_value]
    print("->", current_value)
