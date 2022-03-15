inp = """inp w
mul x 0
add x z
mod x 26
div z 1
add x 11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -8
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 2
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -5
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 9
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -1
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 15
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -5
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -4
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 8
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -8
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y"""
inp2 = """inp z
inp x
mul z 3
eql z x"""
inp3 = """inp x
mul x -1"""
inp4 = """inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2"""

def parse_input(inp):
    i = inp.split('\n')
    return [x.split() for x in i]

def run_program(prog, inp_values):
    memory = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    instr_ind = 0
    inp_index = 0
    while instr_ind < len(prog):
        op, val1, *val2 = prog[instr_ind]
        val2 = (memory[val2[0]] if val2[0].isalpha() else int(val2[0])) if val2 else None
        if op == 'inp':
            i = inp_values[inp_index]
            memory[val1] = i
            inp_index += 1
        elif op == 'add':
            memory[val1] = memory[val1] + val2
        elif op == 'mul':
            memory[val1] = memory[val1] * val2
        elif op == 'div':
            memory[val1] = memory[val1] // val2
        elif op == 'mod':
            memory[val1] = memory[val1] % val2
        elif op == 'eql':
            memory[val1] = 1 if memory[val1] == val2 else 0
        instr_ind += 1
    return memory

def check_monad(program, val):
    memory = run_program(program, val)
    return memory['z'] == 0

# 'z' is always inreasing in steps OTHER than 4, 5, 7, 9, 11, 12, 13
# to reach 0 it must always decrease in steps 4, 5, 7, 9, 11, 12, 13
div_by_step =  [ 1,  1,  1,  1, 26, 26,  1,  26,  1, 26,  1, 26, 26, 26]
add_per_step = [11, 11, 14, 11, -8, -5, 11, -13, 12, -1, 14, -5, -4, -8]
add2_per_step = [1, 11,  1, 11,  2,  9,  7,  11,  6, 15,  7,  1,  8,  6]

input_instr = parse_input(inp)

def common_z(c0, c1):
    # z1 = ((c[0] + 1) * 26 + c[1] + 11
    return (c0 + add2_per_step[0]) * 26 + c1 + add2_per_step[1]

def z3(d0, d1, d2, d3):
    return (common_z(d0, d1) * 26 + d2 + add2_per_step[2]) * 26 + d3 + add2_per_step[3]

def z6(c0, c1, digit_6):
    return common_z(c0, c1) * 26 + digit_6 + add2_per_step[6]

def z8(c0, c1, digit_8):
    return common_z(c0, c1) * 26 + digit_8 + add2_per_step[8]

def z10(c0, c1, digit_10):
    return common_z(c0, c1) * 26 + digit_10 + add2_per_step[10]

def rng():
    return range(9, 0, -1)

def possible_d4(d0, d1, d2, d3):
    return [d4 for d4 in rng() if (z3(d0, d1, d2, d3)) % 26 + add_per_step[4] == d4]

def possible_d5(d0, d1, d2, d3):
    return [d5 for d5 in rng() if z3(d0, d1, d2, d3) // 26 % 26 + add_per_step[5] == d5]

def possible_d7(d0, d1, d6):
    return [d7 for d7 in rng() if (z6(d0, d1, d6)) % 26 + add_per_step[7] == d7]

def possible_d9(d0, d1, d8):
    return [d9 for d9 in rng() if (z8(d0, d1, d8)) % 26 + add_per_step[9] == d9]

def possible_d11(d0, d1, d10):
    return [d11 for d11 in rng() if (z10(d0, d1, d10)) % 26 + add_per_step[11] == d11]

def possible_d12(d0, d1, d10):
    return [d12 for d12 in rng() if z10(d0, d1, d10) // 26 % 26 + add_per_step[12] == d12]

def possible_d13(d0, d1, d10):
    return [d13 for d13 in rng() if z10(d0, d1, d10) // 26 // 26 % 26 + add_per_step[13] == d13]

result = [
    (d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13)
    for d0 in rng()
    for d1 in rng()
    for d2 in rng()
    for d3 in rng()
    for d4 in possible_d4(d0, d1, d2, d3)
    for d5 in possible_d5(d0, d1, d2, d3)
    for d6 in rng()
    for d7 in possible_d7(d0, d1, d6)
    for d8 in rng()
    for d9 in possible_d9(d0, d1, d8)
    for d10 in rng()
    for d11 in possible_d11(d0, d1, d10)
    for d12 in possible_d12(d0, d1, d10)
    for d13 in possible_d13(d0, d1, d10)
]
result = [''.join([str(d) for d in number]) for number in result]
print(result[0])
print(result[-1])
