# https://adventofcode.com/2022/day/9
import sys

def explore(x,y,w,h,grid,is_visible):
    if y == 0 or x == 0 or y == h-1 or x == w-1:
        is_visible[y][x] = True
        return
    #look in all 4 cardinal directions, if there a tree taller than it then stop from that direction 
    tree_height = grid[y][x]
    north,south,west,east = y-1,y+1,x-1,x+1
    while north >= 0:
        if grid[north][x] >= tree_height:
            break
        elif north == 0:
            is_visible[y][x] = True
            break
        north = north - 1
    while south <= h:
        if grid[south][x] >= tree_height:
            break
        elif south == h-1:
            is_visible[y][x] = True
            break
        south = south + 1
    while west >= 0:
        if grid[y][west] >= tree_height:
            break
        elif west == 0:
            is_visible[y][x] = True
            break
        west = west - 1
    while east <= w:
        if grid[y][east] >= tree_height:
            break
        elif east == w-1:
            is_visible[y][x] = True
            break
        east = east + 1

    scenic_scores[y][x] = (y-north) * scenic_scores[y][x]
    scenic_scores[y][x] = (south-y) * scenic_scores[y][x]
    scenic_scores[y][x] = (x-west) * scenic_scores[y][x]
    scenic_scores[y][x] = (east-x) * scenic_scores[y][x]

if __name__ == "__main__":
    data = open(sys.argv[1]).read().splitlines()
    w = len(data[0])
    h = len(data)
    grid = [[0 for x in range(w)] for y in range(h)]
    is_visible = [[False for x in range(w)] for y in range(h)]
    scenic_scores = [[1 for x in range(w)] for y in range(h)]
    for idy,line in enumerate(data):
        for idx,char in enumerate(line):
            grid[idy][idx] = int(char)
    for idy,line in enumerate(grid):
        for idx,tree in enumerate(line):
            explore(idx,idy,w,h,grid,is_visible)
    
    visible_trees = 0
    for line in is_visible:
        for val in line:
            if val:
                visible_trees = visible_trees+1
    
    print(f"Part 1 Num of Visible Trees: {visible_trees}")

    max_scenic_score = 0
    for line in scenic_scores:
        for val in line:
            max_scenic_score = max(val, max_scenic_score)
    print(f"Part 2 Max Scenic Score: {max_scenic_score}")