# https://adventofcode.com/2022/day/3
import sys

if __name__ == "__main__":
    data = open(sys.argv[1]).read().splitlines()
    total = 0
    for line in data:
        length = len(line)
        mid = int(length/2)
    
        first = line[0:mid]
        second = line[mid:length]
        for char in first:
            if char in second:
                if (char.isupper()):
                    val = ord(char) - 38
                else:
                    val = ord(char) - 96
                total += val
                break
    print(f"Part 1 Sum of Priorities: {total}")

    part2 = 0
    for l1,l2,l3 in zip(data[0::3], data[1::3], data[2::3]):
        for char in l1:
            if char in l2 and char in l3:
                if (char.isupper()):
                    val = ord(char) - 38
                else:
                    val = ord(char) - 96
                part2 += val
                break
    print(f"Part 2 Sum of Triplet Priorities: {part2}")
