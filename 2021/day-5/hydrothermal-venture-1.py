# assume each coordinate is between 0 and 1000
map = dict()

for line in open("input.txt"):
    coordinates = line.split(" -> ")
    
    coordinate1 = coordinates[0].split(",")
    x1 = int(coordinate1[0])
    y1 = int(coordinate1[1])

    coordinate2 = coordinates[1].split(",")
    x2 = int(coordinate2[0])
    y2 = int(coordinate2[1])

    if x1 == x2:
        y_min = min(y1, y2)
        y_max = max(y1, y2)

        for y in range(y_min, y_max + 1):
            if (x1, y) in map:
                map[(x1, y)] += 1
            else:
                map[(x1, y)] = 1
    elif y1 == y2:
        x_min = min(x1, x2)
        x_max = max(x1, x2)

        for x in range(x_min, x_max + 1):
            if (x, y1) in map:
                map[(x, y1)] += 1
            else:
                map[(x, y1)] = 1
    else:
        # ignore diagonal lines
        pass

count = 0
for location in map:
    if map[location] >= 2:
        count += 1

print(count)
