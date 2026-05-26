jug1 = 4
jug2 = 3
target = 2

visited = []

def dfs(a, b):

    if (a, b) in visited:
        return False

    visited.append((a, b))

    print(a, b)

    if a == target or b == target:
        print("Goal Reached")
        return True

    return (
        dfs(jug1, b) or
        dfs(a, jug2) or
        dfs(0, b) or
        dfs(a, 0) or
        dfs(a - min(a, jug2 - b), b + min(a, jug2 - b)) or
        dfs(a + min(b, jug1 - a), b - min(b, jug1 - a))
    )

dfs(0, 0)