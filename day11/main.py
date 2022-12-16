# https://adventofcode.com/2022/day/11
import sys
import re
class Monkey:
    def __init__(self, id, starting_items, test, truth_monkey, false_monkey):
        self.id = id
        self.starting_items = starting_items
        self.test = test
        self.truth_monkey = truth_monkey
        self.false_monkey = false_monkey
    
def operate_sample(id,item):
    ret = 0
    if id == 0:
        ret = item * 19
    elif id == 1:
        ret = item + 6
    elif id == 2:
        ret = item * item
    elif id == 3:
        ret = item + 3
    return ret

def operate(id,item):
    ret = 0
    if id == 0:
        ret = item * 3
    elif id == 1:
        ret = item + 3
    elif id == 2:
        ret = item + 5
    elif id == 3:
        ret = item * 19
    elif id == 4:
        ret = item + 1
    elif id == 5:
        ret = item + 2
    elif id == 6:
        ret = item * item
    elif id == 7:
        ret = item + 8
    return ret

if __name__ == "__main__":
    data = open(sys.argv[1]).read()
    monkey_data = list(filter(None,data.split("Monkey")))
    # print(monkey_data)
    
    monkeys = list()        
    for d in monkey_data:
        info = list(filter(None,d.split("\n")))
        # print(info)
        id,starting_items,operation,test,truth_monkey,false_monkey = -1,[],"",0,-1,-1
        for i,item in enumerate(info):
            if i == 0:
                id = int(re.findall(r'\d+', item)[0])
            elif i == 1:
                starting_items = []
                item_string = list(filter(None,item.strip().split("Starting items:")))
                for s in item_string[0].split(','):
                    starting_items.append(int(s))
            elif i == 2:
                operation = item.split("=")[1].strip()
            elif i == 3:
                test = int(re.findall(r'\d+',item)[0])
            elif i == 4:
                truth_monkey = int(re.findall(r'\d+',item)[0])
            else:
                false_monkey = int(re.findall(r'\d+',item)[0])
        
        monkey = Monkey(id,starting_items, test, truth_monkey,false_monkey)
        monkeys.append(monkey)
    monkey_inspect_count = [0,0,0,0,0,0,0,0]
    for i in range(10000):
        for monkey in monkeys:
            # print(i, monkey.starting_items)
            for items in monkey.starting_items:
                monkey_inspect_count[monkey.id] = monkey_inspect_count[monkey.id] + 1
                item_worry = operate(monkey.id,items)
                item_worry = item_worry%9699690
                if item_worry % monkey.test == 0:
                    monkey_to_add = monkeys[monkey.truth_monkey]
                    monkey_to_add.starting_items.append(item_worry)
                else:
                    monkey_to_add = monkeys[monkey.false_monkey]
                    monkey_to_add.starting_items.append(item_worry)
            monkey.starting_items = []
    print(monkey_inspect_count)
    monkey_inspect_count = sorted(monkey_inspect_count,reverse=True)
    print(monkey_inspect_count[0] * monkey_inspect_count[1])
    