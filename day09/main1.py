# https://adventofcode.com/2022/day/9
import sys

steps = [[0,0],[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]
u_diagonal = [[1,-1],[-1,-1]]
d_diagonal = [[-1,1],[1,1]]
l_diagonal = [[-1,1],[-1,-1]]
r_diagonal = [[1,1],[1,-1]]
if __name__ == "__main__":
    data = open(sys.argv[1]).read().splitlines()
    w,h = 1000,1000
    visited_grid = [[False for x in range(w)] for y in range(h)]
    head,tail = [499,499],[499,499]

    for line in data:
        instructions = line.split(" ")
        direction,num = instructions[0],int(instructions[1])

        visited_grid[tail[0]][tail[1]] = True
        within_one_step = False
        for i in range(num):              
            if direction == "U":
                head[1] = head[1]-1
                # fn to calc diagonal tail movement
                for step in steps:
                    if tail[0] + step[0] == head[0] and tail[1] + step[1] == head[1]:
                        within_one_step = True          
                if not within_one_step:
                    # move in same column / row or move in diagonal
                    if tail[0] == head[0]: # it is in the same x, so just move up
                        tail[1] = tail[1]-1
                    else:
                        for move in u_diagonal:
                            if move[0] + tail[0] == head[0]: # moves it into the same X coord so make this move
                                tail[0] = tail[0] + move[0]
                                tail[1] = tail[1] + move[1]
            elif direction == "D":
                head[1] = head[1]+1
                for step in steps:
                    if tail[0] + step[0] == head[0] and tail[1] + step[1] == head[1]:
                        within_one_step = True   
                if not within_one_step:
                    # move in same column / row or move in diagonal
                    if tail[0] == head[0]: # it is in the same x, so just move down
                        tail[1] = tail[1]+1
                    else:
                        for move in d_diagonal:
                            if move[0] + tail[0] == head[0]: # moves it into the same X coord so make this move
                                tail[0] = tail[0] + move[0]
                                tail[1] = tail[1] + move[1]
            elif direction == "L":
                head[0] = head[0]-1
                for step in steps:
                    if tail[0] + step[0] == head[0] and tail[1] + step[1] == head[1]:
                        within_one_step = True   
                if not within_one_step:
                    # move in same column / row or move in diagonal
                    if tail[1] == head[1]: # it is in the same y, so just move left
                        tail[0] = tail[0]-1
                    else:
                        for move in l_diagonal:
                            if move[1] + tail[1] == head[1]: # moves it into the same y coord somake this move
                                tail[0] = tail[0] + move[0]
                                tail[1] = tail[1] + move[1]
            else:
                head[0] = head[0]+1
                for step in steps:
                    if tail[0] + step[0] == head[0] and tail[1] + step[1] == head[1]:
                        within_one_step = True   
                if not within_one_step:
                    # move in same column / row or move in diagonal
                    if tail[1] == head[1]: # it is in the same y, so just move right
                        tail[0] = tail[0]+1
                    else:
                        for move in r_diagonal:
                            if move[1] + tail[1] == head[1]: # moves it into the same y coord somake this move
                                tail[0] = tail[0] + move[0]
                                tail[1] = tail[1] + move[1]
            visited_grid[tail[0]][tail[1]] = True
            within_one_step = False
            # print(f"Head is at: {head[0]},{head[1]}, tail is at {tail[0]},{tail[1]}")
    count_visited = 0
    for line in visited_grid:
        for bool in line:
            if bool:
                count_visited = count_visited+1
    print(f"Part 1 Points Visited: {count_visited}")