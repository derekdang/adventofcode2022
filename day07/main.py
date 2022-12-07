# https://adventofcode.com/2022/day/7
import sys
def traverse(file_system, dir_sizes):
    total_size = 0
    for _,v in file_system.items():
        if isinstance(v,dict):
            total_size = total_size + traverse(v,dir_sizes)
        else:
            total_size = total_size + v
    if total_size < 100000:
        dir_sizes.append(total_size)
    return total_size

def find_total_size(file_system):
    total_size = 0
    for _,v in file_system.items():
        if isinstance(v,dict):
            total_size = total_size + find_total_size(v)
        else:
            total_size = total_size + v
    
    return total_size

def find_closest_min_dir_to_delete(file_system, meets_criteria):
    total_size = 0
    for _,v in file_system.items():
        if isinstance(v,dict):
            total_size = total_size + find_closest_min_dir_to_delete(v, meets_criteria)
        else:
            total_size = total_size + v
    if total_size >= 8008081:
        meets_criteria.append(total_size) 
    return total_size

if __name__ == "__main__":
    data = open(sys.argv[1]).read().splitlines()
    current_dir = {}
    path = "/"
    file_system = {"/":{}}
    info = []
    is_ls = False
    for line in data:
        if is_ls and not line.startswith("$"):
            info.append(line)
        if line.startswith("$"):
            # print(file_system)
            #add info to the file system
            #navigate to the right dict according to path:
            if len(info) != 0:
                folders = list(filter(None,path.split('/')))
                
                current_dir = file_system["/"]
                if path != "/":
                    for folder in folders:
                        current_dir = current_dir[folder]

                for i in info:
                    parse = i.split(" ")
                    if parse[0] == "dir":
                        current_dir[parse[1]] = {}
                    else:
                        current_dir[parse[1]] = int(parse[0])
                info = []

            line = line[1:].strip()
            split = line.split(" ")
            command = split[0]
            if command == "cd":
                is_ls = False
                dir = split[1]
                if dir == "..":
                    path = path[0:len(path)-2]
                    ind = path.rfind("/")
                    path = path[0:ind+1]

                else:
                    if split[1] == "/":
                        path = "/"
                    else:
                        path = path + split[1] + "/"
            else:
                is_ls = True
    # flush out rest of file system if last line is ls
    if len(info) != 0:
        folders = list(filter(None,path.split('/')))
                
        current_dir = file_system["/"]
        if path != "/":
            for folder in folders:
                current_dir = current_dir[folder]
        for i in info:
            parse = i.split(" ")
            if parse[0] == "dir":
                current_dir[parse[1]] = {}
            else:
                current_dir[parse[1]] = int(parse[0])
    
    size = 0
    dir_sizes = []
    for k,v in file_system.items():
        traverse(v,dir_sizes)
    print(f"Part 1: {sum(dir_sizes)}")
    total_size = find_total_size(file_system)
    unused_space = 70000000-48008081
    space_to_free = 30000000 - 21991919
    print(f"Space minimum needed to delete: {space_to_free}")
    meets_deletion_criteria = []
    find_closest_min_dir_to_delete(file_system, meets_deletion_criteria)
    meets_deletion_criteria.sort()
    print(f"Part 2: {meets_deletion_criteria[0]}")