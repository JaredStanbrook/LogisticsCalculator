path_map = []
shelf_map = [
    [1, 1, 1, 1, 0, 4, 4, 4, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 0, 5, 5, 5, 5],
    [3, 3, 3, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 6, 6, 6, 6],
]
shelf = {
    1: {"amm": 20, "height": 10000, "bays": 4},
    2: {"amm": 60, "height": 10000, "bays": 2},
    3: {"amm": 90, "height": 10000, "bays": 3},
    4: {"amm": 10, "height": 10000, "bays": 5},
    5: {"amm": 30, "height": 10000, "bays": 1},
    6: {"amm": 10, "height": 10000, "bays": 10},
}

H = len(shelf_map)
W = len(shelf_map[0])

for x in range(H):
    for y in range(W):
        if shelf_map[x][y] == 0:
            path_map.append([x, y])


warehouse_d = (1000, 1000, 200)
standard_shelf_size = 500  # cm^2


def isValidPos(arr, x, y, z):
    if x < 0 or y < 0:
        return 0
    try:
        if z == 0:
            if arr[x][y] == 0:
                return 1
        else:
            if arr[x][y] != 0:
                return 1
    except IndexError:
        return 0


def checkAdjacent(arr, i, z):
    p = []
    if isValidPos(arr, i[0] - 1, i[1], z):
        p.append(str([i[0] - 1, i[1]]))
    if isValidPos(arr, i[0], i[1] - 1, z):
        p.append(str([i[0], i[1] - 1]))
    if isValidPos(arr, i[0] + 1, i[1], z):
        p.append(str([i[0] + 1, i[1]]))
    if isValidPos(arr, i[0], i[1] + 1, z):
        p.append(str([i[0], i[1] + 1]))
    return p


def getAdjacent(arr, mapp):
    res = {}
    for i in mapp:
        res[str(i)] = checkAdjacent(arr, i, 0)
    return res


graph = getAdjacent(shelf_map, path_map)
node = "[0, 4]"


def BFS(graph, node, shelf_map, shelf, product):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        # print(s, end=" ")
        t = list(map(int, s[1:-1].split(", ", 1)))
        for i in checkAdjacent(shelf_map, t, 1):
            temp = list(map(int, i[1:-1].split(", ", 1)))
            if product <= shelf[shelf_map[temp[0]][temp[1]]]["amm"]:
                shelf[shelf_map[temp[0]][temp[1]]]["amm"] -= product
                return shelf_map[temp[0]][temp[1]]
        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)


product = {
    "Bananna": {"amm": 20, "pop": 1, "pal_h": 1000},
    "Apple": {"amm": 60, "pop": 3, "pal_h": 1500},
    "Orange": {"amm": 80, "pop": 2, "pal_h": 500},
}
sorted_prod = dict(sorted(product.items(), key=lambda x: x[1]["pop"]))
location = []
for key, value in sorted_prod.items():
    shelf_id = BFS(graph, node, shelf_map, shelf, value["amm"])
    print(shelf[shelf_id]["height"] / value["pal_h"])
    location.append([key, shelf_id])


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.cost = value / weight


def main():
    print(location)


if __name__ == "__main__":
    main()
