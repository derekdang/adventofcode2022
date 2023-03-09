# https://adventofcode.com/2022/day/16
import sys
import re

def print_grid(grid):
    p = ""
    for g_y,line in enumerate(grid):
        p = ""
        for g_x,item in enumerate(line):
            p = p + " " + str(grid[g_y][g_x])
        print(p)

def print_valves(valves):
    for item in valves:
        print(item)

class Valve:
    def __init__(self, id, flow_rate):
        self.id = id
        self.is_open = False
        self.flow_rate = flow_rate
        self.connecting_valves = []
    
    def add_paths(self, tunnel_to_valves):
        for i in tunnel_to_valves:
            self.connecting_valves.append(i.strip())
    
    def flow(self):
        return self.flow_rate

    def __str__(self):    
        return f"Valve: {self.id}\nflow rate: {self.flow_rate}\n{self.connecting_valves}\n"

def helper(curr_valve,valves,open_valves,dist_matrix,minute,flow_rate,sum_flow):
    sum = sum_flow + flow_rate
    if (minute > 30):
        return -1
    if (len(open_valves) == len(nonzero_valves)):
        return (30-minute)*flow_rate+sum_flow
    if (minute == 30):
        print(flow_rate)
        return sum
    # print(curr_valve.id + " " +str(minute))
    # if the curr valve has a nonzero flow rate then either open it or go to adj, if zero flow rate go to adj
    ans = 0
    if curr_valve.flow_rate > 0:
        if curr_valve.id not in open_valves:
            open_valves.append(curr_valve.id)
            ans = max(ans,helper(curr_valve,valves,open_valves,dist_matrix,minute+1,flow_rate+curr_valve.flow_rate,sum))
            open_valves.remove(curr_valve.id)
        for v_id in dist_matrix[curr_valve.id]:
            if v_id not in open_valves:
                dist_in_minutes = dist_matrix[curr_valve.id][v_id]
                if dist_in_minutes + minute <= 30:
                    ans = max(ans,helper(valves[v_id],valves,open_valves,dist_matrix,minute+dist_in_minutes,flow_rate,sum+((dist_in_minutes-1)*flow_rate)))
    else:
        for v_id in dist_matrix[curr_valve.id]:
            if v_id not in open_valves:
                dist_in_minutes = dist_matrix[curr_valve.id][v_id]
                if dist_in_minutes + minute <= 30:
                    ans = max(ans,helper(valves[v_id],valves,open_valves,dist_matrix,minute+dist_in_minutes,flow_rate,sum+((dist_in_minutes-1)*flow_rate)))

    # if curr_valve.flow_rate > 0:
    #     if curr_valve.id not in open_valves:
    #         open_valves.append(curr_valve.id)
    #         ans = max(ans,helper(curr_valve,valves,open_valves,minute+1,flow_rate+curr_valve.flow_rate,sum))
    #         open_valves.remove(curr_valve.id)
    #     for valve in adj_valves:
    #         ans = max(ans,helper(valves[valve],valves,open_valves,minute+1,flow_rate,sum))
    # else:
    #     for valve in adj_valves:
    #         ans = max(ans,helper(valves[valve],valves,open_valves,minute+1,flow_rate,sum))
    return ans

def p1():
    ans1 = helper(curr_valve,valves,open_valves,dist_matrix,minute,flow_rate,sum_flow)
    print(ans1)

if __name__ == "__main__":
    data = open(sys.argv[1]).read().splitlines()
    valves = {}
    nonzero_valves = []
    for line in data:
        valve = re.search(r'(?<=Valve)(.*)(?=has)',line).group().strip()
        flow_rate = int(re.search(r'\d+',line).group())
        tunnel_to_valves = re.search(r'(?<=valve)(.*)',line).group()[1:].split(',')

        new_valve = Valve(valve,flow_rate)
        new_valve.add_paths(tunnel_to_valves)
        if flow_rate > 0:
            nonzero_valves.append(valve)
        valves[valve] = new_valve
    
    dist_matrix = {}
    for valve in valves:
        dist_matrix[valve] = {}   
    for valve in valves:
        q = []
        q.append(valve)
        dist = 0
        visited = []
        while(len(q) != 0):
            q_size = len(q)
            i = 0
            while(i < q_size):
                v = valves[q.pop(0)]
                visited.append(v.id)
                if (v.id in nonzero_valves and v.id != valve):
                    dist_matrix[valve][v.id] = dist
                for conn_valve in v.connecting_valves:
                    if conn_valve not in visited:
                        q.append(conn_valve)
                i = i+1
            dist = dist+1

    open_valves = []
    pos = "AA"
    minute,flow_rate,sum_flow = 1,0,0
    curr_valve = valves[pos]
    p1()