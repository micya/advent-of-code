x = 0
y = 0
aim = 0

for line in open("input.txt"):
    parts = line.split(" ")
    move = parts[0]
    distance = int(parts[1])

    if move == "forward":
        x += distance
        y += aim * distance
    elif move == "down":
        aim += distance
    elif move == "up":
        aim -= distance
    else:
        raise ValueError("invalid command")

print(f"x: {x}, y: {y}")
print(x * y)