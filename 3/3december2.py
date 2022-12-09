import string
file = open("3december.txt","r")
lines = file.readlines()

def calc():
    result = 0
    lineNumber = 0
    length = len(lines)//3
    for x in range(length):
        first = getLine(lineNumber)
        lineNumber += 1
        second = getLine(lineNumber)
        lineNumber += 1
        third = getLine(lineNumber)
        lineNumber += 1
        letter = findEqualLetter(first,second,third)
        result = result + calcPoints(letter)
    print(result)

def getLine(number):
    return lines[number]


def findEqualLetter(first, second, third):
    for firstLetter in first:
        for secondLetter in second:
            if(firstLetter == secondLetter):
                for thirdLetter in third:
                    if(firstLetter == thirdLetter):
                        return firstLetter


def calcPoints(letter):
    alphabetLowercase = list(string.ascii_lowercase)
    counter = 0
    for letterLowecase in alphabetLowercase:
        counter+=1
        if letterLowecase == letter:
            return counter
    alphabetUppercase = list(string.ascii_uppercase)
    for letterUppercase in alphabetUppercase:
        counter+=1
        if letterUppercase == letter:
            return counter

calc()