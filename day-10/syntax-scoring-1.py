file = open("input.txt")

symbolScore = {")": 3, "]": 57, "}": 1197, ">": 25137}
score = 0

stack = []

for line in file:
    stack.clear()

    for c in line:
        if c not in symbolScore:
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
        score += symbolScore[c]
        break

print(score)
