count = 0
last = 3

with open("input.txt") as file:
    lines = file.readlines()
    lines = [int(line) for line in lines]

while last < len(lines):
    if lines[last] > lines[last - 3]:
        count += 1

    last += 1

print(count)