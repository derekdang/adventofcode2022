# https://adventofcode.com/2022/day/4
import sys

if __name__ == "__main__":
    data = open(sys.argv[1]).read().splitlines()
    part1 = 0
    part2 = 0
    for line in data:
        split = line.split(',')
        p1 = split[0].split('-')
        p2 = split[1].split('-')
        long,short = [],[]
        if int(p1[1])-int(p1[0])+1 <= int(p2[1])-int(p2[0])+1:
            short = p1
            long = p2
        else:
            short = p2
            long = p1
        s1,s2,l1,l2 = int(short[0]), int(short[1]), int(long[0]), int(long[1])
        if s1 >= l1 and s2 <= l2:
            part1 = part1 + 1
        if (s1 >= l1 and s1 <= l2) or (s2 <= l2 and s2 >= l1):
            part2 = part2 + 1
    print(f"Part 1 Total Overlap: {part1}")
    print(f"Part 2 Partial Overlap: {part2}")