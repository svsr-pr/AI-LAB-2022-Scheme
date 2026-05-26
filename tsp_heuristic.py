n = 4

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

visited = []

for i in range(n):
    visited.append(False)

city = 0

visited[city] = True

path = [city]

cost = 0

for i in range(n - 1):

    minimum = 999

    next_city = -1

    for j in range(n):

        if visited[j] == False and graph[city][j] < minimum:

            minimum = graph[city][j]

            next_city = j

    visited[next_city] = True

    path.append(next_city)

    cost = cost + minimum

    city = next_city

cost = cost + graph[city][0]

path.append(0)

print("Path :", path)

print("Minimum Cost :", cost)