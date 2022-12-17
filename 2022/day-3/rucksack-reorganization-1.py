def get_priority(item_type: str) -> int:
    # capital letters
    if ord(item_type) < ord('a'):
        return ord(item_type) - ord('A') + 26 + 1

    # lowercase letters
    return ord(item_type) - ord('a') + 1


total_priorities = 0

for line in open("input.txt"):
    item_types = set()
    line = line.strip()
    mid = int(len(line) / 2)

    for i in range(mid):
        item_types.add(line[i])

    for i in range(mid, len(line)):
        if line[i] in item_types:
            item_type = line[i]

    total_priorities += get_priority(item_type)

print(total_priorities)
