# https://adventofcode.com/2022/day/12
import sys
import re

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
    print('\n')

def is_valid_move(grid,prev_elevation,x,y,w,h):
    if (x < 0 or x >= w or y < 0 or y >= h):
        return False
    if (prev_elevation+1 < ord(grid[y][x])): #  or (chr(prev_elevation) != 'z' and grid[y][x] == 'E')
        return False
    return True
    
def add_valid_moves(grid,elevation,x,y,w,h,locations_to_visit,step,visited):
    if is_valid_move(grid,elevation,x,y-1,w,h) and not visited[y-1][x]:
        if [x,y-1,step] not in locations_to_visit:
            locations_to_visit.append([x,y-1,step])
    if is_valid_move(grid,elevation,x,y+1,w,h) and not visited[y+1][x]:
        if [x,y+1,step] not in locations_to_visit:
            locations_to_visit.append([x,y+1,step])
    if is_valid_move(grid,elevation,x-1,y,w,h) and not visited[y][x-1]:
        if [x-1,y,step] not in locations_to_visit:
            locations_to_visit.append([x-1,y,step])
    if is_valid_move(grid,elevation,x+1,y,w,h) and not visited[y][x+1]:
        if [x+1,y,step] not in locations_to_visit:
            locations_to_visit.append([x+1,y,step])

if __name__ == "__main__":
    grid = open(sys.argv[1]).read().splitlines()
    w,h = len(grid[0]), len(grid)
    steps_to_point = [[10000 for x in range(w)] for y in range(h)]
    visited = [[False for x in range(w)] for y in range(h)]
    start_y,start_x = -1,-1
    end_y,end_x = -1,-1
    locations_to_visit = []
    all_possible_starting = [] # part 2
    for i,line in enumerate(grid):
        if 'S' in line:
            start_y = i
            start_x = line.find('S')
            steps_to_point[start_y][start_x] = 0
            visited[start_y][start_x] = True
            # add the valid moves
            add_valid_moves(grid,ord('a'),start_x,start_y,w,h,locations_to_visit,1,visited)
        if 'E' in line:
            end_y = i
            end_x = line.find('E')
        
        #part 2
        all_index_of_a = [m.start() for m in re.finditer('a',line)]
        for index in all_index_of_a:
            all_possible_starting.append([index,i])
    
    #bfs while loc to visits is not empty
    while(len(locations_to_visit) != 0):
        point = locations_to_visit.pop(0)
        steps_to_point[point[1]][point[0]] = point[2]
        visited[point[1]][point[0]] = True

        if point[0] == end_x and point[1] == end_y:
            break
        char = grid[point[1]][point[0]]
        elevation = ord(grid[point[1]][point[0]])
        add_valid_moves(grid, elevation,point[0],point[1],w,h,locations_to_visit,point[2]+1,visited)

    min_step_to_point = steps_to_point[end_y][end_x]

    visited = [[False for x in range(w)] for y in range(h)]
    steps_to_point = [[10000 for x in range(w)] for y in range(h)]
    locations_to_visit = []
    print(f"Part 1 starting from S: {min_step_to_point}")
    for starting_point in all_possible_starting:
        s_x,s_y = starting_point[0],starting_point[1]
        steps_to_point[s_y][s_x] = 0
        visited[s_y][s_x] = True
        add_valid_moves(grid,ord('a'),s_x,s_y,w,h,locations_to_visit,1,visited)
        while(len(locations_to_visit) != 0):
            point = locations_to_visit.pop(0)
            steps_to_point[point[1]][point[0]] = point[2]
            visited[point[1]][point[0]] = True

            if point[0] == end_x and point[1] == end_y:
                min_step_to_point = min(steps_to_point[end_y][end_x], min_step_to_point)
                break
            char = grid[point[1]][point[0]]
            elevation = ord(grid[point[1]][point[0]])
            add_valid_moves(grid, elevation,point[0],point[1],w,h,locations_to_visit,point[2]+1,visited)
        visited = [[False for x in range(w)] for y in range(h)]
        steps_to_point = [[10000 for x in range(w)] for y in range(h)]
        locations_to_visit = []
    print(f"Part 2 starting from any 'a': {min_step_to_point}")