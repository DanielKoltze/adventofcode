file = open("1december.txt","r")
lines = file.readlines()








def addTop3Numbers(array,number):
    minNumber = min(array)
    if number > minNumber:
        array.remove(minNumber)
        array.append(number)
    return array



def calc():
    placeholder = 0
    result = [0,0,0]
    for line in lines:
        if line != '\n':
            placeholder += int(line)
        else:
            result = addTop3Numbers(result,placeholder)
            placeholder = 0
    realResult = 0
    for number in result:
        realResult += number
    print(realResult)
            
calc()