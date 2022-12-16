# https://adventofcode.com/2022/day/15
import sys
import re

target_row = 2000000
bound = 4000000
def manhattan_dist(point1,point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

def calc_points_in_row_for_mdist(sensors,beacons,target_row):
    r = []
    for sensor,beacon in zip(sensors.values(),beacons.values()):
        s_x,s_y = sensor[0],sensor[1]
        m_dist = manhattan_dist(sensor,beacon)
        delta_x = m_dist - abs(s_y-target_row)
        if delta_x < 0:
            continue
        range_y = [s_x-delta_x,s_x+delta_x]
        r.append(range_y)
    r.sort()
    merged_intervals = []
    merge_intervals(r, merged_intervals)
    return merged_intervals

def merge_intervals(r, merged_intervals):
    if len(r) >= 2:
        newInterval = r[0]
        merged_intervals.append(newInterval)
        for interval in r:
            if interval[0] <= newInterval[1]+1:
                newInterval[1] = max(interval[1],newInterval[1])
            else:
                newInterval = interval
                merged_intervals.append(newInterval)
               
#brute force work from center where center is Sensor coord
def generate_points_in_manhattan_dist(sensor,beacon,sensors,non_beacons,dist):
    min_x,min_y = sensor[0] - dist,sensor[1] - dist
    max_x,max_y = sensor[0] + dist,sensor[1] + dist

    for x in range(min_x,max_x+1):
        for y in range(min_y,max_y+1):
            if manhattan_dist(sensor,[x,y]) <= dist and [x,y] not in sensors.values() and [x,y] != beacon:
                non_beacons.add(tuple([x,y]))
                
if __name__ == "__main__":
    data = open(sys.argv[1]).read().splitlines()
    sensors,beacons = {},{}
    non_beacons = set()
    for i,line in enumerate(data):
        coords = re.findall(r'-?\d+', line)
        sensors[i] = [int(coords[0]),int(coords[1])]
        beacons[i] = [int(coords[2]),int(coords[3])]
    
    p1 = calc_points_in_row_for_mdist(sensors,beacons,target_row)
    print(f"Part 1: Positions in {target_row} that cannot contain a beacon is {p1[0][1]-p1[0][0]}")
    for y in range(bound+1):
        r = calc_points_in_row_for_mdist(sensors,beacons,y)
        if len(r) > 1:
            print(f"Part 2 Distress Beacon at {r[0][1]+1},{y} \nTuning Frequency is: {(r[0][1]+1)*4000000+y}")
            break