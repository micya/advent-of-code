def has_bingo(board):
    if board[0][0] and board[0][1] and board[0][2] and board[0][3] and board[0][4]:
        return True

    if board[1][0] and board[1][1] and board[1][2] and board[1][3] and board[1][4]:
        return True

    if board[2][0] and board[2][1] and board[2][2] and board[2][3] and board[2][4]:
        return True

    if board[3][0] and board[3][1] and board[3][2] and board[3][3] and board[3][4]:
        return True

    if board[4][0] and board[4][1] and board[4][2] and board[4][3] and board[4][4]:
        return True

    if board[0][0] and board[1][0] and board[2][0] and board[3][0] and board[4][0]:
        return True

    if board[0][1] and board[1][1] and board[2][1] and board[3][1] and board[4][1]:
        return True

    if board[0][2] and board[1][2] and board[2][2] and board[3][2] and board[4][2]:
        return True

    if board[0][3] and board[1][3] and board[2][3] and board[3][3] and board[4][3]:
        return True

    if board[0][4] and board[1][4] and board[2][4] and board[3][4] and board[4][4]:
        return True

    return False

file = open("tmp-input.txt")

calls = file.readline().split(",")
calls = [int(call) for call in calls]

# parse boards
boards = [[]]
numbers = {}

# throw away empty line
file.readline()

line_num = 0

for line in file:
    # empty line marks end of board
    if line_num == 5:
        boards.append([])
        line_num = 0
        continue

    nums = line.split()
    nums = [int(num) for num in nums]
    boards[len(boards) - 1].append(nums)

    for i in range(len(nums)):
        num = nums[i]

        if num in numbers:
            numbers[num].append((len(boards) - 1, line_num, i))
        else:
            numbers[num] = [(len(boards) - 1, line_num, i)]

    line_num += 1

# play bingo
marked = [[[False for _ in range(5)] for _ in range(5)] for _ in range(len(boards))]
bingo_board = -1
last_call = 0

for call in calls:
    if call not in numbers:
        continue

    # mark the numbers
    for board_num, line_num, column_num in numbers[call]:
        marked[board_num][line_num][column_num] = True

    # check for bingo
    for board_num in range(len(marked)):
        board = marked[board_num]

        if has_bingo(board):
            bingo_board = board_num
            last_call = call
            break

    # got bingo
    if bingo_board != -1:
        break

# calculate score
score = 0

for i in range(5):
    for j in range(5):
        if marked[bingo_board][i][j]:
            continue

        score += boards[bingo_board][i][j]

score *= last_call
print(score)