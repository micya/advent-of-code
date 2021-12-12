class Node:
    def __init__(self, id: str) -> None:
        self.id = id
        self.next = []

    def __str__(self) -> str:
        neighbors = ""
        for neighbor in self.next:
            neighbors += neighbor.id
        return f"Node {self.id}: {neighbors}"

# returns number of paths to end
def DFS(start: "Node", visited: "set[Node]", specialSmall: "Node" = None) -> int:
    if start.id == "end":
        return 1

    # add to visited if small cave
    if start.id.islower():
        if start in visited:
            specialSmall = start
        else:
            visited.add(start)

    paths = 0
    for neighbor in start.next:
        if neighbor not in visited or specialSmall is None and neighbor.id != "start":
            paths += DFS(neighbor, visited, specialSmall)

    # remove from visited
    # discard only removes if present
    if specialSmall == start:
        specialSmall = None
    else:
        visited.discard(start)

    return paths


def main() -> None:
    nodes = {}
    visited = set()

    with open("input.txt") as file:
        for line in file:
            parts = line.strip().split("-")
            start = parts[0]
            end = parts[1]

            if start not in nodes:
                nodes[start] = Node(start)

            if end not in nodes:
                nodes[end] = Node(end)

            nodes[start].next.append(nodes[end])
            nodes[end].next.append(nodes[start])

    print(DFS(nodes["start"], visited))


if __name__ == "__main__":
    main()
