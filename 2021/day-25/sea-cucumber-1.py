from copy import deepcopy
from enum import Enum


class Direction(Enum):
    NONE = 0
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4


def main():
    grid = []

    with open("input.txt", "r") as file:
        for line in file:
            grid.append([])
            for char in line.strip():
                # characters can only be south or east technically
                if char == ".":
                    direction = Direction.NONE
                elif char == "^":
                    direction = Direction.NORTH
                elif char == "v":
                    direction = Direction.SOUTH
                elif char == "<":
                    direction = Direction.WEST
                elif char == ">":
                    direction = Direction.EAST
                else:
                    raise ValueError("Invalid character")

                grid[-1].append(direction)

    x = len(grid)
    y = len(grid[0])
    step = 0
    changes = 0

    # not super efficient due to liberal use of deepcopy
    while True:
        changes = 0
        new_grid = deepcopy(grid)

        # everybody move east
        for i in range(x):
            for j in range(y):
                if grid[i][j] != Direction.EAST:
                    continue

                if grid[i][(j + 1 + y) % y] == Direction.NONE:
                    new_grid[i][j] = Direction.NONE
                    new_grid[i][(j + 1 + y) % y] = Direction.EAST
                    changes += 1

        # update tracking grid
        grid = new_grid
        new_grid = deepcopy(grid)

        # everybody move south
        for i in range(x):
            for j in range(y):
                if grid[i][j] != Direction.SOUTH:
                    continue

                if grid[(i + 1 + x) % x][j] == Direction.NONE:
                    new_grid[i][j] = Direction.NONE
                    new_grid[(i + 1 + x) % x][j] = Direction.SOUTH
                    changes += 1

        grid = new_grid

        step += 1

        if changes == 0:
            break

    print(step)


if __name__ == "__main__":
    main()
