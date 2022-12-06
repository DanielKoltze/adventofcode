file = open("5december.txt","r")
lines = file.readlines()

def calc():
    data = assignCrates()
    lines.pop(0)
    for line in lines:
        line = line.replace("move","")
        line = line.replace("from","")
        line = line.replace("to","")
        line = line.replace("\n","")
        line = line.strip()
        list = line.split(" ")
        removeEmpty(list,"")
        move = int(list[0])
        fro = int(list[1])-1
        to = int(list[2])-1
        placeholder = []
        for i in range(move):
            placeholder.append(data[fro].pop(0))
        for i in range(len(placeholder)):
            data[to].insert(0,placeholder.pop())
    result = ""
    for i in range(len(data)):
        result+=data[i].pop(0)
    result = result.replace("[","")
    result = result.replace("]","")
    print(result)


def loadCrates2():
    data = []
    try:
        while(lines[0] != '\n'):
            placeholder = lines.pop(0)
            list = []
            charNumber = 0
            while placeholder != '':
                list.append(placeholder[charNumber:charNumber+3])
                placeholder = placeholder[4:]
            data.append(list)
    except:
        data.pop()
        return data
    data.pop()
    return data

def removeEmpty(list,empty):
    while empty in list:
        list.remove(empty)


def assignCrates():
    data = loadCrates2()
    placeholder = []
    for i in range(len(data[0])):
        list = []
        for j in range(len(data)):
            list.append(data[j][i])
        placeholder.append(list)
    for list in placeholder:
       removeEmpty(list,"   ")
    return placeholder
    

calc()


