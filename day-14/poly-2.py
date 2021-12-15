import math

rules = {}
counts = {}

with open("input.txt") as file:
    # read starting
    initial = file.readline().strip()

    # skip next line
    file.readline()

    # read rules
    for line in file:
        parts = line.strip().split(" -> ")
        input = parts[0]
        output = parts[1]
        rules[input] = output

# populate counts for initial input
for i in range(len(initial) - 1):
    pair = initial[i : i + 2]

    if pair in counts:
        counts[pair] += 1
    else:
        counts[pair] = 1

for _ in range(40):
    # go through rules
    new_counts = {}

    for pair in counts:
        if pair not in rules:
            new_counts[pair] = counts[pair]

        # apply the rules
        new_pair_1 = pair[0] + rules[pair]
        new_pair_2 = rules[pair] + pair[1]

        if new_pair_1 in new_counts:
            new_counts[new_pair_1] += counts[pair]
        else:
            new_counts[new_pair_1] = counts[pair]

        if new_pair_2 in new_counts:
            new_counts[new_pair_2] += counts[pair]
        else:
            new_counts[new_pair_2] = counts[pair]

    counts = new_counts

# actually count letters
element_counts = {}
for pair in counts:
    first = pair[0]
    second = pair[1]

    if first in element_counts:
        element_counts[first] += counts[pair]
    else:
        element_counts[first] = counts[pair]

    if second in element_counts:
        element_counts[second] += counts[pair]
    else:
        element_counts[second] = counts[pair]

# adjustments - except for first and last letters, all others are double-counted
# we could divide by two and round up
for element in element_counts:
    element_counts[element] = math.ceil(element_counts[element] / 2)

print(element_counts)

# get maximum and minimum counts
max_count = element_counts[max(element_counts, key = element_counts.get)]
min_count = element_counts[min(element_counts, key = element_counts.get)]
print(max_count - min_count)