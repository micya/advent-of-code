lose_score = 0
draw_score = 3
win_score = 6


def get_move_score(your_move: str) -> int:
    if your_move == 'X':
        return 1
    if your_move == 'Y':
        return 2
    if your_move == 'Z':
        return 3

    raise ValueError("invalid move")


def get_winning_score(opponent_move: str, your_move: str) -> str:
    if opponent_move == 'A':
        if your_move == 'X':
            return draw_score
        if your_move == 'Y':
            return win_score
        if your_move == 'Z':
            return lose_score

    if opponent_move == 'B':
        if your_move == 'X':
            return lose_score
        if your_move == 'Y':
            return draw_score
        if your_move == 'Z':
            return win_score

    if opponent_move == 'C':
        if your_move == 'X':
            return win_score
        if your_move == 'Y':
            return lose_score
        if your_move == 'Z':
            return draw_score

    raise ValueError("invalid move")

def get_move(opponent_move: str, outcome: str):
    if opponent_move == 'A':
        if outcome == 'X':
            return 'Z'
        if outcome == 'Y':
            return 'X'
        if outcome == 'Z':
            return 'Y'
    
    if opponent_move == 'B':
        if outcome == 'X':
            return 'X'
        if outcome == 'Y':
            return 'Y'
        if outcome == 'Z':
            return 'Z'

    if opponent_move == 'C':
        if outcome == 'X':
            return 'Y'
        if outcome == 'Y':
            return 'Z'
        if outcome == 'Z':
            return 'X'

    raise ValueError("invalid move")

def get_score(opponent_move: str, your_move: str) -> int:
    return get_move_score(your_move) + get_winning_score(opponent_move, your_move)


score = 0

for line in open("input.txt"):
    parts = line.split()
    opponent_move = parts[0]
    outcome = parts[1]
    your_move = get_move(opponent_move, outcome)
    score += get_score(opponent_move, your_move)

print(score)
