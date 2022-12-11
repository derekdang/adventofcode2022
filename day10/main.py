# https://adventofcode.com/2022/day/10
import sys

noop = "noop"
add = "addx"
cycle_targets = [20,60,100,140,180,220]

def calc_signal_strength(cycle_no, register_val):
    return cycle_no * register_val

def draw_crt_row(crt_row, cycle, sprite_display):
    if (cycle-1) % 40 in sprite_display:
        crt_row = crt_row + "#"
    else:
        crt_row = crt_row + "."
    return crt_row

if __name__ == "__main__":
    data = open(sys.argv[1]).read().splitlines()
    signal_strength,register,cycle = 0,1,1
    crt_row = ""
    for line in data:
        sprite_display = [register-1,register,register+1]
        if line == noop:
            if cycle in cycle_targets:
                        signal_strength = signal_strength + calc_signal_strength(cycle, register)
            crt_row = draw_crt_row(crt_row,cycle,sprite_display)
            if cycle % 40 == 0:
                print(crt_row)
                crt_row = ""
            cycle = cycle + 1
        else:
            instruction = line.split(" ")
            if instruction[0] == add:
                for i in range(2):
                    if cycle in cycle_targets:
                        signal_strength = signal_strength + calc_signal_strength(cycle, register)
                    crt_row = draw_crt_row(crt_row,cycle,sprite_display)
                    if cycle % 40 == 0:
                        print(crt_row)
                        crt_row = ""
                    cycle = cycle + 1
                register = register + int(instruction[1])
    print(f"Part 1: {signal_strength}")