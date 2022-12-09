# https://adventofcode.com/2022/day/9
import sys
import math

steps = [[0,0],[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]
all_diagonals = [[-1,-1],[-1,1],[1,-1],[1,1]]
u_diagonal = [[1,-1],[-1,-1]]
d_diagonal = [[-1,1],[1,1]]
l_diagonal = [[-1,1],[-1,-1]]
r_diagonal = [[1,1],[1,-1]]
if __name__ == "__main__":
    data = open(sys.argv[1]).read().splitlines()
    w,h = 1000,1000
    visited_grid = [[False for x in range(w)] for y in range(h)]
    snake = [[500,500],[500,500],[500,500],[500,500],[500,500],[500,500],[500,500],[500,500],[500,500],[500,500]]
    for line in data:
        instructions = line.split(" ")
        direction,num = instructions[0],int(instructions[1])
        head = snake[0]
        tail = snake[9]
        visited_grid[tail[0]][tail[1]] = True
        move_to_make = [0,0]
        
        within_one_step = False
        for n in range(num):
        
            if direction == "U":
                head[1] = head[1]-1
                # fn to calc diagonal tail movement
                for i,node in enumerate(snake[1:]):
                    prev = snake[i]
                    node_within_one = False
                    for step in steps:
                        if node[0] + step[0] == prev[0] and node[1] + step[1] == prev[1]:
                            node_within_one = True
                    if not node_within_one:
                        if node[0] == prev[0]:
                            node[1] = node[1] - 1
                        else:
                            data_struct = [100,[]]
                            for move in steps:
                                proposed_move = [move[0]+node[0], move[1]+node[1]]
                                dist = math.dist(prev,proposed_move)
                                if dist < data_struct[0]:
                                    data_struct[0] = dist
                                    data_struct[1] = proposed_move
                            node[0] = data_struct[1][0]
                            node[1] = data_struct[1][1]
                                
            elif direction == "D":
                head[1] = head[1]+1
                for i,node in enumerate(snake[1:]):
                    prev = snake[i]
                    node_within_one = False
                    for step in steps:
                        if node[0] + step[0] == prev[0] and node[1] + step[1] == prev[1]:
                            node_within_one = True
                    if not node_within_one:
                        if node[0] == prev[0]:
                            node[1] = node[1] + 1
                        else:
                            data_struct = [100,[]]
                            for move in steps:
                                proposed_move = [move[0]+node[0], move[1]+node[1]]
                                dist = math.dist(prev,proposed_move)
                                if dist < data_struct[0]:
                                    data_struct[0] = dist
                                    data_struct[1] = proposed_move
                            node[0] = data_struct[1][0]
                            node[1] = data_struct[1][1]
            elif direction == "L":
                head[0] = head[0]-1
                for i,node in enumerate(snake[1:]):
                    prev = snake[i]
                    node_within_one = False
                    for step in steps:
                        if node[0] + step[0] == prev[0] and node[1] + step[1] == prev[1]:
                            node_within_one = True
                    if not node_within_one:
                        if node[1] == prev[1]:
                            node[0] = node[0] - 1
                        else:
                            data_struct = [100,[]]
                            for move in steps:
                                proposed_move = [move[0]+node[0], move[1]+node[1]]
                                dist = math.dist(prev,proposed_move)
                                if dist < data_struct[0]:
                                    data_struct[0] = dist
                                    data_struct[1] = proposed_move
                            node[0] = data_struct[1][0]
                            node[1] = data_struct[1][1]
            else:
                head[0] = head[0]+1
                for i,node in enumerate(snake[1:]):
                    prev = snake[i]
                    node_within_one = False
                    for step in steps:
                        if node[0] + step[0] == prev[0] and node[1] + step[1] == prev[1]:
                            node_within_one = True
                    if not node_within_one:
                        if node[1] == prev[1]:
                            node[0] = node[0] + 1
                        else:
                            data_struct = [100,[]]
                            for move in steps:
                                proposed_move = [move[0]+node[0], move[1]+node[1]]
                                dist = math.dist(prev,proposed_move)
                                if dist < data_struct[0]:
                                    data_struct[0] = dist
                                    data_struct[1] = proposed_move
                            node[0] = data_struct[1][0]
                            node[1] = data_struct[1][1]
            tail = snake[9]
            visited_grid[tail[0]][tail[1]] = True
        
            within_one_step = False
    count_visited = 0
    for line in visited_grid:
        for bool in line:
            if bool:
                count_visited = count_visited+1
    print(f"Part 2 Points Visited: {count_visited}")