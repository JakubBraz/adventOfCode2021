inp = """Player 1 starting position: 8
Player 2 starting position: 10"""
inp2 = """Player 1 starting position: 4
Player 2 starting position: 8"""

def parse_input(inp):
    inp = inp.split('\n')
    p1 = inp[0].replace("Player 1 starting position: ", '')
    p2 = inp[1].replace("Player 2 starting position: ", '')
    return int(p1), int(p2)

def dice_roll(i):
    return (i+1, i+2, i+3)

def calculate_new_poistion(old_position, move_by, limit):
    new_position = old_position + move_by
    new_position = new_position % limit
    if new_position == 0:
        return limit
    return new_position

def move(score, position, dice, dice_limit, board_limit):
    new_dice = (dice) % dice_limit + 1, (dice + 1) % dice_limit + 1, (dice + 2) % dice_limit + 1
    move_by = sum(new_dice)
    new_position = calculate_new_poistion(position, move_by, board_limit)
    new_score = score + new_position
    return new_score, new_position, new_dice[-1]

def step(score1, score2, pos1, pos2, dice, rolled, win_limit):
    s1, p1, dice = move(score1, pos1, dice, 100, 10)
    if s1 >= win_limit:
        return (1, score2, rolled + 3)
    s2, p2, dice = move(score2, pos2, dice, 100, 10)
    if s2 >= win_limit:
        return (2, score1, rolled + 6)
    return step(s1, s2, p1, p2, dice, rolled + 6, win_limit)

def reduce_universe(acc, val):
    w1, w2 = acc
    return (w1 + val[0], w2 + val[1])

def get_rolls():
    return [(r1, r2, r3) for r1 in range(1, 4) for r2 in range(1, 4) for r3 in range(1, 4)]

def step_universe(dice_rolls, score1, score2, pos1, pos2, limit, memo, i):
    dice_sum = sum(dice_rolls)
    if i == True:
        pos1 = calculate_new_poistion(pos1, dice_sum, 10)
        score1 = score1 + pos1
        if score1 >= limit:
            return (1, 0)
    if i == False:
        pos2 = calculate_new_poistion(pos2, dice_sum, 10)
        score2 = score2 + pos2
        if score2 >= limit:
            return (0, 1)
    ind = (dice_sum, score1, score2, pos1, pos2, i)
    if ind in memo:
        return memo[ind]
    possible_rolls = get_rolls()
    r = reduce(reduce_universe, [step_universe(roll, score1, score2, pos1, pos2, limit, memo, not i) for roll in possible_rolls], (0, 0))
    memo[ind] = r
    return r

def part1(pos1, pos2):
    winner, loser_score, dice_rolled = step(0, 0, pos1, pos2, 0, 0, 1000)
    return loser_score * dice_rolled

def part2(pos1, pos2):
    possible_rolls = get_rolls()
    w1, w2 = reduce(reduce_universe, [step_universe(roll, 0, 0, pos1, pos2, 10, {}, True) for roll in possible_rolls])
    return max(w1, w2)

from functools import reduce

pos1, pos2 = parse_input(inp2)
print(part1(pos1, pos2))
print(part2(pos1, pos2))
