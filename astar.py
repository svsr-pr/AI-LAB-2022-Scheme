from queue import PriorityQueue

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 1,
    'F': 0
}

start = 'A'
goal = 'F'

pq = PriorityQueue()

pq.put((0, start))

visited = []

cost = {start: 0}

while not pq.empty():

    f, node = pq.get()

    if node in visited:
        continue

    visited.append(node)

    print(node)

    if node == goal:
        print("Goal Reached")
        break

    for neighbor, weight in graph[node]:

        g = cost[node] + weight

        h = heuristic[neighbor]

        f = g + h

        if neighbor not in cost or g < cost[neighbor]:

            cost[neighbor] = g

            pq.put((f, neighbor))