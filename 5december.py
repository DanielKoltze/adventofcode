file = open("5december.txt","r")
lines = file.readlines()

def loadCrates():
    data = []
    data2 = []
    while(lines[0] != '\n'):
        placeholder = lines.pop(0)
        list = []
        charNumber = 0
        while placeholder != '':
            list.append(placeholder[charNumber:charNumber+3])
            placeholder = placeholder[4:]
        data2.append(list)
    data2.pop()
    for i in range(len(data2)):
        list = []
        for j in range(len(data2[i])):
            list.append(data2[j][i])
        data.append(list)
    for list in data:
       removeEmpty(list,"   ")
    return data

def removeEmpty(list,empty):
    while empty in list:
        list.remove(empty)



def calc():
    data = loadCrates()
    lines.pop(0)
    for line in lines:
        move = int(line[5:6])
        fro = int(line[12:13])-1
        to = int(line[17:18])-1
        for i in range(move):
            parse = data[fro].pop(0)
            data[to].insert(0,parse)
    result = ""
    for i in range(len(data)):
        result+=data[i].pop(0)
    result = result.replace("[","")
    result = result.replace("]","")
    print(result)

calc()
    
