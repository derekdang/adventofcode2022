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

def explore(valves,curr_valve,minute,open_valves,total_flow,cumulative_flow_rate):
    print(curr_valve.id, minute)
    total_flow = total_flow + cumulative_flow_rate
    if minute == 0:
        return total_flow
    
    # case for all valves w/ flow opened?

    if curr_valve.id not in open_valves and curr_valve.flow_rate != 0:
        open_valves.add(curr_valve.id)
        total_flow = max(total_flow,explore(valves,curr_valve,minute-1,copy.deepcopy(open_valves),total_flow,cumulative_flow_rate+curr_valve.flow_rate))
        open_valves.remove(curr_valve.id)
            
    for i in curr_valve.connecting_valves:
        conn_valve = valves[i]
        total_flow = max(total_flow,explore(valves,conn_valve,minute-1,copy.deepcopy(open_valves),total_flow,cumulative_flow_rate))
    
    return total_flow

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

    
    open_valves = set()
    # recursive traversal
    pos = "AA"
    total_flow = 0
    
    current_valve = valves[pos]
    explore(valves,current_valve,30,open_valves,total_flow,0)