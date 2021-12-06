counts = dict()
days = 256

with open("input.txt") as file:
    ages = file.readline().split(",")

for i in range(9):
    counts[i] = 0

for age in ages:
    counts[int(age)] += 1

for _ in range(days):
    new_fish = counts[0]

    for i in range(8):
        counts[i] = counts[i + 1]
    
    counts[6] += new_fish
    counts[8] = new_fish

total = 0
for age in counts:
    total += counts[age]

print(total)