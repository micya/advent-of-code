# assume each coordinate is between 0 and 1000
vent_map = dict()

def step(x1, y1, x2, y2):
    if x1 == x2:
        x = x1
    elif x1 < x2:
        x = x1 + 1
    else:
        x = x1 - 1

    if y1 == y2:
        y = y1
    elif y1 < y2:
        y = y1 + 1
    else:
        y = y1 - 1

    return x, y

for line in open("input.txt"):
    coordinates = line.split(" -> ")
    
    coordinate1 = coordinates[0].split(",")
    x1 = int(coordinate1[0])
    y1 = int(coordinate1[1])

    coordinate2 = coordinates[1].split(",")
    x2 = int(coordinate2[0])
    y2 = int(coordinate2[1])

    while x1 != x2 or y1 != y2:
        if (x1, y1) in vent_map:
            vent_map[(x1, y1)] += 1
        else:
            vent_map[(x1, y1)] = 1
        
        x1, y1 = step(x1, y1, x2, y2)

    # for endpoint
    if (x2, y2) in vent_map:
        vent_map[(x2, y2)] += 1
    else:
        vent_map[(x2, y2)] = 1

count = 0
for location in vent_map:
    if vent_map[location] >= 2:
        count += 1

print(count)
