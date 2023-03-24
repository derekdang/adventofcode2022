import sys


# iterate through the blocks and see how many it neighbors, if it neighbors increase the count
# iterate through after = sum(6 - #of neighbors)???
def p1():
    xyz = zip(xs,ys,zs)
    coords = {}
    for cube in list(xyz):
        coords[cube] = 6
        for dir in dirs:
            neighbor = cube[0]+dir[0],cube[1]+dir[1],cube[2]+dir[2]
            if neighbor in coords:
                coords[cube] = coords[cube]-1
                coords[neighbor] = coords[neighbor]-1
    # print(coords)
    print("Part 1 Surface Area of Lava Droplets: " + str(sum(coords.values())))

    min_x,max_x,min_y,max_y,min_z,max_z = min(xs),max(xs),min(ys),max(ys),min(zs),max(zs)
    num_air_pockets = 0
    for i in range(min_x,max_x):
        for j in range(min_y,max_y):
            for k in range(min_z,max_z):
                if (i,j,k) not in coords:
                    num_neighbors = 0
                    for dir in dirs:
                        neighbor = i+dir[0],j+dir[1],k+dir[2]
                        if neighbor in coords:
                            num_neighbors = num_neighbors+1
                    if num_neighbors == 6:
                        num_air_pockets = num_air_pockets+1
                        for dir in dirs:
                            neighbor = i+dir[0],j+dir[1],k+dir[2]
    print("Part 2 Surface Area Exlucding Air Pockets: " + str(sum(coords.values()) - num_air_pockets*6))
                    
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
    p1()