# https://adventofcode.com/2022/day/5
import sys

# [B]                     [N]     [H]
# [V]         [P] [T]     [V]     [P]
# [W]     [C] [T] [S]     [H]     [N]
# [T]     [J] [Z] [M] [N] [F]     [L]
# [Q]     [W] [N] [J] [T] [Q] [R] [B]
# [N] [B] [Q] [R] [V] [F] [D] [F] [M]
# [H] [W] [S] [J] [P] [W] [L] [P] [S]
# [D] [D] [T] [F] [G] [B] [B] [H] [Z]
#  1   2   3   4   5   6   7   8   9 
stack1 = list("DHNQTWVB")
stack2 = list("DWB")
stack3 = list("TSQWJC")
stack4 = list("FJRNZTP")
stack5 = list("GPVJMST")
stack6 = list("BWFTN")
stack7 = list("BLDQFHVN")
stack8 = list("HPFR")
stack9 = list("ZSMBLNPH")
stacks = {1:stack1, 2:stack2, 3:stack3, 4:stack4, 5:stack5, 6:stack6, 7:stack7, 8:stack8, 9:stack9}
if __name__ == "__main__":
    data = open(sys.argv[1]).read().splitlines()
    for line in data:
        split = line.split('from')
        quantity = int(split[0].strip().split()[1])
        dir = split[1].strip().split('to')
        from_dir,to_dir = int(dir[0]),int(dir[1])
        from_crate,to_crate = stacks[from_dir], stacks[to_dir]
        crates_to_move = from_crate[len(from_crate)-quantity:]
        # crates_to_move.reverse() # uncomment for part 1
        from_crate = from_crate[0:len(from_crate)-quantity]
        stacks[from_dir] = from_crate
        to_crate.extend(crates_to_move)
        
ans = ""
for k in stacks:
    crate = stacks[k]
    ans = ans + crate[len(crate)-1]
print(f"Crate at top of each stack: {ans}")