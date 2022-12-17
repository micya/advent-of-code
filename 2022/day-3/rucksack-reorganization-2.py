def get_priority(item_type: str) -> int:
    # capital letters
    if ord(item_type) < ord('a'):
        return ord(item_type) - ord('A') + 26 + 1

    # lowercase letters
    return ord(item_type) - ord('a') + 1


line_num = 0
total_priorities = 0
item_types = set()

for line in open("input.txt"):
    line = line.strip()
    
    if line_num % 3 == 0:
        item_types.clear()
        
        # dump everything in first rucksack in group into set
        for item_type in line:
            item_types.add(item_type)
    else:
        # find intersection
        item_types.intersection_update(line)

    if line_num % 3 == 2:
        # in theory, only one item should be left
        total_priorities += get_priority(item_types.pop())

    line_num += 1

print(total_priorities)
