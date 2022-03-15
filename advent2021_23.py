inp = """#############
#...........#
###A#C#B#B###
  #D#D#A#C#
  #########"""
inp2 = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""
inp3 = """#############
#...........#
###B#A#C#D###
  #A#B#C#D#
  #########"""

def parse_input(inp):
    inp = inp.split('\n')
    row0 = inp[3]
    row1 = inp[2]
    row0 = [c for c in row0 if c.isalpha()]
    row1 = [c for c in row1 if c.isalpha()]
    row0 = list(zip([0, 2, 4, 6], row0))
    row1 = list(zip([1, 3, 5, 7], row1))
    d = dict(row0 + row1)
    as_list = [d.get(i, 'X') for i in all_fields]
    return ''.join(as_list)

legal_moves = {
    0: {1},
    1: {10, 0},
    2: {3},
    3: {12, 2},
    4: {5},
    5: {14, 4},
    6: {7},
    7: {16, 6},
    8: {9},
    9: {8, 10},
    10: {9, 11, 1},
    11: {10, 12},
    12: {11, 13, 3},
    13: {12, 14},
    14: {13, 15, 5},
    15: {14, 16},
    16: {15, 17, 7},
    17: {16, 18},
    18: {17}
}

legal_moves2 = {
    0: {1},
    1: {0, 2},
    2: {1, 3},
    3: {2, 18},
    4: {5},
    5: {4, 6},
    6: {5, 7},
    7: {6, 20},
    8: {9},
    9: {8, 10},
    10: {9, 11},
    11: {10, 22},
    12: {13},
    13: {12, 14},
    14: {13, 15},
    15: {14, 24},
    16: {17},
    17: {16, 18},
    18: {17, 19, 3},
    19: {18, 20},
    20: {19, 21, 7},
    21: {20, 22},
    22: {21, 23, 11},
    23: {22, 24},
    24: {23, 25, 15},
    25: {24, 26},
    26: {25}
}

cant_stop = {10, 12, 14, 16}
cant_stop2 = {18, 20, 22, 24}
all_fields = set(range(19))
all_fields2 = set(range(27))
hallway = set(range(8, 19))
hallway2 = set(range(16, 27))
hallway_list = list(range(8, 19))
hallway_list2 = list(range(16, 27))
all_homes = set(range(8))
all_homes2 = set(range(16))
home = {
    'A': [0, 1],
    'B': [2, 3],
    'C': [4, 5],
    'D': [6, 7]
}
home2 = {
    'A': [0, 1, 2, 3],
    'B': [4, 5, 6, 7],
    'C': [8, 9, 10, 11],
    'D': [12, 13, 14, 15]
}

cost = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

def find_closest(field):
    closest = field + 9 if field + 9 in cant_stop else field + 10
    dist = 2 if closest - field == 10 else 1
    return closest, dist

def find_closest2(field):
    if field in home2['A']:
        return (18, max(home2['A']) + 1 - field)
    if field in home2['B']:
        return (20, max(home2['B']) + 1 - field)
    if field in home2['C']:
        return (22, max(home2['C']) + 1 - field)
    if field in home2['D']:
        return (24, max(home2['D']) + 1 - field)

def distance(field1, field2):
    if field1 in hallway and field2 in hallway:
        return abs(field1 - field2)
    if field1 in all_homes:
        closest, closest_distance = find_closest(field1)
        return distance(closest, field2) + closest_distance
    if field2 in all_homes:
        closest, closest_distance = find_closest(field2)
        return distance(field1, closest) + closest_distance

def distance2(field1, field2):
    if field1 in hallway2 and field2 in hallway2:
        return abs(field1 - field2)
    if field1 in all_homes2:
        closest, closest_distance = find_closest2(field1)
        return distance2(closest, field2) + closest_distance
    if field2 in all_homes2:
        closest, closest_distance = find_closest2(field2)
        return distance2(field1, closest) + closest_distance

