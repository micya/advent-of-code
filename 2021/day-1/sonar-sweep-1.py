count = 0
previous = float('-inf')

for line in open("input.txt"):
    current = int(line)

    if current > previous:
        count += 1
    
    previous = current

# subtract to remove first element
count -= 1
print(count)