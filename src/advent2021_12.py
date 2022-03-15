inp = """zs-WO
zs-QJ
WO-zt
zs-DP
WO-end
gv-zt
iu-SK
HW-zs
iu-WO
gv-WO
gv-start
gv-DP
start-WO
HW-zt
iu-HW
gv-HW
zs-SK
HW-end
zs-end
DP-by
DP-iu
zt-start"""
# inp = """start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end"""

def parse_input(inp):
    i = inp.split()
    i = [x.split('-') for x in i]
    return [(x, y) for x,y in i]

def make_map(pairs, res):
    if not pairs:
        return res
    k, v = pairs[0]
    temp = res.get(k, [])
    temp.append(v)
    res[k] = temp
    return make_map(pairs[1:], res)

def reverse_pairs(pairs):
    return [(y,x) for x,y in pairs]

def is_big(cave):
    return 'A' <= cave[0] <= 'Z'

def is_small(cave):
    return not is_big(cave)

def update_visited(current, visited):
    if is_big(current):
        return visited
    r = dict(visited)
    r[current] = r[current] + 1
    return r

def traverse(map, small_limit, current, visited):
    if current == 'end':
        return 1
    v = update_visited(current, visited)
    if v.get('start', 0) == 2:
        return 0
    if v.get(current, 0) == small_limit+1:
        return 0
    if len([x for x in v.values() if x>1]) > 1:
        return 0
    available = map.get(current, [])
    return sum([traverse(map, small_limit, x, v) for x in available])    

inp = parse_input(inp)
inp = make_map(inp + reverse_pairs(inp), {})
visited = {k: 0 for k in inp if is_small(k)}
print(traverse(inp, 1, 'start', visited))
print(traverse(inp, 2, 'start', visited))
