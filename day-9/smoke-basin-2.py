import queue


def get_neighbors(heightMap, x, y):
    neighbors = []

    if x > 0:
        neighbors.append((x - 1, y))

    if x < len(heightMap) - 1:
        neighbors.append((x + 1, y))

    if y > 0:
        neighbors.append((x, y - 1))

    if y < len(heightMap[0]) - 1:
        neighbors.append((x, y + 1))

    return neighbors


file = open("input.txt")

heightMap = []

for line in file:
    heights = list(line.strip())
    heights = [int(height) for height in heights]
    heightMap.append(heights)

# perform BFS until all locations are visited
frontier = queue.Queue()
visited = set()
basins = []

for x in range(len(heightMap)):
    for y in range(len(heightMap[0])):
        if heightMap[x][y] == 9 or (x, y) in visited:
            continue

        basinSize = 0
        frontier.put((x, y))

        # perform BFS
        while not frontier.empty():
            current_x, current_y = frontier.get()

            if (current_x, current_y) in visited:
                continue

            for neighbor_x, neighbor_y in get_neighbors(heightMap, current_x, current_y):
                if (neighbor_x, neighbor_y) not in visited and heightMap[neighbor_x][neighbor_y] != 9:
                    frontier.put((neighbor_x, neighbor_y))

            visited.add((current_x, current_y))
            basinSize += 1

        basins.append(basinSize)
        basinSize = 0

# get three largest basins and print product
basins.sort(reverse=True)
print(basins[0] * basins[1] * basins[2])
