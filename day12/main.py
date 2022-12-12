# https://adventofcode.com/2022/day/12
import sys

def traverse(grid, steps_to_point, step_no, prev_elev, x, y, w,h):
    if (x < 0 or x >= w or y < 0 or y >= h or step_no > steps_to_point[y][x]):
        return
    elev = ord(grid[y][x])
    if elev > prev_elev+1 or elev == 69:
        return

    steps_to_point[y][x] = min(step_no,steps_to_point[y][x])
    traverse(grid,steps_to_point,step_no+1,elev,x-1,y,w,h)
    traverse(grid,steps_to_point,step_no+1,elev,x+1,y,w,h)
    traverse(grid,steps_to_point,step_no+1,elev,x,y-1,w,h)
    traverse(grid,steps_to_point,step_no+1,elev,x,y+1,w,h)

def print_2d_array(arr):
    for l in arr:
        print(l)

def is_valid_move(grid,new_elev,x,y,w,h):
    if (x < 0 or x >= w or y < 0 or y >= h):
        return False
    if grid[y][x] != 'S':
        if new_elev > ord(grid[y][x])+1:
            return False
    return True

def calc_min_step(grid,steps_to_point,x,y,w,h):
    if (x < 0 or x >= w or y < 0 or y >= h):
        return 
    elev = ord(grid[y][x])
    
    up,down,left,right = 10000,10000,10000,10000
    if is_valid_move(grid,elev,x,y-1,w,h):
        up = steps_to_point[y-1][x]
    if is_valid_move(grid,elev,x,y+1,w,h):
        down = steps_to_point[y+1][x]
    if is_valid_move(grid,elev,x-1,y,w,h):
        left = steps_to_point[y][x-1]
    if is_valid_move(grid,elev,x+1,y,w,h):
        right = steps_to_point[y][x+1]
    
    min_move = min(up,down,left,right)
    if min_move != 10000:
        steps_to_point[y][x] = min(up,down,left,right)+1

if __name__ == "__main__":
    grid = open(sys.argv[1]).read().splitlines()
    w,h = len(grid[0]), len(grid)
    steps_to_point = [[10000 for x in range(w)] for y in range(h)]
    start_y,start_x = -1,-1
    end_y,end_x = -1,-1
    for i,line in enumerate(grid):
        if 'S' in line:
            start_y = i
            start_x = line.find('S')
            steps_to_point[start_y][start_x] = 0
            elev = ord('a')
            # traverse(grid,steps_to_point,1,elev,start_x-1,start_y,w,h)
            # traverse(grid,steps_to_point,1,elev,start_x+1,start_y,w,h)
            # traverse(grid,steps_to_point,1,elev,start_x,start_y-1,w,h)
            # traverse(grid,steps_to_point,1,elev,start_x,start_y+1,w,h)
        if 'E' in line:
            end_y = i
            end_x = line.find('E')

    # while(steps_to_point[end_y][end_x] == 10000):
    #     for y,line in enumerate(grid):
    #         for x,r in enumerate(line):
    #             calc_min_step(grid,steps_to_point,x,y,w,h) 
    print_2d_array(steps_to_point)