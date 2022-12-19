# https://adventofcode.com/2022/day/16
import sys
import re
import copy
def print_valves(valves):
    for item in valves:
        print(item)
class Valve:
    def __init__(self, id, flow_rate):
        self.id = id
        self.is_open = False
        self.flow_rate = flow_rate
        self.connecting_valves = []
    
    def open(self):
        self.is_open = True
    
    def close(self):
        self.is_open = False
    
    def add_paths(self, tunnel_to_valves):
        for i in tunnel_to_valves:
            self.connecting_valves.append(i.strip())
    
    def calc_flow_with_time(self, minutes):
        return self.flow_rate*minutes

    def flow(self):
        return self.flow_rate

    def __str__(self):    
        return f"Valve: {self.id}\nOpen: {self.is_open}\nflow rate: {self.flow_rate}\n{self.connecting_valves}\n"

def find_shortest_path_between_valves(valves,visited_valves,v1,v2):
    if v1.id == v2.id:
        return 0
    visited_valves.append(v1.id)
    min_path = 1000
    for conn_valve in v1.connecting_valves:
        if conn_valve not in visited_valves:
            min_path = min(min_path,1 + find_shortest_path_between_valves(valves,copy.deepcopy(visited_valves),valves[conn_valve],v2))
    if min_path == 1000:
        return 1000
    else:
        return min_path

def p1(valves,open_valves,nonzero_valves,curr_valve,minute,total_flow_rate,sum_flow):
    if sorted(open_valves) == sorted(nonzero_valves):
        print("all valves open")
        print(sum_flow)
        return
    # look at nonzero valves and find the best production
    dist_map,production = {},{}
    max_dist = -1
    for nz_valve in nonzero_valves:
        if nz_valve not in open_valves:
            target_valve = valves[nz_valve]
            dist = find_shortest_path_between_valves(valves,[],curr_valve,target_valve)
            max_dist = max(dist,max_dist)
            dist_map[nz_valve] = dist
    
    best_move,best_prod = '',-1
    for nz_valve in dist_map:
        production = (30 - minute - (max_dist - dist_map[nz_valve] + 1)) * (total_flow_rate+valves[nz_valve].flow_rate)
        if production > best_prod:
            best_prod = production
            best_move = nz_valve
    open_valves.append(best_move)
    print(f"opening: {best_move}")
    dest_valve = valves[best_move]
    s_flow = total_flow_rate*(dist_map[best_move]+1)
    p1(valves,open_valves,nonzero_valves,dest_valve, minute+dist_map[best_move]+1, total_flow_rate+dest_valve.flow_rate,s_flow)

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

    open_valves = []
    # recursive traversal
    pos = "AA"
    minute,total_flow_rate,sum_flow = 0,0,0
    curr_valve = valves[pos]
    actions = []
    # explore(valves,open_valves,actions,curr_valve,minute,total_flow_rate,total_flow)
    # print(find_shortest_path_between_valves(valves,[],valves['BB'],valves['HH']))
    p1(valves,open_valves,nonzero_valves,curr_valve,minute,total_flow_rate,sum_flow)