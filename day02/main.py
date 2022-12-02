# https://adventofcode.com/2022/day/2
import sys

if __name__ == "__main__":
    data = open(sys.argv[1]).read().splitlines()
    rock_map = {'r':3, 'p':6, 's':0}
    paper_map = {'r':0, 'p':3, 's':6}
    scissor_map = {'r':6, 'p':0, 's':3}
    total = 0
    for line in data:
        split = line.split(' ')
        score = 0
        mapping = dict()
        
        if split[0] == 'A': #rock
            mapping = rock_map
        elif split[0] == 'B':
            mapping = paper_map
        else:
            mapping = scissor_map
        
        if split[1] == 'X': #rock
            score = 1 + mapping['r']
        elif split[1] == 'Y': #paper
            score = 2 + mapping['p']
        else: #scissor
            score = 3 + mapping['s']
        total += score
    print(f"Part 1 Total Score: {total}")

    rock_map = {'r':3, 'p':1, 's':2}
    paper_map = {'r':1, 'p':2, 's':3}
    scissor_map = {'r':2, 'p':3, 's':1}
    total = 0
    for line in data:
        split = line.split(' ')
        score = 0
        mapping = dict()
        
        if split[0] == 'A': #rock
            mapping = rock_map
        elif split[0] == 'B':
            mapping = paper_map
        else:
            mapping = scissor_map
        
        if split[1] == 'X': #lose
            score = 0 + mapping['r']
        elif split[1] == 'Y': #draw
            score = 3 + mapping['p']
        else: #win
            score = 6 + mapping['s']
        total += score
    print(f"Part 2 Total Score: {total}")