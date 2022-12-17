file = open("input.txt")

count = 0

for line in file:
    parts = line.split("|")
    outputs = parts[1].split()

    for output in outputs:
        # only digit 1 has 2 segments, only digit 7 has 3 segments, etc.
        if len(output) == 2 or len(output) == 3 or len(output) == 4 or len(output) == 7:
            print(output)
            count += 1

print(count)