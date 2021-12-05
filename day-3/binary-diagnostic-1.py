gamma = 0
epsilon = 0
numLength = 12

with open("input.txt") as file:
    lines = file.readlines()

for i in range(numLength):
    digits = [line[i] for line in lines]
    
    if digits.count("1") > len(digits) / 2:
        gamma += 2 ** (numLength - i - 1)
    else:
        epsilon += 2 ** (numLength - i - 1)

print(f"gamma: {gamma}, epsilon: {epsilon}")
print(gamma * epsilon)
