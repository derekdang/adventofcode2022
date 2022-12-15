# https://adventofcode.com/2022/day/13
import sys
import ast
import itertools
import functools

def compare(l_item, r_item):
    ret = 0    
    for l,r in itertools.zip_longest(l_item,r_item,fillvalue=None):
        if isinstance(l,int) and isinstance(r,list):
            ret = compare_l_int_to_rlist(l,r,1)
        elif isinstance(l,list) and isinstance(r,int):
            ret = compare_llist_to_r_int(l,r,1)
        elif isinstance(l,list) and isinstance(r,list):
            ret = compare_lists(l,r,1)
        elif r == None:
            return 1
        elif l == None:
            return -1
        elif l < r:
            return -1
        elif l > r:
            return 1
        if ret != 0:
            return ret
        continue
    return 0

def compare_lists(l_item, r_item,tab_no):
    for l,r in itertools.zip_longest(l_item,r_item,fillvalue=None):
        print(tab_no*"\t" + f"Compare {l} vs {r}")
        if isinstance(l,int) and isinstance(r,list):
            return compare_l_int_to_rlist(l,r,tab_no+1)
        elif isinstance(l,list) and isinstance(r,int):
            return compare_llist_to_r_int(l,r,tab_no)
        elif isinstance(l,list) and isinstance(r,list):
            return compare_lists(l,r,tab_no+1)
        elif r == None:
            print(tab_no*"\t"+"Right side ran out of items, so inputs are not in the right order")
            return 1
        elif l == None:
            print(tab_no*"\t"+"Left side ran out of items, so inputs are in the right order")
            return -1
        elif l < r:
            print(tab_no*"\t"+"Left side is smaller, so inputs are in the right order")
            return -1
        elif l > r:
            print(tab_no*"\t"+"Right side is smaller, so inputs are not in the right order")
            return 1
        continue
    return 0
        
def compare_llist_to_r_int(l_item, r_item, tab_no):
    print(tab_no*"\t"+f"Mixed types; convert right to [{r_item}] and retry comparison")
    r_list = [r_item]
    print(tab_no*"\t"f"Compare {l_item} vs {r_list}")
    for l,r in itertools.zip_longest(l_item,r_list,fillvalue=None):
        tab_no = tab_no+1
        print(tab_no*"\t"+f"Compare {l} vs {r}")
        tab_no = tab_no+1
        if isinstance(l,list) and len(l) == 0:
            print(tab_no*"\t"+"Left side ran out of items, so inputs are in the right order")
            return -1
        elif isinstance(l,list) and isinstance(r,int):
            return compare_llist_to_r_int(l,r,tab_no+1)
        elif r == None:
            print(tab_no*"\t"+"Right side ran out of items, so inputs are not in the right order")
            return 1
        elif l == None:
            print(tab_no*"\t"+"Left side ran out of items, so inputs are in the right order")
            return -1
        elif l < r:
            print((tab_no+1)*"\t"+"Left side is smaller, so inputs are in the right order")
            return -1
        elif l > r:
            print((tab_no+1)*"\t"+"Right side is smaller, so inputs are not in the right order")
            return 1
    return 0

def compare_l_int_to_rlist(l_item, r_item, tab_no):
    tab_no = tab_no+1
    print(tab_no*"\t"+f"Mixed types; convert left to [{l_item}] and retry comparison")
    l_list = [l_item]
    print(tab_no*"\t"+f"Compare {l_list} vs {r_item}")
    for l,r in itertools.zip_longest(l_list,r_item,fillvalue=None):
        tab_no = tab_no+1
        print(tab_no*"\t"+f"Compare {l} vs {r}")
        if isinstance(r,list) and len(r) == 0:
            print(tab_no*"\t"+"Right side ran out of items, so inputs are not in the right order")
            return 1
        elif isinstance(l,int) and isinstance(r,list):
            return compare_l_int_to_rlist(l,r,tab_no+1)
        elif r == None:
            print(tab_no*"\t"+"Right side ran out of items, so inputs are not in the right order")
            return 1
        elif l == None:
            print(tab_no*"\t"+"Left side ran out of items, so inputs are in the right order")
            return -1
        elif l < r:
            print((tab_no+1)*"\t"+"Left side is smaller, so inputs are in the right order")
            return -1
        elif l > r:
            print((tab_no+1)*"\t"+"Right side is smaller, so inputs are not in the right order")
            return 1
    return 0

if __name__ == "__main__":
    data = open(sys.argv[1]).read().split("\n\n")
    pairs = []
    all_packets = []
    for pair in data:
        input = pair.split('\n')
        l = [ ast.literal_eval(x) for x in input]
        dup = [ ast.literal_eval(x) for x in input]
        pairs.append(l)
    correct_pairs = 0
    for i,pair in enumerate(pairs):
        
        lhs = pair[0].copy()
        rhs = pair[1].copy()
        all_packets.append(pair[0])
        all_packets.append(pair[1])
        print(f"\nCompare: {lhs} vs {rhs}")
        
        right_order = 0
        if len(lhs) == 0:
            print("Left side ran out of items, so inputs are in the right order")
            right_order = -1
                
        while (len(lhs) != 0 and right_order==0):
            l_item = lhs.pop(0)
            if len(rhs) == 0:
                print("\tRight side ran out of items, so inputs are not in the right order")
                right_order = 1
                break
            else:
                r_item = rhs.pop(0)
            
            print(f"\tCompare {l_item} vs {r_item}")
            if isinstance(l_item,int) and isinstance(r_item,int):
                if l_item < r_item:
                    print("\t\tLeft side is smaller, so inputs are in the right order")
                    right_order = -1
                    break
                elif l_item > r_item:
                    print("\t\tRight side is smaller, so inputs are not in the right order")
                    right_order = 1
                    break
            elif isinstance(l_item,list) and isinstance(r_item,list):
                right_order = compare_lists(l_item, r_item,1)
            elif isinstance(l_item,list) and isinstance(r_item,int):
                right_order = compare_llist_to_r_int(l_item, r_item,1)
            elif isinstance(l_item,int) and isinstance(r_item,list):
                right_order = compare_l_int_to_rlist(l_item, r_item,1)
            if len(lhs) == 0 and len(rhs) != 0 and right_order==0:
                print("Left side ran out of items, so inputs are in the right order")
                right_order = -1
                break
        if right_order==-1:
            correct_pairs = correct_pairs + (i+1)
            print(f"Part 1 Correct Pair Score: updated with {i+1} now {correct_pairs}")
        print(correct_pairs)

    all_packets.append([[2]])
    all_packets.append([[6]])

    all_packets = (sorted(all_packets,key=functools.cmp_to_key(compare)))
    two_packet_index = all_packets.index([[2]])+1
    six_packet_index = all_packets.index([[6]])+1
    print(f"Part 2: {two_packet_index*six_packet_index}") # sort is currently off by 1 :/