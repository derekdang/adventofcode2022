# https://adventofcode.com/2022/day/18
import sys

def p1():
    xyz = zip(xs,ys,zs)
    for cube in list(xyz):
        coords[cube] = 6
        for dir in dirs:
            neighbor = cube[0]+dir[0],cube[1]+dir[1],cube[2]+dir[2]
            if neighbor in coords:
                coords[cube] = coords[cube]-1
                coords[neighbor] = coords[neighbor]-1
    print("Part 1 Surface Area of Lava Droplets: " + str(sum(coords.values())))

def p2():
    min_x,max_x,min_y,max_y,min_z,max_z = min(xs),max(xs),min(ys),max(ys),min(zs),max(zs)
    air_pockets = set()
    surface_area_air = {}
    for i in range(min_x,max_x):
        for j in range(min_y,max_y):
            for k in range(min_z,max_z):
                if (i,j,k) not in coords:
                    if i > min_x and i < max_x and j > min_y and j < max_y and k > min_z and k < max_z:
                        air_pockets.add((i,j,k))
    open_air = set()
    queue = []
    for ap in air_pockets:
        if ap not in open_air:
            queue.append(ap)
        visited = set()
        contained = True
        while (len(queue) != 0 and contained):
            curr = queue.pop(0)
            visited.add(curr)
            for dir in dirs:
                step = curr[0]+dir[0],curr[1]+dir[1],curr[2]+dir[2]
                if step in coords:
                    continue
                if step in open_air:
                    contained = False
                    break
                if step[0] == min_x or step[0] == max_x or step[1] == min_y or step[1] == max_y or step[2] == min_z or step[2] == max_z:
                    #reached the edge
                    contained = False
                    break
                if step not in coords and step not in visited and step not in queue:
                    queue.append(step)
        if not contained:
            for abc in visited:
                open_air.add(abc)
                queue = []
    for abc in open_air:
        if abc in air_pockets:
            air_pockets.remove(abc)
    
    for ap in air_pockets:
        surface_area_air[ap] = 6
        for dir in dirs:
            neighbor = ap[0]+dir[0],ap[1]+dir[1],ap[2]+dir[2]
            if neighbor in surface_area_air:
                surface_area_air[ap] = surface_area_air[ap]-1
                surface_area_air[neighbor] = surface_area_air[neighbor]-1
    # Part 2 Solution is SA of Lava Droplet - SA of Air Pockets
    print("Part 2 Surface Area Excluding Air Pockets: " + str(sum(coords.values()) - sum(surface_area_air.values())))

if __name__ == "__main__":
    data = open(sys.argv[1]).read().splitlines()
    xs = []
    ys = []
    zs = []
    dirs = [[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]
    for line in data:
        l = line.split(',')
        xs.append(int(l[0]))
        ys.append(int(l[1]))
        zs.append(int(l[2]))
    coords = {}
    p1()
    p2()