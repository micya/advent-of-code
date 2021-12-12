class Octopus:
    flashes = 0
    threshold = 10

    def __init__(self, energy: int, x: int = None, y: int = None) -> None:
        self.energy = energy
        self.neighbors = []
        self.x = x
        self.y = y
        self.lastCharge = None

    def addNeighbor(self, neighbor: "Octopus") -> None:
        self.neighbors.append(neighbor)
        neighbor.neighbors.append(self)

    def charge(self, step: int) -> None:
        # don't charge if just flashed
        if self.lastCharge == step:
            return

        self.energy += 1

        if self.energy < Octopus.threshold:
            return

        # flash
        self.energy = 0
        self.lastCharge = step
        Octopus.flashes += 1

        # charge neighbors
        for neighbor in self.neighbors:
            neighbor.charge(step)


class Grid:
    def __init__(self) -> None:
        self.octopi = []
        self.x = -1
        self.y = 0
        self.step = 0

    def addRow(self) -> None:
        self.octopi.append([])
        self.x += 1
        self.y = 0

    def addOctopus(self, octopus: "Octopus") -> None:
        # add octopus to last row
        octopus.x = self.x
        octopus.y = self.y
        self.octopi[self.x].append(octopus)

        self.y += 1

        # add neighbors if they exist - only will exist if above or to the left
        if octopus.x > 0:
            octopus.addNeighbor(self.octopi[octopus.x - 1][octopus.y])

        if octopus.y > 0:
            octopus.addNeighbor(self.octopi[octopus.x][octopus.y - 1])

        if octopus.x > 0 and octopus.y > 0:
            octopus.addNeighbor(self.octopi[octopus.x - 1][octopus.y - 1])

        if octopus.x > 0 and octopus.y < len(self.octopi[0]) - 1:
            octopus.addNeighbor(self.octopi[octopus.x - 1][octopus.y + 1])

    def charge(self) -> None:
        self.step += 1

        for row in self.octopi:
            for octopus in row:
                octopus.charge(self.step)

    def getFlashes(self) -> int:
        return Octopus.flashes

    def __str__(self) -> str:
        output = ""

        for row in self.octopi:
            for octopus in row:
                output += str(octopus.energy)
            output += "\n"

        return output


def main():
    grid = Grid()
    with open("input.txt") as file:
        for line in file:
            grid.addRow()

            for c in line.strip():
                grid.addOctopus(Octopus(int(c)))

    for _ in range(100):
        grid.charge()

    print(grid.getFlashes())


if __name__ == "__main__":
    main()
