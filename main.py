N = 10
M = 10
zeros = [[1] * N for _ in range(M)]
pos_map = []
amm_zeros = 0
for x in range(M):
    row = []
    for y in range(N):
        row.append([x, y])
        if (x + 1) % 3 == 0 or (y + 1) % 6 == 0:
            zeros[x][y] = 0
            amm_zeros += 1
        print("[" + str(x) + "][" + str(y) + "]", end=" ")
    pos_map.append(row)
    print("")

start = [2, 0]


def getAdjacent(arr, i, j):

    n = len(arr)
    m = len(arr[0])

    v = []

    for dx in range(-1 if (i > 0) else 0, 2 if (i < n) else 1):

        for dy in range(-1 if (j > 0) else 0, 2 if (j < m) else 1):
            if dx is not 0 or dy is not 0:
                v.append(arr[i + dx][j + dy])

    return v


graph = getAdjacent(pos_map, 1, 1)
node = [2, 0]

visited = []
queue = []

visited.append(node)
queue.append(node)

while queue:
    s = queue.pop(0)
    print(s, end=" ")

    for n in graph[s]:
        if n not in visited:
            visited.append(n)
            queue.append(n)
