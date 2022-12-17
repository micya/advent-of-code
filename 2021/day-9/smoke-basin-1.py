# inefficient but it works
def is_lowest(heightMap, x, y):
    if x > 0 and heightMap[x][y] >= heightMap[x - 1][y]:
        return False

    if x < len(heightMap) - 1 and heightMap[x][y] >= heightMap[x + 1][y]:
        return False

    if y > 0 and heightMap[x][y] >= heightMap[x][y - 1]:
        return False

    if y < len(heightMap[0]) - 1 and heightMap[x][y] >= heightMap[x][y + 1]:
        return False

    return True

file = open("input.txt")

heightMap = []

for line in file:
    heights = list(line.strip())
    heights = [int(height) for height in heights]
    heightMap.append(heights)

lowestSum = 0

for x in range(len(heightMap)):
    for y in range(len(heightMap[0])):
        if is_lowest(heightMap, x, y):
            lowestSum += heightMap[x][y] + 1

print(lowestSum)
