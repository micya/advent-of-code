import statistics

with open("input.txt") as file:
    locations = file.readline().split(",")

locations = [int(location) for location in locations]

# find median
median = statistics.median(locations)

# find fuel usage
fuel = 0
for location in locations:
    fuel += abs(location - median)

print(fuel)