import string
file = open("3december.txt","r")
lines = file.readlines()

def calc():
    result = 0
    for line in lines:
        wordLen = len(line)
        first = line[0:wordLen//2]
        second = line[wordLen//2:wordLen]
        letter = findEqualLetter(first,second)
        result = result + calcPoints(letter)
    print(result)


def findEqualLetter(first, second):
    for firstLetter in first:
        for secondLetter in second:
            if(firstLetter == secondLetter):
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