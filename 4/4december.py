lines = open("4december.txt","r").readlines()

def calc():
    result = 0
    for line in lines:
        split = line.split(',')
        firstSection = getNumbers2(split[0])
        secondSection = getNumbers2(split[1])
        result += checkContains2(firstSection,secondSection)
    print(result)
     


def getNumbers(numbers):
    numb = numbers.split("-")
    section = []
    section.append("-")
    for number in range(int(numb[0]),int(numb[1])+1):
        section.append(str(number)+ "-")
    return "".join(section)
    


def checkContains(first,second):
    if first in second or second in first:
        return 1
    return 0

def getNumbers2(numbers):
    numb = numbers.split("-")
    section = []
    for number in range(int(numb[0]),int(numb[1])+1):
        section.append(number)
    return section
    

def checkContains2(firstList,secondList):
    for first in firstList:
        for second in secondList:
            if first == second:
                return 1
    return 0

calc()

