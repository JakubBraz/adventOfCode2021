from functools import reduce
from collections import Counter

input = "3,4,3,1,2"
input = "1,1,5,2,1,1,5,5,3,1,1,1,1,1,1,3,4,5,2,1,2,1,1,1,1,1,1,1,1,3,1,1,5,4,5,1,5,3,1,3,2,1,1,1,1,2,4,1,5,1,1,1,4,4,1,1,1,1,1,1,3,4,5,1,1,2,1,1,5,1,1,4,1,4,4,2,4,4,2,2,1,2,3,1,1,2,5,3,1,1,1,4,1,2,2,1,4,1,1,2,5,1,3,2,5,2,5,1,1,1,5,3,1,3,1,5,3,3,4,1,1,4,4,1,3,3,2,5,5,1,1,1,1,3,1,5,2,1,3,5,1,4,3,1,3,1,1,3,1,1,1,1,1,1,5,1,1,5,5,2,1,5,1,4,1,1,5,1,1,1,5,5,5,1,4,5,1,3,1,2,5,1,1,1,5,1,1,4,1,1,2,3,1,3,4,1,2,1,4,3,1,2,4,1,5,1,1,1,1,1,3,4,1,1,5,1,1,3,1,1,2,1,3,1,2,1,1,3,3,4,5,3,5,1,1,1,1,1,1,1,1,1,5,4,1,5,1,3,1,1,2,5,1,1,4,1,1,4,4,3,1,2,1,2,4,4,4,1,2,1,3,2,4,4,1,1,1,1,4,1,1,1,1,1,4,1,5,4,1,5,4,1,1,2,5,5,1,1,1,5"

def parse_input(i):
    return [int(x) for x in i.split(',')]

def step(fishes):
    len_fish = len(fishes)
    new_fishes = [fishes[(i+1) % len_fish] for i in range(len_fish)]
    new_fishes[6] += fishes[0]
    return new_fishes

def simulation(fishes, days):
    return sum(reduce(lambda current_fish, _: step(current_fish), range(days), fishes))

def build_list(fishes):
    c = Counter(fishes)
    return [c[i] if c[i] else 0 for i in range(9)]

i = parse_input(input)
i = build_list(i)
print(simulation(i, 80))
print(simulation(i, 256))
