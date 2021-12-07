import statistics

with open("input.txt") as file:
    locations = file.readline().split(",")

locations = [int(location) for location in locations]

# highly inefficient but it works
fuel = []

for i in range(max(locations)):
    usages = [abs(location - i) for location in locations]
    usages = [1/2 * usage * (usage + 1) for usage in usages]
    fuel.append(sum(usages))

print(min(fuel))