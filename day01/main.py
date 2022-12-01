import sys

if __name__ == "__main__":
    data = open(sys.argv[1]).read().splitlines()
    total,max_calories = 0,0
    arr = list()
    for line in data:
        if line == "":
            max_calories = max(total,max_calories)
            arr.append(total)
            total = 0
        else:
            total = total + int(line)
    print(f"Part 1 Highest Calorie Elf: {max_calories}")
    arr.sort(reverse=True)
    ans = arr[0]+arr[1]+arr[2]
    print(f"Part 2 Three Highest Calorie Elves: {ans}")