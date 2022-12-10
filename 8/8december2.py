file = open("8december.txt","r")
lines = file.readlines()

def solve():
    result = 0
    map = []
    #create 2d array
    for line in lines:
        listOfChar = list(line.strip())
        listOfChar = ([int(x) for x in listOfChar])
        map.append(listOfChar)
    #run though 2d array
    for i in range(len(map)):
        for j in range(len(map[i])):
            #gets list of edges
            edges = getViews(map, j, i)
            #result += treeValid(edges, map[i][j])
    print(result)

def getViews(map,x,y):
    #top right bottom left. minus hvis ingen edge
    x = 2
    y = 3
    result = [1,1,1,1]
    if x == 0 or y == 0 or x == len(map[y])-1 or y == len(map)-1:
        return []
    #get biggest top
    top = True
    for ys in range(y-1,-1,-1):
        if map[ys][x] < map[y][x] and top and ys-1 > 0:
            result[0] += 1
        else:
            top = False
    #get biggest bottom
    bottom = True
    for ys in range(y+1,len(map)):
        if map[ys][x] < map[y][x] and bottom and ys+1 < len(map):
            result[2] += 1
        else:
            bottom = False
    #get biggest right
    right = True
    for xs in range(x+1,len(map[y])):
        if map[y][xs] < map[y][x] and right and xs+1 < len(map[y]):
            result[1] += 1
        else:
            right = False
    #get biggest left
    left = True
    for xs in range(x-1,-1,-1):
        if map[y][xs] < map[y][x] and left and x-xs > 0:
            result[3] += 1
        else:
            left = False
    return result
   
def treeValid(list, tree):
    for number in list:
        if number < tree or number == -1:
            return 1
    return 0

solve()