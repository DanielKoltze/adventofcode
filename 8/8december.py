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
            current = map[i][j]
            #gets list of edges
            edges = getEdges(map, j, i)
            result += treeValid(edges, map[i][j])
    print(result)

def getEdges(map,x,y):
    #top right bottom left. minus hvis ingen edge
    edges = [-1,-1,-1,-1]
    #get biggest top
    for yCheck in range(y):
        if(edges[0] < map[yCheck][x]):
            edges[0] = map[yCheck][x]
    for xCheck in range(x):
        if(edges[3] < map[y][xCheck]):
            edges[3] = map[y][xCheck]
    for yCheck in range(y+1,len(map)):
        if(edges[2] < map[yCheck][x]):
            edges[2] = map[yCheck][x]
    for xCheck in range(x+1,len(map[y])):
         if(edges[1] < map[y][xCheck]):
             edges[1] = map[y][xCheck]
    return edges
   
def treeValid(list, tree):
    for number in list:
        if number < tree or number == -1:
            return 1
    return 0

solve()