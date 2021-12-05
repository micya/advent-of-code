oxygen = 0
co2 = 0
numLength = 12

with open("input.txt") as file:
    lines = file.readlines()

valid_oxygen = lines
valid_co2 = lines

for i in range(numLength):
    if len(valid_oxygen) == 1:
        break

    digits_oxygen = [line[i] for line in valid_oxygen]

    # more common
    if digits_oxygen.count("1") >= len(valid_oxygen) / 2:
        valid_oxygen = [line for line in valid_oxygen if line[i] == "1"]
    else:
        valid_oxygen = [line for line in valid_oxygen if line[i] == "0"]

for i in range(numLength):
    if len(valid_co2) == 1:
        break
    
    digits_co2 = [line[i] for line in valid_co2]

    # less common
    if digits_co2.count("0") <= len(valid_co2) / 2:
        valid_co2 = [line for line in valid_co2 if line[i] == "0"]
    else:
        valid_co2 = [line for line in valid_co2 if line[i] == "1"]

oxygen = int(valid_oxygen[0], 2)
co2 = int(valid_co2[0], 2)

print(f"oxygen: {oxygen}, co2: {co2}")
print(oxygen * co2)
