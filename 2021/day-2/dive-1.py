x = 0
y = 0

for line in open("input.txt"):
    parts = line.split(" ")
    move = parts[0]
    distance = int(parts[1])

    if move == "forward":
        x += distance
    elif move == "down":
        y += distance
    elif move == "up":
        y -= distance
    else:
        raise ValueError("invalid command")

print(f"x: {x}, y: {y}")
print(x * y)