def find_free_left(start_pos, state, available_chars = 'X'):
    ran = [i for i in range(hallway_list[0], start_pos) if i not in cant_stop]
    r = itertools.takewhile(lambda x: state[x] in available_chars, reversed(ran))
    return list(r)

def find_free_left2(start_pos, state, available_chars = 'X'):
    ran = [i for i in range(hallway_list2[0], start_pos) if i not in cant_stop2]
    r = itertools.takewhile(lambda x: state[x] in available_chars, reversed(ran))
    return list(r)

def find_free_right(start_pos, state, available_chars = 'X'):
    ran = [i for i in range(start_pos, hallway_list[-1] + 1) if i not in cant_stop]
    r = itertools.takewhile(lambda x: state[x] in available_chars, ran)
    return list(r)

def find_free_right2(start_pos, state, available_chars = 'X'):
    ran = [i for i in range(start_pos, hallway_list2[-1] + 1) if i not in cant_stop2]
    r = itertools.takewhile(lambda x: state[x] in available_chars, ran)
    return list(r)

def available_hall_moves(field, state):
    pos, letter = field
    homes = home[letter]
    if pos in homes and all(state[x]==letter for x in range(homes[0], pos)):
        return []
    ind = max(legal_moves[pos])
    if ind not in hallway and state[ind] != 'X':
        return []
    closest,_ = find_closest(pos)
    available = find_free_left(closest, state) + find_free_right(closest, state)
    return available

def available_hall_moves2(field, state):
    pos, letter = field
    homes = home2[letter]
    if pos in homes and all(state[x]==letter for x in range(homes[0], pos)):
        return []
    ind = max(legal_moves2[pos])
    if ind not in hallway2 and state[ind] != 'X':
        return []
    closest,_ = find_closest2(pos)
    available = find_free_left2(closest, state) + find_free_right2(closest, state)
    return available

def free_home_index(letter, state):
    indices = home[letter]
    r = list(itertools.takewhile(lambda i: state[i] == 'X' or state[i] == letter, indices))
    if not r:
        return []
    r = [i for i in r if state[i] == 'X']
    return [r[0]] if r else []

def free_home_index2(letter, state):
    indices = home2[letter]
    r = list(itertools.takewhile(lambda i: state[i] == 'X' or state[i] == letter, indices))
    if not r:
        return []
    r = [i for i in r if state[i] == 'X']
    return [r[0]] if r else []

def find_home_road(home_letter, state):
    home_indices = home[home_letter]
    closest, _ = find_closest(home_indices[0])
    home_road = find_free_left(closest, state, 'X' + home_letter) + find_free_right(closest, state, 'X' + home_letter)
    return [i for i in home_road if state[i] == home_letter]

def find_home_road2(home_letter, state):
    home_indices = home2[home_letter]
    closest, _ = find_closest2(home_indices[0])
    home_road = find_free_left2(closest, state, 'X' + home_letter) + find_free_right2(closest, state, 'X' + home_letter)
    return [i for i in home_road if state[i] == home_letter]

def any_available_home_moves(state):
    r = {letter: list(zip(find_home_road(letter, state), free_home_index(letter, state))) for letter in home.keys()}
    r = {k:v[0] for k,v in r.items() if v}
    return [((start_pos, letter), dest_pos) for letter, (start_pos, dest_pos) in r.items()]

def any_available_home_moves2(state):
    r = {letter: list(zip(find_home_road2(letter, state), free_home_index2(letter, state))) for letter in home2.keys()}
    r = {k:v[0] for k,v in r.items() if v}
    return [((start_pos, letter), dest_pos) for letter, (start_pos, dest_pos) in r.items()]

def every_move(state):
    home_moves = any_available_home_moves(state)
    if home_moves:
        return home_moves
    moves = {f: available_hall_moves(f, state) for f in enumerate(state) if f[1] != 'X' and f[0] < hallway_list[0]}
    moves = [(k, v) for k,v in moves.items() if v]
    result = reduce(lambda acc, val: acc + [(val[0], p) for p in val[1]], moves, [])
    return result

