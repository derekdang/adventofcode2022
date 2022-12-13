# https://adventofcode.com/2022/day/4
import sys
import ast
import itertools

if __name__ == "__main__":
    data = open(sys.argv[1]).read().split("\n\n")
    pairs = [] 
    for pair in data:
        input = (pair.split('\n'))
        l = [ ast.literal_eval(x) for x in input]
        pairs.append(l)
    # print(pairs)
    correct_pairs = 0
    for i,pair in enumerate(pairs):
        print(f"Pair: {pair}")
        lhs = [pair[0]]
        rhs = [pair[1]]
        right_order = True
        while (len(lhs) != 0):
            l_item = lhs.pop(0)
            if (len(rhs) != 0):
                r_item = rhs.pop(0)
            else:
                right_order = False
                break
            if (isinstance(l_item,list) and isinstance(r_item,list)):
                # compare the lists
                print(f"Compare {l_item} vs {r_item}")
                for l,r in itertools.zip_longest(l_item,r_item,fillvalue=None):
                    print(l,r)
                    if isinstance(l,int):
                        l = [l]
                    if isinstance(r,int):
                        r = [r]
                    if r == None:
                        right_order = False
                        break
                    if l == None:
                        break
                    if l > r:
                        print(f"Compare: {l} vs {r}")
                        right_order = False
                        break
                    if l < r:
                        print(f"Compare: {l} vs {r}")
                        break
                    print(f"Compare: {l} vs {r}")
            elif isinstance(l_item,int) and isinstance(r_item,int):
                if l_item > r_item:
                    print(f"Compare: {l_item} vs {r_item}")
                    right_order = False
                print(f"Compare: {l_item} vs {r_item}")
            elif isinstance(l_item,int) and isinstance(r_item,list):
                l_list = [l_item]
                for l,r in itertools.zip_longest(l_list,r_item,fillvalue=None):
                    print("lhs turned list - ",l,r)
                    if r == None:
                        right_order = False
                        break
                    if l > r:
                        print(f"Compare: {l} vs {r}")
                        right_order = False
                        break
                    if l == None:
                        break
                    if l < r:
                        print(f"Compare: {l} vs {r}")
                        break
                    print(f"Compare: {l} vs {r}")
            elif isinstance(l_item,list) and isinstance(r_item,int):
                r_list = [r_item]
                for l,r in itertools.zip_longest(l_item,r_list,fillvalue=None):
                    print("rhs turned list - ",l,r)
                    if r == None:
                        right_order = False
                        break
                    if l > r:
                        print(f"Compare: {l} vs {r}")
                        right_order = False
                        break
                    if l < r:
                        print(f"Compare: {l} vs {r}")
                        break
                    print(f"Compare: {l} vs {r}")
        
            
        if right_order:
            correct_pairs = correct_pairs + (i+1)
            print(f"Correct Pair Score: updated with {i+1} now {correct_pairs}")