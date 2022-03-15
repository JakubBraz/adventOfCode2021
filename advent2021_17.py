import re

inp = "target area: x=175..227, y=-134..-79"
# inp = "target area: x=20..30, y=-10..-5"

def parse_input(inp):
    res = tuple(re.findall("\d+|-\d+", inp))
    return [int(x) for x in res]

def in_area(area, x, y):
    ax1, ax2, ay1, ay2 = area
    return ax1 <= x <= ax2 and ay1 <= y <= ay2

def find_max_h(init_v):
    return int((1 + init_v) / 2 * init_v)

def reach_point(max_h, points):
    i = 0
    while True:
        if any([max_h == p for p in points]): return True
        if all(max_h < p for p in points): return False
        i += 1
        max_h -= i

def find_v(v, points):
    while True:
        if v < 0:
            return None
        max_h = find_max_h(v)
        if reach_point(max_h, points):
            return max_h
        v -= 1

def step_loop(area, x, y, vel_x, vel_y, prev_x, prev_y):
    while True:
        is_in = in_area(area, x, y)
        if is_in:
            return True
        if (prev_x < area[0] and x>area[1]) or (vel_y < 0 and prev_y>area[3] and y<area[2]) or (vel_y > 0 and prev_y<area[2] and y>area[3]):
            return False
        x, y = x + vel_x, y + vel_y
        vel_x, vel_y = vel_x - 1 if vel_x > 0 else 0, vel_y - 1

def part1(area):
    _, _, y1, y2 = area
    start_v = 1000
    return find_v(start_v, range(y1, y2+1))

def part2(area, max_h):
    size = 350
    res = [vel for vel in ((vx, vy) for vx in range(-size, size) for vy in range(-size, size)) if find_max_h(vel[1]) <= max_h and step_loop(area, 0, 0, vel[0], vel[1], 0, 0)]
    return len(res)

area = parse_input(inp)
h = part1(area)
print(h)
print(part2(area, h))
