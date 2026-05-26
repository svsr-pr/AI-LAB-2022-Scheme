from queue import PriorityQueue

goal = (0, 0, 0)

visited = []

pq = PriorityQueue()

start = (3, 3, 1)

pq.put((6, start))

def valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if (m > 0 and c > m):
        return False
    if ((3 - m) > 0 and (3 - c) > (3 - m)):
        return False
    return True

while not pq.empty():

    h, state = pq.get()

    m, c, b = state

    if state in visited:
        continue

    visited.append(state)

    print(state)

    if state == goal:
        print("Goal Reached")
        break

    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

    for dm, dc in moves:

        if b == 1:
            new = (m - dm, c - dc, 0)
        else:
            new = (m + dm, c + dc, 1)

        nm, nc, nb = new

        if valid(nm, nc):
            cost = nm + nc
            pq.put((cost, new))