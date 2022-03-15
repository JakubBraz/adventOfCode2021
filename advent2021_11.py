inp = """4585612331
5863566433
6714418611
1746467322
6161775644
6581631662
1247161817
8312615113
6751466142
1161847732"""
# inp = """5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526"""

from functools import reduce

def parse_input(inp):
    i = inp.split()
    return {(x,y): int(i[x][y]) for x in range(len(i)) for y in range(len(i[x]))}

def get_neighbours(oct):
    x,y = oct
    xy = [(x-1, y), (x+1, y), (x,y-1), (x, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]
    xy = [(x,y) for x,y in xy if 0 <= x < N and 0 <= y < N]
    return xy

def step(board):
    new_board = {(x,y): board[(x,y)]+1 for x in range(N) for y in range(N)}
    new_board, flash_count = do_flash(new_board, [(x,y) for x in range(N) for y in range(N)], set())
    all_light = all([board[(x,y)] == 0 for x in range(N) for y in range(N)])
    return make_zero(new_board), flash_count, all_light

def do_flash(board, to_visit, flashed):
    if not to_visit:
        return board, 0
    if to_visit[0] in flashed:
        return do_flash(board, to_visit[1:], flashed)
    if board[to_visit[0]] < 10:
        return do_flash(board, to_visit[1:], flashed)
    new_board = dict(board)
    neighs = get_neighbours(to_visit[0])
    updated = {k: v+1 for k,v in new_board.items() if (k[0], k[1]) in neighs}
    new_board.update(updated)
    new_board, count_flash = do_flash(new_board, to_visit[1:] + neighs, flashed | {to_visit[0]})
    return new_board, count_flash + 1

def make_zero(board):
    return {k: 0 if v>9 else v for k,v in board.items()}

def solve1(inp, steps):
    def f(acc, _val):
        b, cnt = acc
        new_b, new_cnt, _synchro = step(b)
        return (new_b, cnt+new_cnt)
    _b, cnt = reduce(f, range(steps), (inp, 0))
    return cnt

def solve2(board, cnt, synchro):
    if synchro:
        return cnt-1
    board, _, light = step(board)
    return solve2(board, cnt + 1, light)

N = len(inp.split())
inp = parse_input(inp)
print(solve1(inp, 100))
import sys
sys.setrecursionlimit(10000)
print(solve2(inp, 0, False))
