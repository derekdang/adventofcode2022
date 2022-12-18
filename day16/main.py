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

def explore(valves,open_valves,helper,actions,curr_valve,minute,total_flow_rate,total_flow):
    if minute == 0:
        return total_flow_rate
    print(f"Currently at {curr_valve.id}, open valves are: {open_valves} at minute {minute} with total_flow_rate of {total_flow_rate}")
    if minute not in helper:
        helper[minute] = [total_flow_rate, curr_valve, copy.deepcopy(open_valves)]
    else:
        
    if total_flow_rate > helper[minute][0]:
        helper[minute] = [total_flow_rate, curr_valve, copy.deepcopy(open_valves)]
    if curr_valve.flow_rate == 0 or curr_valve.id in open_valves:
        for conn_valve in curr_valve.connecting_valves:
            actions.append(f"You move to valve {conn_valve}")
            explore(valves,copy.deepcopy(open_valves), helper, copy.deepcopy(actions),valves[conn_valve],minute-1,total_flow_rate,total_flow+total_flow_rate)
            actions.pop()
    else:
        valve_to_open = curr_valve.id
        valve_to_open_rate = curr_valve.flow_rate
        for conn_valve in curr_valve.connecting_valves:
            if valve_to_open_rate < valves[conn_valve].flow_rate and conn_valve not in open_valves:
                valve_to_open = conn_valve
                valve_to_open_rate = valves[conn_valve].flow_rate
        if valve_to_open == curr_valve.id:
            open_valves.append(curr_valve.id)
            actions.append(f"You open valve {curr_valve.id}")
            explore(valves,copy.deepcopy(open_valves), helper,copy.deepcopy(actions),curr_valve,minute-1,total_flow_rate+curr_valve.flow(),total_flow+total_flow_rate)
            actions.pop()
            open_valves.remove(curr_valve.id)
        else:
            actions.append(f"You move to valve {valve_to_open}")
            explore(valves,copy.deepcopy(open_valves), helper,copy.deepcopy(actions),valves[valve_to_open], minute-1,total_flow_rate, total_flow+total_flow_rate)

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
    minute,total_flow_rate,total_flow = 30,0,0
    curr_valve = valves[pos]
    actions = []
    helper = dict()
    explore(valves,open_valves,helper,actions,curr_valve,minute,total_flow_rate,total_flow)