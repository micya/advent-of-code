file = open("input.txt")

symbolScore = {"(": 1, "[": 2, "{": 3, "<": 4}
scores = []

stack = []
corrupted = False

for line in file:
    stack.clear()
    corrupted = False

    for c in line.strip():
        if c in symbolScore:
            stack.append(c)
            continue

        if c == ")" and stack[len(stack) - 1] == "(":
            stack.pop()
            continue

        if c == "]" and stack[len(stack) - 1] == "[":
            stack.pop()
            continue

        if c == "}" and stack[len(stack) - 1] == "{":
            stack.pop()
            continue

        if c == ">" and stack[len(stack) - 1] == "<":
            stack.pop()
            continue

        # have a corrupted line if we reached here
        corrupted = True
        break

    # don't bother correcting corrupted lines
    if corrupted:
        continue

    score = 0
    while len(stack) != 0:
        c = stack.pop()
        score *= 5
        score += symbolScore[c]

    scores.append(score)

scores.sort()
print(scores[int(len(scores) / 2)])
