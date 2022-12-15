# https://adventofcode.com/2022/day/14
import sys

def print_grid_in_range(grid, x,y):
    p = ""
    for g_y,line in enumerate(grid):
        for g_x,item in enumerate(line):
            if g_x >= x and g_y <= y:
                p = p+item
        if p != "":
            print(p)
        p = ""

def build_rocks(grid, point1, point2):
    p1_x,p1_y = point1[0],point1[1]
    p2_x,p2_y = point2[0],point2[1]
    if p1_x == p2_x:
        for n in range(min(p1_y,p2_y), max(p1_y,p2_y)+1):
            grid[n][p1_x] = '#'
    else:
        for n in range(min(p1_x,p2_x), max(p1_x,p2_x)+1):
            grid[p1_y][n] = '#'

def build_floor(grid, floor):
    for x,point in enumerate(grid[floor]):
        grid[floor][x] = '#'

blockers = ['#','O']
# Returns True if it is still falling, false otherwise
def sand_fall(grid,x,y):
    if y == 199:
        return True
    if grid[y+1][x] in blockers and grid[y+1][x-1] in blockers and grid[y+1][x+1] in blockers:
        if x == 500 and y == 0: # edge case filling the source
            if grid[y][x] == 'O':
                return True
        grid[y][x] = 'O'
        return False
    else:
        if grid[y+1][x] not in blockers: # down
            return sand_fall(grid,x,y+1)
        elif grid[y+1][x-1] not in blockers: # down left
            return sand_fall(grid,x-1,y+1)
        elif grid[y+1][x+1] not in blockers: # down right
            return sand_fall(grid,x+1,y+1)

# abyss if it reaches max depth
if __name__ == "__main__":
    w,h = 700,200
    grid = [['.' for x in range(w)] for y in range(h)]
    source = 500
    floor = -1
    data = open(sys.argv[1]).read().splitlines()
    for line in data:
        points = line.split('->')
        prev_point = []
        current_point = []
        for i,point in enumerate(points):
            if i == 0:
                prev_point = [int(p) if p.isdigit() else p for p in point.strip().split(',')]
                continue
            else:
                current_point = [int(p) if p.isdigit() else p for p in point.strip().split(',')]
            floor = max(floor, max(prev_point[1],current_point[1]))
            build_rocks(grid,prev_point,current_point)
            prev_point = current_point         
    build_floor(grid,floor+2) # remove for part 1 answer
    counter = 0
    while(not sand_fall(grid,500,0)):
        counter = counter+1
    print(f"Number of Units of Sand until comes to rest: {counter}")