def every_move2(state):
    home_moves = any_available_home_moves2(state)
    if home_moves:
        return home_moves
    moves = {f: available_hall_moves2(f, state) for f in enumerate(state) if f[1] != 'X' and f[0] < hallway_list2[0]}
    moves = [(k, v) for k,v in moves.items() if v]
    result = reduce(lambda acc, val: acc + [(val[0], p) for p in val[1]], moves, [])
    return result

def state_per_move(move, old_state):
    (old_pos, letter), new_pos = move
    new_state = old_state[:old_pos] + 'X' + old_state[old_pos+1:]
    new_state = new_state[:new_pos] + letter + new_state[new_pos+1:]
    return new_state

def cost_per_move(move):
    (old_pos, letter), new_pos = move
    return distance(old_pos, new_pos) * cost[letter]

def cost_per_move2(move):
    (old_pos, letter), new_pos = move
    return distance2(old_pos, new_pos) * cost[letter]

def state_correct(state):
    return state == 'AABBCCDDXXXXXXXXXXX'

def state_correct2(state):
    return state == 'AAAABBBBCCCCDDDDXXXXXXXXXXX'

def solve(old_state, cost, best_memo, memo):
    if (old_state, cost) in memo:
        return memo[(old_state, cost)]
    if state_correct(old_state):
        return cost
    moves = every_move(old_state)
    moves.sort(key= lambda x: cost_per_move(x))
    if not moves:
        return 10_000_000
    new_states = [state_per_move(m, old_state) for m in moves]
    # print('new states', new_states)
    move_cost = [cost_per_move(m) for m in moves]
    zipped = [(ns, nc) for ns, nc in zip(new_states, move_cost) if nc + cost < best_memo[0]]
    if not zipped:
        return 10_000_000
    r = min([solve(s, c + cost, best_memo, memo) for s,c in zipped])
    if r < best_memo[0]:
        best_memo[0] = r
    memo[(old_state, cost)] = r
    return r

def solve2(old_state, cost, best_memo, memo):
    if (old_state, cost) in memo:
        return memo[(old_state, cost)]
    if state_correct2(old_state):
        return cost
    moves = every_move2(old_state)
    moves.sort(key= lambda x: cost_per_move2(x))
    if not moves:
        return 10_000_000
    new_states = [state_per_move(m, old_state) for m in moves]
    move_cost = [cost_per_move2(m) for m in moves]
    zipped = [(ns, nc) for ns, nc in zip(new_states, move_cost) if nc + cost < best_memo[0]]
    if not zipped:
        return 10_000_000
    r = min([solve2(s, c + cost, best_memo, memo) for s,c in zipped])
    if r < best_memo[0]:
        best_memo[0] = r
    memo[(old_state, cost)] = r
    return r

def parse_input2(inp, inserted_lines):
    inp = inp.split('\n')
    row0 = inp[3]
    row1 = inp[2]
    row0 = [c for c in row0 if c.isalpha()]
    row1 = [c for c in row1 if c.isalpha()]
    # row0 = list(zip([0, 2, 4, 6], row0))
    # row1 = list(zip([1, 3, 5, 7], row1))
    row2 = [c for c in inserted_lines[0] if c.isalpha()]
    row3 = [c for c in inserted_lines[1] if c.isalpha()]
    row0 = list(zip([0, 4, 8, 12], row0))
    row3 = list(zip([1, 5, 9, 13], row3))
    row2 = list(zip([2, 6, 10, 14], row2))
    row1 = list(zip([3, 7, 11, 15], row1))
    d = dict(row0 + row3 + row2 + row1)
    as_list = [d.get(i, 'X') for i in all_fields2]
    return ''.join(as_list)

import itertools
from functools import reduce

init_state = parse_input(inp)
print(solve(init_state, 0, [10_000_000], {}))

state2 = parse_input2(inp, ["#D#C#B#A#", "#D#B#A#C#"])
print(solve2(state2, 0, [10_000_000], {}))
