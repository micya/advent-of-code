import heapq


def expand_grid(grid: "list[list[int]]") -> "list[list[int]]":
    expanded_grid = []

    max_x = len(grid)
    max_y = len(grid[0])

    for i in range(5):
        expanded_grid.extend([[] for _ in range(max_x)])
        for j in range(5):
            for x in range(max_x):
                for y in range(max_y):
                    # i + j is equal to increase
                    new_value = grid[x][y] + i + j
                    if new_value > 9:
                        new_value = new_value % 10 + 1
                    expanded_grid[i * max_x + x].append(new_value)

    return expanded_grid


def neighbors(x: int, y: int, grid: "list[list[int]]") -> "list[tuple]":
    neighbors = []

    if x > 0:
        neighbors.append((x - 1, y))
    if x < len(grid) - 1:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < len(grid[0]) - 1:
        neighbors.append((x, y + 1))

    return neighbors


def is_end(x: int, y: int, grid: "list[list[int]]") -> bool:
    return x == len(grid) - 1 and y == len(grid[0]) - 1


def dijkstra(grid: "list[list[int]]") -> int:
    frontier = []
    distances = {}
    heapq.heappush(frontier, (0, 0, 0))

    while len(frontier) != 0:
        distance, x, y = heapq.heappop(frontier)
        for neighbor_x, neighbor_y in neighbors(x, y, grid):
            new_distance = distance + grid[neighbor_x][neighbor_y]

            if is_end(neighbor_x, neighbor_y, grid):
                return new_distance

            if (neighbor_x, neighbor_y) not in distances or new_distance < distances[neighbor_x, neighbor_y]:
                distances[neighbor_x, neighbor_y] = new_distance
                heapq.heappush(
                    frontier, (new_distance, neighbor_x, neighbor_y))

    raise ValueError("no path found!")


def main():
    grid = []

    # read grid
    with open("input.txt") as file:
        for line in file:
            grid.append([])

            for c in line.strip():
                grid[-1].append(int(c))

    grid = expand_grid(grid)
    print(dijkstra(grid))


if __name__ == "__main__":
    main()
