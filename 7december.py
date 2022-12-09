file = open("7december.txt", "r")
placeholder = file.readlines()
lines = [line.strip() for line in placeholder]

directories = [{"/":0}]

path = []
def solve():
    list = []
    alreadyExists = False
    for line in lines:
        if "$ cd" in line:
            if ".." in line: 
                path.pop()
            else:
                path.append(line[5:])
        elif "$ ls" in line:
            space = 0
        else:
            if not "dir" in line[:3]:
                pathName = ""
                storedFile = line.split(" ")
                for i in range(len(path)):
                    pathName += " " + path[i]
                space += int(storedFile[0])
                if alreadyExists == True:
                    list.pop()
                alreadyExists = True
                list.append(pathName[1:] + " " + str(space))
                continue
        alreadyExists = False
    print(list)
    list = amountinDir(list)
    opg1(list)
def amountinDir(list):
    result = []
    for dir in range(len(list)):
        checkDir = list[dir].rsplit(" ", 1)
        result.append(int(checkDir[1]))
        for otherDir in range(dir+1, len(list)):
            checkOtherDir = list[otherDir].rsplit(" ", 1)
            if checkDir[0] in checkOtherDir[0]:
                number = result.pop()
                result.append(int(number)+int(checkOtherDir[1]))
    return result
      
      
def opg1(list):
    result = 0
    for number in list:
        if number < 100000:
            result += number
    #print(result)

solve()