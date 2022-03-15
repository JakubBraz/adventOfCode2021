inp = """SNPVPFCPPKSBNSPSPSOF

CF -> N
NK -> B
SF -> B
HV -> P
FN -> S
VV -> F
FO -> F
VN -> V
PV -> P
FF -> P
ON -> S
PB -> S
PK -> P
OO -> P
SP -> F
VF -> H
OV -> C
BN -> P
OH -> H
NC -> F
BH -> N
CS -> C
BC -> N
OF -> N
SN -> B
FP -> F
FV -> K
HP -> H
VB -> P
FH -> F
HF -> P
BB -> O
HH -> S
PC -> O
PP -> B
VS -> B
HC -> H
NS -> N
KF -> S
BO -> V
NP -> S
NF -> K
BS -> O
KK -> O
VC -> V
KP -> K
CK -> P
HN -> F
KN -> H
KH -> N
SB -> S
NO -> K
HK -> H
BF -> V
SV -> B
CV -> P
CO -> P
FC -> O
CP -> H
CC -> N
CN -> P
SK -> V
SS -> V
VH -> B
OS -> N
FB -> H
NB -> N
SC -> K
NV -> H
HO -> S
SO -> P
PH -> C
VO -> O
OB -> O
FK -> S
PN -> P
VK -> O
NH -> N
OC -> B
BP -> O
PF -> F
KB -> K
KV -> B
PO -> N
NN -> K
CH -> O
KC -> P
OP -> V
VP -> F
OK -> P
FS -> K
CB -> S
HB -> N
KS -> O
BK -> C
BV -> O
SH -> H
PS -> N
HS -> K
KO -> N"""
# inp = """NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C"""

from functools import reduce
from collections import Counter

def parse_input(inp):
    r = inp.split('\n')
    template = r[0]
    r = r[2:]
    r = [x.split(' -> ') for x in r]
    return template, {x: x[0] + y for x,y in r}

def parse_new_pairs(inp):
    r = inp.split('\n')
    r = r[2:]
    r = [x.split(' -> ') for x in r]
    return {x: (x[0] + y, y + x[1]) for x,y in r}

def step(temp, pairs):
    size = 2
    result = reduce(lambda acc, val: acc + pairs[temp[val:val+size]], range(len(temp)-1), "") + temp[-1]
    return result

def count_pairs(pairs, template):
    size = 2
    r = {p: 0 for p in pairs}
    def f(acc, val):
        temp = dict(acc)
        ind = template[val:val+size]
        temp[ind] = temp[ind] + 1
        return temp
    r = reduce(f, range(len(template)-1), r)
    return r

def part1(template, pairs, N):
    r = reduce(lambda acc, val: step(acc, pairs), range(N), template)
    r = Counter(r)
    r = r.values()
    min_c, max_c = min(r), max(r)
    return max_c - min_c

def update_counter(counter, new_pairs, non_zero_pairs, res):
    if not non_zero_pairs:
        return res
    result = dict(res)
    e = non_zero_pairs[0]
    old_val = counter[e]
    result[e] = result[e] - old_val
    p1, p2 = new_pairs[e]
    result[p1] = result[p1] + old_val
    result[p2] = result[p2] + old_val
    return update_counter(counter, new_pairs, non_zero_pairs[1:], result)

def part2(template, new_pairs, count, N):
    def f(acc, _val):
        non_zero = [x for x in acc if acc[x]>0]
        return update_counter(acc, new_pairs, non_zero, acc)
    r = reduce(f, range(N), count)
    def f(acc, val):
        ind = val[0]
        res = dict(acc)
        res[ind] = acc.get(ind, 0) + r[val]
        return res
    occur = reduce(f, r, {})
    occur[template[-1]] = occur[template[-1]] + 1
    return max(occur.values()) - min(occur.values())

template, pairs = parse_input(inp)
count = count_pairs(pairs, template)
new_pairs = parse_new_pairs(inp)

print(part1(template, pairs, 10))
print(part2(template, new_pairs, count, 40))
