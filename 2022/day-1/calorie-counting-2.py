calories = 0
calories_list = []

for line in open("input.txt"):
    line = line.strip()

    if len(line) == 0:
        calories_list.append(calories)
        calories = 0
        continue

    calories += int(line)

calories_list.sort(reverse=True)

total_calories = calories_list[0] + calories_list[1] + calories_list[2]
print(total_calories)