class Paper:
    def __init__(self, x: int = 1500, y: int = 1500) -> None:
        self.x = x
        self.y = y
        self.grid = [[False for _ in range(x)] for _ in range(y)]

    def num_visible(self) -> int:
        count = 0

        for i in range(self.x):
            for j in range(self.y):
                if self.grid[i][j]:
                    count += 1

        return count

    def fold_horizontally(self, y: int) -> None:
        for i in range(self.x):
            for j in range(y, self.y):
                if self.grid[i][j]:
                    self.grid[i][2 * y - j] = True
                    self.grid[i][j] = False

        self.y = y

    def fold_vertically(self, x: int) -> None:
        for i in range(x, self.x):
            for j in range(self.y):
                if self.grid[i][j]:
                    self.grid[2 * x - i][j] = True
                    self.grid[i][j] = False

        self.x = x

    def add_dot(self, x: int, y: int) -> None:
        self.grid[x][y] = True

    def __str__(self) -> str:
        output = ""

        for i in range(self.x):
            for j in range(self.y):
                output += "#" if self.grid[i][j] else "."
            output += "\n"

        return output


def main():
    paper = Paper()

    with open("input.txt") as file:
        for line in file:
            # keep going until fold instruction
            if not line.strip():
                break

            # mark the dots
            parts = line.split(",")
            x = int(parts[0])
            y = int(parts[1])
            paper.add_dot(x, y)

        # execute folds
        for line in file:
            line = line.split(" ")[-1]
            parts = line.split("=")

            direction = parts[0]
            crease = int(parts[1])

            if direction == "x":
                paper.fold_vertically(crease)
            elif direction == "y":
                paper.fold_horizontally(crease)
            else:
                raise ValueError("invalid fold")

    print(paper)


if __name__ == "__main__":
    main()
