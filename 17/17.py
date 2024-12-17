import sys, re
# lines = [i.strip() for i in open(sys.argv[1]).readlines()]
line = open(sys.argv[1]).read()

num_matches = [int(i) for i in re.findall(r"(\d+)",line)]

registers = num_matches[:3]

# part 1
program = num_matches[3:]
print(program)
output = []
instruction_pointer = 0

while 0 <= instruction_pointer < len(program):
    [ins, op] = program[instruction_pointer:(instruction_pointer+2)]
    combo_op = op if op <= 3 else registers[op - 4]
    match ins:
        case 0:
            registers[0] = registers[0] // (2**combo_op)
        case 1: 
            registers[1] ^= op
        case 2:
            registers[1] = (combo_op % 8)
        case 3:
            if registers[0]:
                instruction_pointer = op
                instruction_pointer -= 2 # accounting for 
        case 4:
            registers[1] ^= registers[2]
        case 5:
            output.append(combo_op % 8)
        case 6:
            registers[1] = registers[0] // (2**combo_op)
        case 7:
            registers[2] = registers[0] // (2**combo_op)
    instruction_pointer += 2
print(','.join([str(i) for i in output]))


# part 2
def evaluate_match(program, registers):
    instruction_pointer = 0
    output = []
    while 0 <= instruction_pointer < len(program):
        [ins, op] = program[instruction_pointer:(instruction_pointer+2)]
        combo_op = op if op <= 3 else registers[op - 4]
        match ins:
            case 0:
                registers[0] = registers[0] // (2**combo_op)
            case 1: 
                registers[1] ^= op
            case 2:
                registers[1] = (combo_op % 8)
            case 3:
                if registers[0]:
                    instruction_pointer = op
                    instruction_pointer -= 2 # accounting for 
            case 4:
                registers[1] ^= registers[2]
            case 5:
                output.append(combo_op % 8)
                # if output[:len(output)] != to_match[:len(output)]:
                #     return False
            case 6:
                registers[1] = registers[0] // (2**combo_op)
            case 7:
                registers[2] = registers[0] // (2**combo_op)
        instruction_pointer += 2
    return output#output == to_match

new_regs = num_matches[:3]
val = 8 ** len(num_matches[3:])
regs = new_regs.copy()
regs[0] = val


# build up from the end
num = 0
possible_nums_prev = {0}
b_c_regs = num_matches[1:3]
for n in range(len(program)):
    possible_nums = set()
    print(n, possible_nums_prev)
    for j in possible_nums_prev:
        for k in range(8*j, 8*j+8):
            output = evaluate_match(program, [k] + b_c_regs)
            if output == program[-(n+1):]:
                possible_nums.add(k)
    possible_nums_prev = possible_nums
print(min(possible_nums_prev))
# while num_matches[3:] != output:
#     regs = new_regs.copy()
#     regs[0] = val
#     output = evaluate_match(program, regs)
#     # print(output)
#     if not (val % 100000): print(val)
#     val += 1
# print(val - 1)
