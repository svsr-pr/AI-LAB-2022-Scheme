graph = {
    'A': [['B', 'C'], ['D']],
    'B': [['E'], ['F']],
    'C': [['G']],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

heuristic = {
    'A': 10,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 0,
    'F': 0,
    'G': 0
}

def ao_star(node):

    print(node)

    if heuristic[node] == 0:
        return 0

    min_cost = 999

    for path in graph[node]:

        cost = 0

        for child in path:

            cost += heuristic[child]

        if cost < min_cost:
            min_cost = cost

    heuristic[node] = min_cost + 1

    return heuristic[node]

start = 'A'

result = ao_star(start)

print("Cost =", result)