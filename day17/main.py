# https://adventofcode.com/2022/day/17
import sys
rock1 = ['..####.']
rock2 = ['...#...','..###..','...#...']
rock3 = ['..###..','....#..','....#..']
rock4 = ['..#....','..#....','..#....','..#....']
rock5 = ['..##...','..##...']
def print_cave(cave):
    for line in reversed(cave):
        print(line)

def print_rock(r):
    for line in reversed(r.arr):
        print(line)

class Rock:
    def __init__(self,arr):
        self.arr = arr.copy()
    
    def move_left(self):
        for line in self.arr:
            if line[0] == '#':
                return
        for i,line in enumerate(self.arr):
            line = line[1:]
            line = line + '.'
            self.arr[i] = line
    
    def move_right(self):
        for line in self.arr:
            if line[6] == '#':
                return
        for i,line in enumerate(self.arr):
            line = line[:-1]
            line = '.'+ line
            self.arr[i] = line

def can_fall(r, cave, height):
    if (height > len(cave)):
        return True
    
    for i,line in enumerate(r.arr):
        if height+i > len(cave):
            return True
        cave_line = cave[height+i-1]
        for j in range(7):
            if line[j] == '#' and cave_line[j] == '#':
                # print("colliding at index: " + str(j) + " and height: " + str(height-i-1))
                # print_cave(cave)
                return False
    return True

def can_move_left(r, cave, height):
    left_most_coord = 6
    for line in r.arr:
        for i,ch in enumerate(line):
            if ch == '#':
                left_most_coord = min(i,left_most_coord)
    if left_most_coord == 0:
        return False
    
    rock_h = len(r.arr)
    for i in range(rock_h):
        if height+i > len(cave):
            return True
        rock_line = r.arr[i]
        left_most_coord = 7
        for j in range(7):
            if rock_line[j] == '#':
                left_most_coord = j
                break
        cave_line = cave[height+i-1]
        if cave_line[left_most_coord-1] == '#':
            return False
    return True

def can_move_right(r, cave, height):
    right_most_coord = 0
    for line in r.arr:
        for i,ch in enumerate(line):
            if ch == '#':
                right_most_coord = max(i,right_most_coord)
    if right_most_coord == 6:
        return False
    
    rock_h = len(r.arr)
    for i in range(rock_h):
        if height+i > len(cave):
            return True
        rock_line = r.arr[i]
        right_most_coord = 0
        for j in reversed(range(7)):
            if rock_line[j] == '#':
                right_most_coord = j
                break

        cave_line = cave[height+i-1]
        if cave_line[right_most_coord+1] == '#':
            return False
    return True

def p1():
    rock_pattern = [rock1,rock2,rock3,rock4,rock5]
    cave = []
    start_height = 4
    num_rocks = 2022
    jetstream_pos = 0
    for x in range(num_rocks):
        rock_no = x % 5
        r = Rock(rock_pattern[rock_no])
        height = start_height
        while height > 0 and can_fall(r,cave,height): #or fall to rest
            # print(height)
            # if(rock_no == 1):
            #     print("problem child")
            #     print_rock(r)
            if jetstream[jetstream_pos%len(jetstream)] == '<':
                # print("<")
                if can_move_left(r,cave,height):
                    r.move_left()
            else:
                # print(">")
                if can_move_right(r,cave,height):
                    r.move_right()
            jetstream_pos = jetstream_pos + 1
            height = height - 1
            
        cave_height = len(cave)
        for j,line in enumerate(r.arr):
            # print(height)
            if height+j < cave_height:
                cave_line = cave[height+j]
                # print(line)
                # print("cave line: ")
                # print(cave_line)
                joined_line = []
                for i in range(7):
                    if line[i] == '#' or cave_line[i] == '#':
                        joined_line.append('#')
                    else:
                        joined_line.append('.')
                # print(joined_line)
                cave[height+j] = ''.join(joined_line)
            else:
                cave.append(line)
        start_height = len(cave) + 4
        # print_cave(cave)
        # print('\n')

    # print_cave(cave)
    print(len(cave))

def p2():
    rock_pattern = [rock1,rock2,rock3,rock4,rock5]
    cave = []
    start_height = 4
    num_rocks = 4500
    running_cave_height = 0
    prev_rock_no = 0
    jetstream_pos = 0
    for x in range(num_rocks):
        if len(cave) > 10:
            for y in reversed(range(4)):
                c_line = cave[len(cave)-1-y]
                if c_line == "#######":
                    # cycle adds 2767 lines of height every 1745 rocks starting at rock 1459
                    # (1 TRILLION - 1458)%1745 = # of left over rocks that we need calculate
                    prev_delta_cave_height = running_cave_height 
                    running_cave_height = running_cave_height + len(cave)
                    cave = cave[len(cave)-1-y:] #15838-10000, 1585676 - 1mil
                    running_cave_height = running_cave_height - len(cave)
                    start_height = len(cave) + 4
                    prev_rock_no = x

        rock_no = x % 5
        r = Rock(rock_pattern[rock_no])
        height = start_height
        while height > 0 and can_fall(r,cave,height):
            if jetstream[jetstream_pos%len(jetstream)] == '<':
                if can_move_left(r,cave,height):
                    r.move_left()
            else:
                if can_move_right(r,cave,height):
                    r.move_right()
            jetstream_pos = jetstream_pos + 1
            height = height - 1   
        cave_height = len(cave)
        for j,line in enumerate(r.arr):
            if height+j < cave_height:
                cave_line = cave[height+j]
                joined_line = []
                for i in range(7):
                    if line[i] == '#' or cave_line[i] == '#':
                        joined_line.append('#')
                    else:
                        joined_line.append('.')
                cave[height+j] = ''.join(joined_line)
            else:
                cave.append(line)
        start_height = len(cave) + 4
    print(len(cave)+running_cave_height)    
if __name__ == "__main__":
    jetstream = open(sys.argv[1]).read().splitlines()[0]
    p1()
    p2()