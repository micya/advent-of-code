max_calories = 0
calories = 0

for line in open("input.txt"):
    line = line.strip()

    if line == '':
        if calories > max_calories:
            max_calories = calories
        calories = 0
        continue

    calories += int(line)

print(max_calories)